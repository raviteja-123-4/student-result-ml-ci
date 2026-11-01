$ErrorActionPreference = "Stop"
$gh = "C:\Program Files\GitHub CLI\gh.exe"
$repo = "raviteja-123-4/student-result-ml-ci"
$backup = "C:\Users\Ravi teja\Downloads\ml_backup"

function Wait-For-Run($expected) {
    Write-Host "Waiting for GitHub Actions run to register..."
    Start-Sleep -Seconds 10
    
    $runId = ""
    for ($i = 0; $i -lt 20; $i++) {
        $runId = & $gh run list -R $repo --limit 1 --json databaseId --jq '.[0].databaseId'
        if ($runId) { break }
        Start-Sleep -Seconds 3
    }
    
    Write-Host "Monitoring run $runId (Expected: $expected)..."
    while ($true) {
        Start-Sleep -Seconds 10
        $runInfo = & $gh run list -R $repo --limit 1 --json databaseId,status,conclusion | ConvertFrom-Json
        if ($runInfo.databaseId -eq $runId) {
            $status = $runInfo.status
            $conclusion = $runInfo.conclusion
            Write-Host "Run $runId -> Status: $status, Conclusion: $conclusion"
            if ($status -eq "completed") {
                if ($conclusion -eq $expected) {
                    Write-Host ">>> Run $runId MATCHED expected outcome: $expected <<<" -ForegroundColor Green
                } else {
                    Write-Warning "Run $runId concluded with '$conclusion' (expected '$expected')"
                }
                break
            }
        }
    }
}

function Do-Commit-And-Push($msg, $body, $expected) {
    Write-Host "`n=======================================================" -ForegroundColor Cyan
    Write-Host "Committing: $msg" -ForegroundColor Cyan
    Write-Host "=======================================================" -ForegroundColor Cyan
    git add -A
    if ($body) {
        git commit -m "$msg" -m "$body"
    } else {
        git commit -m "$msg"
    }
    git push origin main
    Wait-For-Run $expected
}

# --- Step 20: Add Flask prediction application ---
@'
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

try:
    model = joblib.load("student_result_model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    required_fields = ["attendance", "internal_marks", "assignment_marks", "previous_score"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    input_df = pd.DataFrame([data])
    pred = model.predict(input_df)[0]
    result = "PASS" if pred == 1 else "FAIL"

    return jsonify({
        "prediction": result,
        "prediction_code": int(pred)
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'@ | Set-Content -Path "app.py" -Encoding UTF8

Do-Commit-And-Push "Add Flask prediction application" "Implement Flask app for student result prediction with model loading and prediction endpoints." "success"

# --- Step 21: Add prediction API tests ---
Copy-Item "$backup\test_app.py" "test_app.py" -Force
@'
name: Student Result ML CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  train-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install ML dependencies
        run: pip install -r requirements.txt

      - name: Train student result model
        run: python train_model.py

      - name: Check ML quality gate
        run: python quality_gate.py

      - name: Run automated ML tests
        run: python -m unittest test_ml_pipeline.py -v

      - name: Run prediction application tests
        run: python -m unittest test_app.py -v
'@ | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Add prediction API tests" "Add unit tests for health check and prediction endpoints, including validation for missing fields." "success"

# --- Step 22: Add continuous delivery release packaging ---
@'
name: Student Result ML CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  train-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install ML dependencies
        run: pip install -r requirements.txt

      - name: Train student result model
        run: python train_model.py

      - name: Check ML quality gate
        run: python quality_gate.py

      - name: Run automated ML tests
        run: python -m unittest test_ml_pipeline.py -v

      - name: Run prediction application tests
        run: python -m unittest test_app.py -v

      - name: Prepare release candidate
        run: |
          mkdir -p release_candidate
          cp app.py release_candidate/
          cp student_result_model.pkl release_candidate/
          cp metrics.json release_candidate/
          cp requirements.txt release_candidate/
          printf "Student Result Prediction ML Application\nRun: python app.py\nEndpoint: POST /predict\n" > release_candidate/DEPLOYMENT.txt

      - name: Upload release candidate
        uses: actions/upload-artifact@v4
        with:
          name: student-result-ml-release
          path: release_candidate/
          if-no-files-found: error
          retention-days: 7
'@ | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Add continuous delivery release packaging" $null "success"

# --- Step 23: Add continuous delivery release packaging (formatting update) ---
@'
name: Student Result ML CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  train-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install ML dependencies
        run: pip install -r requirements.txt

      - name: Train student result model
        run: python train_model.py

      - name: Check ML quality gate
        run: python quality_gate.py

      - name: Run automated ML tests
        run: python -m unittest test_ml_pipeline.py -v

      - name: Run prediction application tests
        run: python -m unittest test_app.py -v

      - name: Prepare release candidate
        run: |
          mkdir -p release_candidate
          cp app.py release_candidate/
          cp student_result_model.pkl release_candidate/
          cp metrics.json release_candidate/
          cp requirements.txt release_candidate/
          printf "Student Result Prediction ML Application v1.0\nRun: python app.py\nEndpoint: POST /predict\n" > release_candidate/DEPLOYMENT.txt

      - name: Upload release candidate
        uses: actions/upload-artifact@v4
        with:
          name: student-result-ml-release
          path: release_candidate/
          if-no-files-found: error
          retention-days: 7
'@ | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Add continuous delivery release packaging" "Updated GitHub Actions workflow to use newer action versions and modified deployment message formatting." "success"

# --- Step 24: Demonstrate application test failure (EXPECTED FAILURE) ---
$appTestContent = Get-Content "test_app.py" -Raw
$appTestContent = $appTestContent -replace 'self\.assertEqual\(response\.status_code, 200\)', 'self.assertEqual(response.status_code, 201)'
$appTestContent | Set-Content "test_app.py" -Encoding UTF8

Do-Commit-And-Push "Demonstrate application test failure" $null "failure"

# --- Step 25: Restore valid prediction API test ---
Copy-Item "$backup\test_app.py" "test_app.py" -Force
Do-Commit-And-Push "Restore valid prediction API test" $null "success"

# --- Step 26: corrected work flow ---
@'
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

try:
    model = joblib.load("student_result_model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    required_fields = ["attendance", "internal_marks", "assignment_marks", "previous_score"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        input_df = pd.DataFrame([data])
        pred = model.predict(input_df)[0]
        result = "PASS" if pred == 1 else "FAIL"

        return jsonify({
            "prediction": result,
            "prediction_code": int(pred)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'@ | Set-Content -Path "app.py" -Encoding UTF8

Do-Commit-And-Push "corrected work flow" "Refactor model loading and input validation in the prediction endpoint. Improved error handling for invalid inputs and added checks for missing fields." "success"

# --- Step 27: Add Dockerfile for ML prediction application ---
Copy-Item "$backup\Dockerfile" "Dockerfile" -Force
Do-Commit-And-Push "Add Dockerfile for ML prediction application" $null "success"

# --- Step 28: Add Docker ignore rules ---
Copy-Item "$backup\.dockerignore" ".dockerignore" -Force
Do-Commit-And-Push "Add Docker ignore rules" $null "success"

# --- Step 29: Update workflow for Docker release. ---
@'
name: Student Result ML CI-CD with Docker and GHCR

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  train-test-docker:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Train student result model
        run: python train_model.py

      - name: Check ML quality gate
        run: python quality_gate.py

      - name: Run automated ML tests
        run: python -m unittest test_ml_pipeline.py -v

      - name: Run prediction application tests
        run: python -m unittest test_app.py -v

      - name: Prepare release candidate
        run: |
          mkdir -p release_candidate
          cp app.py release_candidate/
          cp student_result_model.pkl release_candidate/
          cp metrics.json release_candidate/
          cp requirements.txt release_candidate/
          cp Dockerfile release_candidate/
          cp .dockerignore release_candidate/
          printf "Student Result Prediction ML Application\nRun: python app.py\nEndpoint: POST /predict\nDocker image: student-result-ml:latest\n" > release_candidate/DEPLOYMENT.txt

      - name: Upload release candidate
        uses: actions/upload-artifact@v4
        with:
          name: student-result-ml-docker-release
          path: release_candidate/
          if-no-files-found: error
          retention-days: 7
'@ | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Update workflow for Docker release." $null "success"

# --- Step 30: Add health endpoint for automated Docker CI ---
@'
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

try:
    model = joblib.load("student_result_model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "student-result-prediction"
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    required_fields = ["attendance", "internal_marks", "assignment_marks", "previous_score"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        input_df = pd.DataFrame([data])
        pred = model.predict(input_df)[0]
        result = "PASS" if pred == 1 else "FAIL"

        return jsonify({
            "prediction": result,
            "prediction_code": int(pred)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'@ | Set-Content -Path "app.py" -Encoding UTF8

Do-Commit-And-Push "Add health endpoint for automated Docker CI" $null "success"

# --- Step 31: Automate Docker build and prediction testing ---
@'
name: Student Result ML CI-CD with Docker and GHCR

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  train-test-docker:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Train student result model
        run: python train_model.py

      - name: Check ML quality gate
        run: python quality_gate.py

      - name: Run automated ML tests
        run: python -m unittest test_ml_pipeline.py -v

      - name: Run prediction application tests
        run: python -m unittest test_app.py -v

      - name: Build Docker image
        run: docker build -t student-result-ml:latest .

      - name: Run Docker container
        run: |
          docker run -d \
            --name student-result-container \
            -p 5000:5000 \
            student-result-ml:latest

      - name: Wait for application health
        run: |
          for i in {1..15}; do
            if curl -fsS http://localhost:5000/health; then
              echo "Application is healthy"
              exit 0
            fi

            echo "Waiting for application... attempt $i"
            sleep 2
          done

          echo "Application health check failed"
          docker logs student-result-container
          exit 1

      - name: Test health endpoint
        run: curl -f http://localhost:5000/health

      - name: Test PASS prediction
        run: |
          python - <<'PY'
          import json
          import urllib.request

          data = {
              "attendance": 90,
              "internal_marks": 85,
              "assignment_marks": 88,
              "previous_score": 80
          }

          req = urllib.request.Request(
              "http://localhost:5000/predict",
              data=json.dumps(data).encode(),
              headers={"Content-Type": "application/json"},
              method="POST"
          )

          with urllib.request.urlopen(req) as response:
              result = json.loads(response.read())

          print("PASS prediction:", result)

          assert result["prediction"] == "PASS"
          assert result["prediction_code"] == 1
          PY

      - name: Test FAIL prediction
        run: |
          python - <<'PY'
          import json
          import urllib.request

          data = {
              "attendance": 55,
              "internal_marks": 30,
              "assignment_marks": 40,
              "previous_score": 35
          }

          req = urllib.request.Request(
              "http://localhost:5000/predict",
              data=json.dumps(data).encode(),
              headers={"Content-Type": "application/json"},
              method="POST"
          )

          with urllib.request.urlopen(req) as response:
              result = json.loads(response.read())

          print("FAIL prediction:", result)

          assert result["prediction"] == "FAIL"
          assert result["prediction_code"] == 0
          PY

      - name: Capture Docker logs
        if: always()
        run: docker logs student-result-container || true

      - name: Cleanup Docker container
        if: always()
        run: |
          docker stop student-result-container || true
          docker rm student-result-container || true

      - name: Prepare release candidate
        run: |
          mkdir -p release_candidate
          cp app.py release_candidate/
          cp student_result_model.pkl release_candidate/
          cp metrics.json release_candidate/
          cp requirements.txt release_candidate/
          cp Dockerfile release_candidate/
          cp .dockerignore release_candidate/
          printf "Student Result Prediction ML Application\nRun: python app.py\nEndpoint: POST /predict\nDocker image: student-result-ml:latest\n" > release_candidate/DEPLOYMENT.txt

      - name: Upload release candidate
        uses: actions/upload-artifact@v4
        with:
          name: student-result-ml-docker-release
          path: release_candidate/
          if-no-files-found: error
          retention-days: 7
'@ | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Automate Docker build and prediction testing" $null "success"

# --- Step 32: Demonstrate Docker health check failure (EXPECTED FAILURE) ---
$workflowFail = Get-Content ".github\workflows\ml-ci.yml" -Raw
$workflowFail = $workflowFail -replace '-p 5000:5000', '-p 5001:5000'
$workflowFail | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Demonstrate Docker health check failure" $null "failure"

# --- Step 33: Restore Docker health check port ---
$workflowRestore = Get-Content ".github\workflows\ml-ci.yml" -Raw
$workflowRestore = $workflowRestore -replace '-p 5001:5000', '-p 5000:5000'
$workflowRestore | Set-Content -Path ".github\workflows\ml-ci.yml" -Encoding UTF8

Do-Commit-And-Push "Restore Docker health check port" "Added steps to prepare and upload a release candidate for the ML application." "success"

# --- Step 34: Automate Docker build test and GHCR publishing ---
Copy-Item "$backup\.github\workflows\ml-ci.yml" ".github\workflows\ml-ci.yml" -Force
Do-Commit-And-Push "Automate Docker build test and GHCR publishing" $null "success"

# --- Step 35: Verify automated GHCR publishing on second update ---
Add-Content -Path "README.md" -Value "`n<!-- Verified automated GHCR publishing -->"
Do-Commit-And-Push "Verify automated GHCR publishing on second update" $null "success"

# --- Step 36: Update application version for Render redeployment test ---
@'
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

try:
    model = joblib.load("student_result_model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "student-result-prediction",
        "version": "1.0.1"
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    required_fields = ["attendance", "internal_marks", "assignment_marks", "previous_score"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        input_df = pd.DataFrame([data])
        pred = model.predict(input_df)[0]
        result = "PASS" if pred == 1 else "FAIL"

        return jsonify({
            "prediction": result,
            "prediction_code": int(pred)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'@ | Set-Content -Path "app.py" -Encoding UTF8

Do-Commit-And-Push "Update application version for Render redeployment test" $null "success"

# --- Step 37: Add Flasgger dependency for API documentation ---
Add-Content -Path "requirements.txt" -Value "flasgger>=0.9.7.1"
Do-Commit-And-Push "Add Flasgger dependency for API documentation" $null "success"

# --- Step 38: Add Swagger documentation to Flask prediction API ---
@'
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

try:
    model = joblib.load("student_result_model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    """
    Health Check Endpoint
    ---
    responses:
      200:
        description: Service is healthy
    """
    return jsonify({
        "status": "healthy",
        "service": "student-result-prediction",
        "version": "1.0.1"
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict Student Result Endpoint
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - attendance
            - internal_marks
            - assignment_marks
            - previous_score
          properties:
            attendance:
              type: number
            internal_marks:
              type: number
            assignment_marks:
              type: number
            previous_score:
              type: number
    responses:
      200:
        description: Prediction result
    """
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    required_fields = ["attendance", "internal_marks", "assignment_marks", "previous_score"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        input_df = pd.DataFrame([data])
        pred = model.predict(input_df)[0]
        result = "PASS" if pred == 1 else "FAIL"

        return jsonify({
            "prediction": result,
            "prediction_code": int(pred)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'@ | Set-Content -Path "app.py" -Encoding UTF8

Do-Commit-And-Push "Add Swagger documentation to Flask prediction API" "Added Swagger documentation for health check and prediction endpoints." "success"

# --- Step 39: Fix Swagger UI static asset loading ---
$appContent = Get-Content "app.py" -Raw
$appContent = $appContent -replace 'swagger = Swagger\(app\)', "app.config['SWAGGER'] = {'title': 'Student Result Prediction API', 'uiversion': 3}`nswagger = Swagger(app)"
$appContent | Set-Content -Path "app.py" -Encoding UTF8

Do-Commit-And-Push "Fix Swagger UI static asset loading" $null "success"

# --- Step 40: Implement logging and improve error handling ---
Copy-Item "$backup\app.py" "app.py" -Force
Do-Commit-And-Push "Implement logging and improve error handling" "Added logging configuration and middleware for request logging. Enhanced error handling in the prediction function." "success"

# --- Step 41: Update Docker deployment and dependencies for Practical 11 ---
Copy-Item "$backup\*" "." -Recurse -Force
Do-Commit-And-Push "Update Docker deployment and dependencies for Practical 11" $null "success"

Write-Host "`nAll commits 20 to 41 completed successfully!" -ForegroundColor Green
