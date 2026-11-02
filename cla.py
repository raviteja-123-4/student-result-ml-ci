PS C:\Users\Ravi teja> wsl
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja$ curl localhost:8080
<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="alerts.py">alerts.py</a></li>
<li><a href="capture.py">capture.py</a></li>
<li><a href="data/">data/</a></li>
<li><a href="detect.py">detect.py</a></li>
<li><a href="features.py">features.py</a></li>
<li><a href="fusion.py">fusion.py</a></li>
<li><a href="logs/">logs/</a></li>
<li><a href="respond.py">respond.py</a></li>
<li><a href="screenshots/">screenshots/</a></li>
</ul>
<hr>
</body>
</html>
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja$ cd ~
cp -r "/mnt/c/Users/Ravi teja/FloodGuard" ~/FloodGuard   # folder ekkada undo check chesuko
cd ~/FloodGuard
source ~/venv/bin/activate 2>/dev/null || source venv/bin/activate
cp: cannot stat '/mnt/c/Users/Ravi teja/FloodGuard': No such file or directory
-bash: venv/bin/activate: No such file or directory
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
python3 -m venv venv
source venv/bin/activate
pip install scapy pandas scikit-learn joblib streamlit
Collecting scapy
  Using cached scapy-2.8.0-py3-none-any.whl.metadata (5.8 kB)
Collecting pandas
  Using cached pandas-3.1.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (18 kB)
Collecting scikit-learn
  Using cached scikit_learn-1.9.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.3 kB)
Collecting joblib
  Using cached joblib-1.6.0-py3-none-any.whl.metadata (6.5 kB)
Collecting streamlit
  Using cached streamlit-1.66.1-py3-none-any.whl.metadata (10 kB)
Collecting numpy>=2.0.2 (from pandas)
  Using cached numpy-2.5.4-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting python-dateutil>=2.9.0 (from pandas)
  Using cached python_dateutil-3.0.0-py2.py3-none-any.whl.metadata (8.2 kB)
Collecting scipy>=1.10.0 (from scikit-learn)
  Using cached scipy-1.18.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting narwhals>=2.0.1 (from scikit-learn)
  Using cached narwhals-2.28.0-py3-none-any.whl.metadata (15 kB)
Collecting threadpoolctl>=3.5.0 (from scikit-learn)
  Using cached threadpoolctl-3.7.0-py3-none-any.whl.metadata (24 kB)
Collecting cloudpickle>=3.0 (from joblib)
  Using cached cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting altair!=5.4.0,!=5.4.1,<7,>=5.0.0 (from streamlit)
  Using cached altair-6.3.0-py3-none-any.whl.metadata (11 kB)
Collecting click<9,>=7.0 (from streamlit)
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting packaging>=20 (from streamlit)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pillow<14,>=9.2.0 (from streamlit)
  Using cached pillow-13.0.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.1 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Using cached pydeck-0.9.3-py2.py3-none-any.whl.metadata (4.2 kB)
Collecting protobuf<8,>=5.26.1 (from streamlit)
  Using cached protobuf-7.36.2-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
Collecting pyarrow!=25.0.0,<27,>=10.0.1 (from streamlit)
  Using cached pyarrow-26.0.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.0 kB)
Collecting requests<3,>=2.27 (from streamlit)
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting typing-extensions<5,>=4.10.0 (from streamlit)
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting starlette<2,>=0.46.0 (from streamlit)
  Using cached starlette-1.10.0-py3-none-any.whl.metadata (6.6 kB)
Collecting uvicorn<1,>=0.30.0 (from streamlit)
  Using cached uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting anyio<5,>=4.0.0 (from streamlit)
  Using cached anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting python-multipart<1,>=0.0.10 (from streamlit)
  Using cached python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting websockets<18,>=12.0.0 (from streamlit)
  Using cached websockets-17.3-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.3 kB)
Collecting itsdangerous<3,>=2.1.2 (from streamlit)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting watchdog<7,>=2.1.5 (from streamlit)
  Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting idna>=2.8 (from anyio<5,>=4.0.0->streamlit)
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting six>=1.6 (from python-dateutil>=2.9.0->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting tzdata (from python-dateutil>=2.9.0->pandas)
  Using cached tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)
  Using cached charset_normalizer-3.5.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
Collecting urllib3<3,>=1.26 (from requests<3,>=2.27->streamlit)
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting certifi>=2023.5.7 (from requests<3,>=2.27->streamlit)
  Using cached certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Collecting h11>=0.8 (from uvicorn<1,>=0.30.0->streamlit)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached markupsafe-3.0.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Using cached rpds_py-2026.9.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Using cached scapy-2.8.0-py3-none-any.whl (2.8 MB)
Using cached pandas-3.1.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.0 MB)
Using cached scikit_learn-1.9.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (9.2 MB)
Using cached joblib-1.6.0-py3-none-any.whl (306 kB)
Using cached streamlit-1.66.1-py3-none-any.whl (10.4 MB)
Using cached altair-6.3.0-py3-none-any.whl (797 kB)
Using cached anyio-4.15.1-py3-none-any.whl (132 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Using cached cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached narwhals-2.28.0-py3-none-any.whl (490 kB)
Using cached numpy-2.5.4-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.7 MB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pillow-13.0.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
Using cached protobuf-7.36.2-cp310-abi3-manylinux2014_x86_64.whl (343 kB)
Using cached pyarrow-26.0.0-cp312-cp312-manylinux_2_28_x86_64.whl (53.9 MB)
Using cached pydeck-0.9.3-py2.py3-none-any.whl (11.4 MB)
Using cached python_dateutil-3.0.0-py2.py3-none-any.whl (94 kB)
Using cached python_multipart-0.0.32-py3-none-any.whl (30 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached scipy-1.18.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
Using cached starlette-1.10.0-py3-none-any.whl (80 kB)
Using cached threadpoolctl-3.7.0-py3-none-any.whl (26 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached uvicorn-0.54.0-py3-none-any.whl (87 kB)
Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
Using cached websockets-17.3-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (225 kB)
Using cached certifi-2026.10.23-py3-none-any.whl (135 kB)
Using cached charset_normalizer-3.5.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (257 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Using cached tzdata-2026.6-py2.py3-none-any.whl (348 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached markupsafe-3.0.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached rpds_py-2026.9.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (371 kB)
Installing collected packages: websockets, watchdog, urllib3, tzdata, typing-extensions, threadpoolctl, six, scapy, rpds-py, python-multipart, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, itsdangerous, idna, h11, cloudpickle, click, charset_normalizer, certifi, attrs, uvicorn, scipy, requests, referencing, python-dateutil, joblib, jinja2, anyio, starlette, scikit-learn, pydeck, pandas, jsonschema-specifications, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.4 altair-6.3.0 anyio-4.15.1 attrs-26.1.0 certifi-2026.10.23 charset_normalizer-3.5.2 click-8.5.0 cloudpickle-3.1.2 h11-0.16.0 idna-3.20 itsdangerous-2.2.0 jinja2-3.1.6 joblib-1.6.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 narwhals-2.28.0 numpy-2.5.4 packaging-26.3 pandas-3.1.0 pillow-13.0.0 protobuf-7.36.2 pyarrow-26.0.0 pydeck-0.9.3 python-dateutil-3.0.0 python-multipart-0.0.32 referencing-0.37.0 requests-2.34.2 rpds-py-2026.9.1 scapy-2.8.0 scikit-learn-1.9.1 scipy-1.18.1 six-1.17.0 starlette-1.10.0 streamlit-1.66.1 threadpoolctl-3.7.0 typing-extensions-4.16.0 tzdata-2026.6 urllib3-2.8.0 uvicorn-0.54.0 watchdog-6.0.0 websockets-17.3
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 -c "import scapy, pandas, sklearn, joblib, streamlit; print('All OK')"
All OK
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard && source venv/bin/activate
python3 -m http.server 8080
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/lib/python3.12/http/server.py", line 1314, in <module>
    test(
  File "/usr/lib/python3.12/http/server.py", line 1261, in test
    with ServerClass(addr, HandlerClass) as httpd:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/socketserver.py", line 457, in __init__
    self.server_bind()
  File "/usr/lib/python3.12/http/server.py", line 1308, in server_bind
    return super().server_bind()
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/http/server.py", line 136, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.12/socketserver.py", line 473, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard && source venv/bin/activate
cat > traffic_normal.py << 'EOF'
import random, time, urllib.request

URL = "http://127.0.0.1:8080/"
DURATION = 180  # seconds

end = time.time() + DURATION
count = 0
while time.time() < end:
    try:
        urllib.request.urlopen(URL, timeout=3).read()
        count += 1
    except Exception as e:
        print("err", e)
    time.sleep(random.uniform(0.2, 2.0))
print("done, requests:", count)
EOF
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
sudo tcpdump -i lo -w data/normal.pcap port 8080
[sudo] password for raviteja:
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
^C0 packets captured
0 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -lh data/normal.pcap
sudo tcpdump -r data/normal.pcap | head
-rw-r--r-- 1 tcpdump tcpdump 24 Oct 28 14:28 data/normal.pcap
reading from file data/normal.pcap, link-type EN10MB (Ethernet), snapshot length 262144
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard && source venv/bin/activate
python3 -m http.server 8080
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/lib/python3.12/http/server.py", line 1314, in <module>
    test(
  File "/usr/lib/python3.12/http/server.py", line 1261, in test
    with ServerClass(addr, HandlerClass) as httpd:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/socketserver.py", line 457, in __init__
    self.server_bind()
  File "/usr/lib/python3.12/http/server.py", line 1308, in server_bind
    return super().server_bind()
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/http/server.py", line 136, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.12/socketserver.py", line 473, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
sudo tcpdump -i lo -w data/normal.pcap port 8080
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
^C0 packets captured
0 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard && source venv/bin/activate
curl -s localhost:8080 | head -3
<!DOCTYPE HTML>
<html lang="en">
<head>
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo -v
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo tcpdump -i lo -w data/normal.pcap port 8080 &
[1] 1457
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes

(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 traffic_normal.py
^CTraceback (most recent call last):
  File "/home/raviteja/FloodGuard/traffic_normal.py", line 14, in <module>
    time.sleep(random.uniform(0.2, 2.0))
KeyboardInterrupt

(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo pkill tcpdump
1044 packets captured
2088 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -lh data/normal.pcap
sudo tcpdump -r data/normal.pcap | head
-rw-r--r-- 1 tcpdump tcpdump 165K Oct 28 14:34 data/normal.pcap
[1]+  Done                    sudo tcpdump -i lo -w data/normal.pcap port 8080
reading from file data/normal.pcap, link-type EN10MB (Ethernet), snapshot length 262144
14:32:17.713376 IP localhost.34330 > localhost.http-alt: Flags [S], seq 1249242578, win 65495, options [mss 65495,sackOK,TS val 3074678622 ecr 0,nop,wscale 10], length 0
14:32:17.713436 IP localhost.http-alt > localhost.34330: Flags [S.], seq 2007767004, ack 1249242579, win 65483, options [mss 65495,sackOK,TS val 2915534051 ecr 3074678622,nop,wscale 10], length 0
14:32:17.713452 IP localhost.34330 > localhost.http-alt: Flags [.], ack 1, win 64, options [nop,nop,TS val 3074678622 ecr 2915534051], length 0
14:32:17.713580 IP localhost.34330 > localhost.http-alt: Flags [P.], seq 1:119, ack 1, win 64, options [nop,nop,TS val 3074678622 ecr 2915534051], length 118: HTTP: GET / HTTP/1.1
14:32:17.713586 IP localhost.http-alt > localhost.34330: Flags [.], ack 119, win 64, options [nop,nop,TS val 2915534051 ecr 3074678622], length 0
14:32:17.715009 IP localhost.http-alt > localhost.34330: Flags [P.], seq 1:156, ack 119, win 64, options [nop,nop,TS val 2915534053 ecr 3074678622], length 155: HTTP: HTTP/1.0 200 OK
14:32:17.715050 IP localhost.34330 > localhost.http-alt: Flags [.], ack 156, win 64, options [nop,nop,TS val 3074678624 ecr 2915534053], length 0
14:32:17.715083 IP localhost.http-alt > localhost.34330: Flags [P.], seq 156:822, ack 119, win 64, options [nop,nop,TS val 2915534053 ecr 3074678624], length 666: HTTP
14:32:17.715099 IP localhost.34330 > localhost.http-alt: Flags [.], ack 822, win 64, options [nop,nop,TS val 3074678624 ecr 2915534053], length 0
14:32:17.715219 IP localhost.http-alt > localhost.34330: Flags [F.], seq 822, ack 119, win 64, options [nop,nop,TS val 2915534053 ecr 3074678624], length 0
tcpdump: Unable to write output: Broken pipe
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo tcpdump -i lo -w data/normal.pcap port 8080 &
python3 traffic_normal.py
sudo pkill tcpdump
[1] 1578
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
done, requests: 165
1980 packets captured
3960 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cp data/normal.pcap data/normal_backup.pcap
git add . && git commit -m "Day 2: normal traffic captured" && git push
[1]+  Done                    sudo tcpdump -i lo -w data/normal.pcap port 8080
fatal: not a git repository (or any of the parent directories): .git
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard && source venv/bin/activate
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo tcpdump -i lo -w data/attack_syn.pcap port 8080 &
sleep 2
sudo hping3 -S -p 8080 -c 5000 -i u1000 --rand-source 127.0.0.1
sleep 2
sudo pkill tcpdump
[1] 1772
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
HPING 127.0.0.1 (lo 127.0.0.1): S set, 40 headers + 0 data bytes
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=68 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=130 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=138 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=184 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=195 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=216 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=220 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=282 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=287 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=340 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=357 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=374 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=378 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=403 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=434 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=441 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=453 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=465 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=480 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=522 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=557 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=565 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=572 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=579 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=582 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=602 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=648 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=659 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=661 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=676 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=688 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=726 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=766 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=768 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=787 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=832 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=861 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=862 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=889 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=957 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=958 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=966 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=994 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1012 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1063 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1134 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1138 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1170 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1186 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1236 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1243 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1284 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1285 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1292 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1296 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1309 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1317 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1348 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1360 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1418 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1433 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1459 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1461 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1469 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1499 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1501 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1506 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1520 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1521 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1562 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1655 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1667 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1703 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1713 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1744 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1745 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1778 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1786 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1789 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1827 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1865 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1877 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1879 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1883 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1899 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1943 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1953 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1982 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2011 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2055 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2057 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2073 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2074 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2079 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2114 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2142 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2145 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2165 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2198 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2243 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2262 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2271 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2299 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2331 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2388 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2389 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2392 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2399 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2407 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2436 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2472 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2496 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2509 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2529 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2555 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2562 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2566 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2570 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2593 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2608 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2636 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2647 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2693 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2699 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2719 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2731 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2742 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2790 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2799 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2806 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2824 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2835 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2843 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2857 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2866 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2868 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2874 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2890 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2900 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2965 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2974 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2975 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2977 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2984 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2986 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2994 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3002 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3017 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3018 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3026 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3037 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3052 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3097 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3139 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3173 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3188 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3200 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3205 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3265 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3270 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3298 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3332 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3366 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3369 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3390 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3405 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3413 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3416 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3422 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3434 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3466 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3516 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3518 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3535 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3602 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3604 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3611 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3612 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3622 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3627 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3629 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3634 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3640 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3643 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3662 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3674 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3706 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3722 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3727 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3736 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3741 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3785 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3806 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3816 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3832 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3838 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3856 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3872 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3891 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3893 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3976 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4020 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4021 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4030 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4056 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4057 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4074 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4106 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4119 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4142 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4143 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4172 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4176 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4257 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4287 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4391 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4394 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4400 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4401 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4402 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4408 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4412 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4470 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4473 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4478 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4485 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4517 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4518 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4562 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4572 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4584 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4624 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4653 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4692 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4704 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4753 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4763 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4768 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4829 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4838 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4854 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4903 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4925 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4935 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4951 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4957 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4977 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4982 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4995 win=65495 rtt=0.1 ms

--- 127.0.0.1 hping statistic ---
5000 packets transmitted, 250 packets received, 95% packet loss
round-trip min/avg/max = 0.0/0.6/1.1 ms
5319 packets captured
10638 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo tcpdump -i lo -w data/attack_udp.pcap udp port 9999 or icmp &
sleep 2
sudo hping3 --udp -p 9999 -c 5000 -i u1000 --rand-source 127.0.0.1
sleep 2
sudo pkill tcpdump
[2] 1785
[1]   Done                    sudo tcpdump -i lo -w data/attack_syn.pcap port 8080
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
HPING 127.0.0.1 (lo 127.0.0.1): udp mode set, 28 headers + 0 data bytes
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1720 seq=26
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1735 seq=41
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1765 seq=71
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1817 seq=123
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1820 seq=126
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1850 seq=156
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1855 seq=161
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1859 seq=165
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1914 seq=220
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1938 seq=244
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1945 seq=251
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1952 seq=258
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1956 seq=262
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1972 seq=278
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=1991 seq=297
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2010 seq=316
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2031 seq=337
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2033 seq=339
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2035 seq=341
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2101 seq=407
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2105 seq=411
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2182 seq=488
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2200 seq=506
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2202 seq=508
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2208 seq=514
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2226 seq=532
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2321 seq=627
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2322 seq=628
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2372 seq=678
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2393 seq=699
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2403 seq=709
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2429 seq=735
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2477 seq=783
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2597 seq=903
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2614 seq=920
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2676 seq=982
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2679 seq=985
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2702 seq=1008
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2721 seq=1027
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2752 seq=1058
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2800 seq=1106
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2817 seq=1123
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2946 seq=1252
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2954 seq=1260
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3017 seq=1323
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3072 seq=1378
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3075 seq=1381
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3133 seq=1439
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3163 seq=1469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3175 seq=1481
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3199 seq=1505
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3202 seq=1508
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3204 seq=1510
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3238 seq=1544
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3267 seq=1573
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3310 seq=1616
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3311 seq=1617
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3325 seq=1631
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3360 seq=1666
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3384 seq=1690
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3385 seq=1691
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3417 seq=1723
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3423 seq=1729
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3491 seq=1797
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3509 seq=1815
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3517 seq=1823
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3544 seq=1850
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3546 seq=1852
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3556 seq=1862
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3596 seq=1902
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3625 seq=1931
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3640 seq=1946
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3644 seq=1950
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3690 seq=1996
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3695 seq=2001
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3741 seq=2047
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3840 seq=2146
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3849 seq=2155
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3851 seq=2157
 name=localhost
status=0 port=3861 seq=2167
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3862 seq=2168
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3881 seq=2187
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3960 seq=2266
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3980 seq=2286
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3999 seq=2305
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4023 seq=2329
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4115 seq=2421
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4118 seq=2424
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4120 seq=2426
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4128 seq=2434
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4139 seq=2445
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4187 seq=2493
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4227 seq=2533
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4246 seq=2552
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4249 seq=2555
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4329 seq=2635
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4335 seq=2641
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4341 seq=2647
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4343 seq=2649
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4376 seq=2682
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4393 seq=2699
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4405 seq=2711
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4409 seq=2715
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4426 seq=2732
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4468 seq=2774
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4472 seq=2778
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4476 seq=2782
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4492 seq=2798
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4501 seq=2807
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4508 seq=2814
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4525 seq=2831
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4590 seq=2896
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4632 seq=2938
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4641 seq=2947
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4659 seq=2965
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4718 seq=3024
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4729 seq=3035
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4802 seq=3108
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4805 seq=3111
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4837 seq=3143
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4843 seq=3149
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4851 seq=3157
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4859 seq=3165
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4887 seq=3193
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4896 seq=3202
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4908 seq=3214
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4935 seq=3241
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4951 seq=3257
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4954 seq=3260
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4963 seq=3269
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4968 seq=3274
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4973 seq=3279
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4997 seq=3303
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4999 seq=3305
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5039 seq=3345
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5051 seq=3357
 name=localhost
status=0 port=5082 seq=3388
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5131 seq=3437
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5145 seq=3451
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5151 seq=3457
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5182 seq=3488
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5185 seq=3491
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5197 seq=3503
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5224 seq=3530
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5241 seq=3547
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5288 seq=3594
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5294 seq=3600
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5302 seq=3608
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5311 seq=3617
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5376 seq=3682
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5444 seq=3750
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5451 seq=3757
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5465 seq=3771
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5502 seq=3808
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5519 seq=3825
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5567 seq=3873
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5582 seq=3888
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5593 seq=3899
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5601 seq=3907
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5608 seq=3914
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5644 seq=3950
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5671 seq=3977
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5749 seq=4055
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5760 seq=4066
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5765 seq=4071
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5800 seq=4106
 name=localhost
status=0 port=5805 seq=4111
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5811 seq=4117
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5824 seq=4130
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5827 seq=4133
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5846 seq=4152
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5855 seq=4161
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5857 seq=4163
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5879 seq=4185
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5884 seq=4190
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5971 seq=4277
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5985 seq=4291
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5990 seq=4296
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6020 seq=4326
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6047 seq=4353
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6087 seq=4393
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6094 seq=4400
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6099 seq=4405
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6121 seq=4427
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6136 seq=4442
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6138 seq=4444
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6139 seq=4445
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6204 seq=4510
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6258 seq=4564
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6265 seq=4571
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6294 seq=4600
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6347 seq=4653
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6350 seq=4656
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6391 seq=4697
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6429 seq=4735
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6445 seq=4751
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6456 seq=4762
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6471 seq=4777
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6490 seq=4796
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6538 seq=4844
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6568 seq=4874
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6576 seq=4882
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6591 seq=4897
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6599 seq=4905
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6602 seq=4908
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6605 seq=4911
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6681 seq=4987

--- 127.0.0.1 hping statistic ---
5000 packets transmitted, 207 packets received, 96% packet loss
round-trip min/avg/max = 0.1/0.8/1.7 ms
5253 packets captured
10506 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cat > attack_http.py << 'EOF'
import threading, time, urllib.request

URL = "http://127.0.0.1:8080/"
THREADS = 20
DURATION = 20  # seconds, keep short

def worker(end):
    while time.time() < end:
        try:
            urllib.request.urlopen(URL, timeout=2).read()
        except Exception:
            pass

end = time.time() + DURATION
ts = [threading.Thread(target=worker, args=(end,)) for _ in range(THREADS)]
[t.start() for t in ts]
[t.join() for t in ts]
print("http flood done")
EOF
[2]+  Done                    sudo tcpdump -i lo -w data/attack_udp.pcap udp port 9999 or icmp
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sudo tcpdump -i lo -w data/attack_http.pcap port 8080 &
sleep 2
python3 attack_http.py
sleep 2
sudo pkill tcpdump
[1] 1801
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
http flood done
68799 packets captured
137598 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -lh data/*.pcap
-rw-r--r-- 1 tcpdump  tcpdump   11M Oct 28 14:41 data/attack_http.pcap
-rw-r--r-- 1 tcpdump  tcpdump  365K Oct 28 14:39 data/attack_syn.pcap
-rw-r--r-- 1 tcpdump  tcpdump  305K Oct 28 14:40 data/attack_udp.pcap
-rw-r--r-- 1 tcpdump  tcpdump  313K Oct 28 14:38 data/normal.pcap
-rw-r--r-- 1 raviteja raviteja 313K Oct 28 14:38 data/normal_backup.pcap
[1]+  Done                    sudo tcpdump -i lo -w data/attack_http.pcap port 8080
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ git add . && git commit -m "Day 3: attack pcaps" && git push
fatal: not a git repository (or any of the parent directories): .git
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
git init
git config user.name "Ravi Teja"
git config user.email "your-github-email@example.com"
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/raviteja/FloodGuard/.git/
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cat > .gitignore << 'EOF'
venv/
__pycache__/
data/*.pcap
*.pkl
EOF
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ git add .
git commit -m "Day 1-3: setup, normal and attack traffic capture"
git branch -M main
git remote add origin https://github.com/<username>/FloodGuard.git
git push -u origin main
[master (root-commit) 20db079] Day 1-3: setup, normal and attack traffic capture
 9 files changed, 37 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 alerts.py
 create mode 100644 attack_http.py
 create mode 100644 capture.py
 create mode 100644 detect.py
 create mode 100644 features.py
 create mode 100644 fusion.py
 create mode 100644 respond.py
 create mode 100644 traffic_normal.py
-bash: username: No such file or directory
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ git remote add origin https://github.com/NEE-USERNAME/FloodGuard.git
git push -u origin main
Username for 'https://github.com': FloodGuard.git
Password for 'https://FloodGuard.git@github.com':
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/NEE-USERNAME/FloodGuard.git/'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ git branch -M main
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ git remote add origin https://github.com/NEE-USERNAME/FloodGuard.git
error: remote origin already exists.
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ git push -u origin main
Username for 'https://github.com': raviteja
Password for 'https://raviteja@github.com':
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/NEE-USERNAME/FloodGuard.git/'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard && source venv/bin/activate

sudo tcpdump -i lo -w data/attack_syn.pcap port 8080 &
sleep 2
sudo hping3 -S -p 8080 -c 30000 -i u1000 --rand-source 127.0.0.1
sleep 2
sudo pkill tcpdump

sudo tcpdump -i lo -w data/attack_udp.pcap udp port 9999 or icmp &
sleep 2
sudo hping3 --udp -p 9999 -c 30000 -i u1000 --rand-source 127.0.0.1
sleep 2
sudo pkill tcpdump
[1] 7606
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
HPING 127.0.0.1 (lo 127.0.0.1): S set, 40 headers + 0 data bytes
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=34 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=35 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=89 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=105 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=106 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=115 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=132 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=137 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=139 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=147 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=155 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=163 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=204 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=217 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=230 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=252 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=305 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=358 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=359 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=371 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=383 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=406 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=409 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=413 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=438 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=449 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=481 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=495 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=511 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=558 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=560 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=561 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=572 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=580 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=583 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=593 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=608 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=621 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=657 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=666 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=673 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=683 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=688 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=690 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=692 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=771 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=779 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=783 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=789 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=790 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=794 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=800 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=806 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=880 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=887 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=900 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=907 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=911 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=918 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=921 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=942 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=948 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=997 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=999 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1036 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1116 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1159 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1185 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1200 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1213 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1217 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1241 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1259 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1305 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1307 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1313 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1352 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1414 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1423 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1474 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1487 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1501 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1553 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1555 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1610 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1612 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1656 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1672 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1708 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1718 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1740 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1748 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1772 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1794 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1807 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1808 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1811 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1813 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1826 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1832 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1837 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1840 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1906 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1911 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1929 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1956 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=1974 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2020 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2029 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2093 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2109 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2117 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2138 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2193 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2211 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2247 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2277 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2286 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2303 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2323 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2334 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2360 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2363 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2369 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2379 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2388 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2404 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2408 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2433 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2461 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2475 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2496 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2576 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2669 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2680 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2695 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2724 win=65495 rtt=1000.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2740 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2743 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2769 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2810 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2828 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2863 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2897 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2906 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2914 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2940 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2950 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2965 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=2986 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3008 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3021 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3043 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3055 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3064 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3086 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3115 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3121 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3142 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3207 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3234 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3237 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3254 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3255 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3280 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3292 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3294 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3307 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3315 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3320 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3353 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3355 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3374 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3408 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3413 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3420 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3434 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3468 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3473 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3485 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3520 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3530 win=65495 rtt=1000.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3538 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3542 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3599 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3642 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3654 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3727 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3740 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3765 win=65495 rtt=1.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3768 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3791 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3794 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3808 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3823 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3828 win=65495 rtt=1.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3830 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3835 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3843 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3847 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3858 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3875 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3876 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3877 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3880 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3893 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3912 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3924 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3944 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3962 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3995 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=3998 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4019 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4024 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4041 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4044 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4060 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4087 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4089 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4128 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4137 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4154 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4172 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4188 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4203 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4215 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4221 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4264 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4290 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4303 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4330 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4356 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4359 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4366 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4392 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4399 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4401 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4412 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4420 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4449 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4455 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4569 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4581 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4593 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4615 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4624 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4627 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4628 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4641 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4664 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4711 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4736 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4790 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4794 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4801 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4805 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4820 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4822 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4862 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4877 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4939 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4943 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=4972 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5024 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5033 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5036 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5040 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5050 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5064 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5065 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5071 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5079 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5090 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5095 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5123 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5155 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5210 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5214 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5229 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5242 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5318 win=65495 rtt=1.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5358 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5364 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5375 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5401 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5419 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5420 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5476 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5501 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5522 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5525 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5532 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5546 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5587 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5596 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5637 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5642 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5675 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5692 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5711 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5718 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5745 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5754 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5782 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5789 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5803 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5807 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5818 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5831 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5835 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5845 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5916 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5941 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5943 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5951 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5959 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5970 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=5973 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6030 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6077 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6121 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6157 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6162 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6175 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6178 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6209 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6239 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6259 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6292 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6344 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6400 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6414 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6485 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6490 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6588 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6597 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6655 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6666 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6676 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6684 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6749 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6767 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6783 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6789 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6797 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6862 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6871 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6880 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6891 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6917 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6923 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6938 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6968 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6979 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6988 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6995 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=6996 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7006 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7013 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7020 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7039 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7069 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7100 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7109 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7170 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7176 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7189 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7196 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7226 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7276 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7282 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7302 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7326 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7353 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7355 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7367 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7373 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7392 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7427 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7480 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7491 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7501 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7504 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7526 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7551 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7553 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7569 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7579 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7601 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7617 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7620 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7637 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7642 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7700 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7728 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7742 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7778 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7789 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7807 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7836 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7859 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7871 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7909 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7935 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7952 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7960 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=7980 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8022 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8026 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8036 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8042 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8097 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8102 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8109 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8119 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8153 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8155 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8169 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8174 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8183 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8217 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8241 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8312 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8329 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8337 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8339 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8359 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8367 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8390 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8420 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8438 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8457 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8461 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8468 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8486 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8492 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8504 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8518 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8519 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8524 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8525 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8559 win=65495 rtt=1.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8598 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8640 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8718 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8729 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8755 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8779 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8786 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8804 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8863 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8867 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8879 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8889 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8898 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8918 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8970 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=8995 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9069 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9084 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9100 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9104 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9105 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9136 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9177 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9249 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9252 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9259 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9273 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9281 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9290 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9300 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9312 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9322 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9354 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9408 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9420 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9480 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9549 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9569 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9574 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9605 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9607 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9641 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9668 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9725 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9728 win=65495 rtt=1.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9743 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9745 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9752 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9782 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9792 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9796 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9869 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9871 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9927 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9974 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=9975 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10045 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10055 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10075 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10126 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10127 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10137 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10191 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10210 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10233 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10248 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10256 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10261 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10264 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10287 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10294 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10343 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10353 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10378 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10390 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10414 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10447 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10479 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10480 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10481 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10482 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10543 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10576 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10580 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10586 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10655 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10660 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10665 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10684 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10717 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10734 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10736 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10738 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10785 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10803 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10804 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10865 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10875 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10902 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10917 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10918 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10924 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10941 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=10966 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11032 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11037 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11050 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11061 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11089 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11096 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11109 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11110 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11126 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11142 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11150 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11185 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11226 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11228 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11239 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11254 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11261 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11270 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11273 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11315 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11322 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11333 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11345 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11362 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11390 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11425 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11433 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11441 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11446 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11468 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11497 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11504 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11516 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11531 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11532 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11547 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11560 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11562 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11565 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11612 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11629 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11652 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11680 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11699 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11734 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11745 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11780 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11797 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11862 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11874 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11894 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11922 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11935 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11947 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11973 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=11999 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12040 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12047 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12060 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12062 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12088 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12111 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12116 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12199 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12225 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12250 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12266 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12267 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12268 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12310 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12313 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12322 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12323 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12327 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12353 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12379 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12397 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12399 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12428 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12435 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12465 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12473 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12488 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12491 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12530 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12586 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12611 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12647 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12654 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12663 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12666 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12715 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12759 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12782 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12801 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12882 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12893 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12906 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12911 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12929 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12945 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12952 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12955 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12991 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=12999 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13003 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13007 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13027 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13028 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13033 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13055 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13081 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13085 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13090 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13105 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13115 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13122 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13126 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13140 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13152 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13162 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13172 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13191 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13219 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13247 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13290 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13295 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13314 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13315 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13317 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13323 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13328 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13359 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13360 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13380 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13395 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13396 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13426 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13431 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13492 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13508 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13544 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13548 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13563 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13583 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13614 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13628 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13633 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13661 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13680 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13686 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13697 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13746 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13749 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13760 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13762 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13767 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13817 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13905 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13933 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13934 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13955 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13962 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13963 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=13974 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14017 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14020 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14026 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14028 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14062 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14066 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14091 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14095 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14110 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14113 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14119 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14178 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14198 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14208 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14219 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14245 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14251 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14264 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14274 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14333 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14404 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14407 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14426 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14458 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14470 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14475 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14492 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14507 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14515 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14528 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14548 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14568 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14606 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14616 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14647 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14661 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14668 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14672 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14693 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14716 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14747 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14748 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14770 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14786 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14801 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14813 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14824 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14837 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14880 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14894 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14977 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14979 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14980 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14992 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=14995 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15004 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15021 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15023 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15035 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15063 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15067 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15101 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15104 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15116 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15121 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15143 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15170 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15173 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15175 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15184 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15186 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15207 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15210 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15227 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15257 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15272 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15301 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15315 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15347 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15385 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15388 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15391 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15403 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15408 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15412 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15422 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15424 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15455 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15484 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15496 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15508 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15511 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15518 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15573 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15576 win=65495 rtt=1.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15583 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15586 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15607 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15732 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15734 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15754 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15804 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15805 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15833 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15842 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15845 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15875 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15882 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15896 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15915 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15923 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15945 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15958 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=15982 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16016 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16019 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16022 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16026 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16029 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16058 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16082 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16088 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16178 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16201 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16232 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16277 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16340 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16367 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16394 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16405 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16407 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16445 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16476 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16484 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16495 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16500 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16510 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16529 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16533 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16590 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16652 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16662 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16698 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16699 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16732 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16734 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16772 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16794 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16855 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16864 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16917 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16923 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16925 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16941 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16961 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16967 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16970 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16975 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=16988 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17026 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17039 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17048 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17077 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17103 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17129 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17138 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17148 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17198 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17217 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17223 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17230 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17244 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17253 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17255 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17316 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17319 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17337 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17338 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17353 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17388 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17411 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17425 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17452 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17495 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17555 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17562 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17578 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17611 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17620 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17655 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17690 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17742 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17745 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17746 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17771 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17775 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17809 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17819 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17838 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17872 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17895 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17938 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17945 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17948 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17950 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17968 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17977 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=17990 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18001 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18052 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18071 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18110 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18123 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18135 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18152 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18165 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18171 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18175 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18187 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18216 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18256 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18261 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18270 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18285 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18287 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18311 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18334 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18335 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18369 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18415 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18431 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18448 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18478 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18481 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18511 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18523 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18532 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18541 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18546 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18547 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18556 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18567 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18608 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18610 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18625 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18628 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18647 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18650 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18651 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18656 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18667 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18735 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18752 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18760 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18833 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18864 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18889 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18921 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18929 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18942 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18947 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18973 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18983 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=18994 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19035 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19039 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19049 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19058 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19083 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19104 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19105 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19109 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19124 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19165 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19205 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19221 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19250 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19259 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19260 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19291 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19315 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19354 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19365 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19366 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19381 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19388 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19403 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19405 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19490 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19519 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19521 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19530 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19532 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19551 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19572 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19575 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19596 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19627 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19639 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19650 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19704 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19721 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19748 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19764 win=65495 rtt=1.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19765 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19803 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19817 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19851 win=65495 rtt=1000.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19870 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19891 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19926 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19949 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19955 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19965 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19969 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19972 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=19991 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20009 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20085 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20129 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20141 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20155 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20175 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20194 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20201 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20208 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20220 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20226 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20244 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20265 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20272 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20284 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20300 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20308 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20334 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20338 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20362 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20380 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20402 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20409 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20416 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20427 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20435 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20455 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20463 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20473 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20485 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20492 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20499 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20601 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20688 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20702 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20726 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20736 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20738 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20746 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20767 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20846 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20857 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20862 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20864 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20865 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20869 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20879 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20889 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20898 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=20930 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21006 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21018 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21035 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21037 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21038 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21045 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21074 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21075 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21077 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21098 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21118 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21147 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21150 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21175 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21214 win=65495 rtt=1.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21224 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21231 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21232 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21271 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21272 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21274 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21314 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21334 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21342 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21370 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21387 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21388 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21400 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21405 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21406 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21421 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21430 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21552 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21571 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21577 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21583 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21587 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21605 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21611 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21623 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21624 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21639 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21684 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21693 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21707 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21734 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21763 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21766 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21777 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21789 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21790 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21795 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21800 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21809 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21819 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21820 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21848 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21864 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21871 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21927 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21935 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21965 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21971 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21989 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=21993 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22017 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22020 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22053 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22058 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22069 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22100 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22101 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22139 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22171 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22200 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22204 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22210 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22225 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22228 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22249 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22256 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22288 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22294 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22308 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22361 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22365 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22376 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22435 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22447 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22492 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22499 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22507 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22537 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22548 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22562 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22565 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22576 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22599 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22609 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22637 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22641 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22646 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22647 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22650 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22670 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22681 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22683 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22698 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22726 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22742 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22746 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22758 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22803 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22812 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22862 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22914 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22937 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22969 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=22974 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23084 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23087 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23088 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23099 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23101 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23140 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23173 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23185 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23204 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23207 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23258 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23275 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23289 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23349 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23373 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23379 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23388 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23397 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23419 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23432 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23459 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23464 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23467 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23555 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23569 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23571 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23573 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23584 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23597 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23602 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23629 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23646 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23657 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23663 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23686 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23763 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23822 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23842 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23843 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23845 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23920 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23954 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23978 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=23994 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24003 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24011 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24030 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24069 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24075 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24085 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24088 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24095 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24107 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24122 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24137 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24139 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24171 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24189 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24191 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24195 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24212 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24235 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24261 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24272 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24279 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24283 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24306 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24322 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24329 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24333 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24334 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24335 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24339 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24382 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24407 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24415 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24419 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24422 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24427 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24444 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24474 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24477 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24527 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24552 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24563 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24571 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24572 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24609 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24611 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24612 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24625 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24641 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24660 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24669 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24701 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24740 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24755 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24758 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24781 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24789 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24790 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24807 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24817 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24839 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24865 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24869 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24872 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24912 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24916 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24935 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24943 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24956 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24957 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24965 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24982 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24984 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=24996 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25036 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25048 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25052 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25054 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25062 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25095 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25120 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25172 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25175 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25186 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25217 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25231 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25236 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25254 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25255 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25271 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25277 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25284 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25294 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25334 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25342 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25412 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25438 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25458 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25479 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25492 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25540 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25542 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25557 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25560 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25585 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25593 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25604 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25615 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25622 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25674 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25694 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25737 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25744 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25749 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25819 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25821 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25825 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25845 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25887 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25906 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25910 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25912 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25914 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25939 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25975 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=25993 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26028 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26049 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26055 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26080 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26096 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26106 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26110 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26117 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26143 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26146 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26172 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26179 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26207 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26213 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26223 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26236 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26237 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26246 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26249 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26253 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26316 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26354 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26398 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26405 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26437 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26453 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26475 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26488 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26494 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26499 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26507 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26516 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26524 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26528 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26550 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26558 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26561 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26562 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26565 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26568 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26592 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26593 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26596 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26600 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26603 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26631 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26652 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26659 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26663 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26681 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26720 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26739 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26789 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26802 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26803 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26834 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26846 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26894 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26899 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26919 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26930 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26936 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26962 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26973 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=26976 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27010 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27050 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27057 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27070 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27080 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27082 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27101 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27123 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27138 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27153 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27161 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27163 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27179 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27196 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27213 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27222 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27224 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27258 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27277 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27286 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27304 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27320 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27339 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27349 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27378 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27390 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27406 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27425 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27435 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27440 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27468 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27495 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27523 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27540 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27553 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27573 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27574 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27594 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27629 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27643 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27647 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27657 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27659 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27660 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27674 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27681 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27700 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27705 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27716 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27736 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27739 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27757 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27781 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27808 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27810 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27825 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27853 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27859 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27877 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27903 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27911 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27917 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27976 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=27990 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28029 win=65495 rtt=0.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28038 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28067 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28089 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28091 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28092 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28095 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28097 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28126 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28128 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28149 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28164 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28184 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28222 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28228 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28241 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28247 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28253 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28265 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28271 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28305 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28309 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28324 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28350 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28388 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28415 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28423 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28439 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28477 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28487 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28522 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28539 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28574 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28581 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28589 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28596 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28598 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28619 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28644 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28650 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28653 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28655 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28666 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28679 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28683 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28694 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28707 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28716 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28736 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28744 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28760 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28781 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28817 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28843 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28901 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28946 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28948 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28960 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28965 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=28988 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29017 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29050 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29060 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29076 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29129 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29131 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29162 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29173 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29213 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29243 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29368 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29386 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29393 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29406 win=65495 rtt=1.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29407 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29432 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29453 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29485 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29499 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29519 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29558 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29600 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29608 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29609 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29611 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29636 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29650 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29652 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29660 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29668 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29725 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29731 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29734 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29748 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29774 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29775 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29777 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29787 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29798 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29800 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29809 win=65495 rtt=0.1 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29810 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29812 win=65495 rtt=0.5 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29822 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29831 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29837 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29842 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29865 win=65495 rtt=0.4 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29872 win=65495 rtt=0.9 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29873 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29874 win=65495 rtt=0.7 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29931 win=65495 rtt=1.0 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29934 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29947 win=65495 rtt=0.8 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29948 win=65495 rtt=0.6 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29978 win=65495 rtt=0.2 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29986 win=65495 rtt=0.3 ms
len=44 ip=127.0.0.1 ttl=64 DF id=0 sport=8080 flags=SA seq=29999 win=65495 rtt=0.1 ms

--- 127.0.0.1 hping statistic ---
30000 packets transmitted, 1634 packets received, 95% packet loss
round-trip min/avg/max = 0.0/2.5/1000.8 ms
31887 packets captured
63774 packets received by filter
0 packets dropped by kernel
[2] 7625
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
[1]-  Done                    sudo tcpdump -i lo -w data/attack_syn.pcap port 8080
HPING 127.0.0.1 (lo 127.0.0.1): udp mode set, 28 headers + 0 data bytes
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2022 seq=19
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2068 seq=65
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2088 seq=85
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2113 seq=110
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2116 seq=113
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2128 seq=125
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2132 seq=129
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2213 seq=210
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2226 seq=223
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2235 seq=232
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2249 seq=246
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2257 seq=254
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2309 seq=306
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2360 seq=357
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2410 seq=407
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2412 seq=409
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2446 seq=443
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2473 seq=470
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2498 seq=495
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2510 seq=507
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2516 seq=513
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2519 seq=516
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2541 seq=538
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2607 seq=604
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2608 seq=605
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2612 seq=609
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2637 seq=634
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2639 seq=636
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2692 seq=689
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2700 seq=697
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2707 seq=704
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2711 seq=708
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2724 seq=721
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2735 seq=732
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2741 seq=738
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2746 seq=743
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2758 seq=755
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2797 seq=794
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2825 seq=822
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2834 seq=831
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2837 seq=834
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2867 seq=864
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2876 seq=873
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2888 seq=885
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2898 seq=895
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2901 seq=898
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2903 seq=900
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2908 seq=905
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2928 seq=925
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2943 seq=940
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=2946 seq=943
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3004 seq=1001
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3029 seq=1026
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3040 seq=1037
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3049 seq=1046
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3054 seq=1051
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3063 seq=1060
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3125 seq=1122
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3143 seq=1140
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3160 seq=1157
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3210 seq=1207
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3238 seq=1235
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3243 seq=1240
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3264 seq=1261
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3281 seq=1278
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3324 seq=1321
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3327 seq=1324
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3352 seq=1349
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3353 seq=1350
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3358 seq=1355
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3361 seq=1358
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3379 seq=1376
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3395 seq=1392
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3432 seq=1429
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3454 seq=1451
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3456 seq=1453
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3490 seq=1487
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3508 seq=1505
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3532 seq=1529
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3541 seq=1538
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3571 seq=1568
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3577 seq=1574
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3595 seq=1592
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3625 seq=1622
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3635 seq=1632
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3637 seq=1634
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3648 seq=1645
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3665 seq=1662
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3668 seq=1665
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3678 seq=1675
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3682 seq=1679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3694 seq=1691
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3696 seq=1693
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3715 seq=1712
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3738 seq=1735
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3742 seq=1739
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3743 seq=1740
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3760 seq=1757
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3823 seq=1820
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3824 seq=1821
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3833 seq=1830
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3845 seq=1842
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3846 seq=1843
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3850 seq=1847
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3895 seq=1892
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3896 seq=1893
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3907 seq=1904
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3908 seq=1905
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3937 seq=1934
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=3972 seq=1969
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4013 seq=2010
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4038 seq=2035
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4043 seq=2040
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4054 seq=2051
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4071 seq=2068
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4081 seq=2078
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4087 seq=2084
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4110 seq=2107
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4125 seq=2122
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4129 seq=2126
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4175 seq=2172
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4178 seq=2175
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4190 seq=2187
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4219 seq=2216
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4254 seq=2251
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4259 seq=2256
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4305 seq=2302
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4307 seq=2304
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4333 seq=2330
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4341 seq=2338
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4354 seq=2351
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4366 seq=2363
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4372 seq=2369
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4383 seq=2380
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4385 seq=2382
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4392 seq=2389
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4461 seq=2458
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4481 seq=2478
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4505 seq=2502
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4523 seq=2520
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4561 seq=2558
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4569 seq=2566
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4579 seq=2576
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4601 seq=2598
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4644 seq=2641
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4647 seq=2644
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4719 seq=2716
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4778 seq=2775
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4797 seq=2794
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4816 seq=2813
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4840 seq=2837
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4841 seq=2838
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4851 seq=2848
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4894 seq=2891
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4915 seq=2912
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4952 seq=2949
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4986 seq=2983
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4988 seq=2985
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=4990 seq=2987
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5007 seq=3004
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5008 seq=3005
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5018 seq=3015
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5049 seq=3046
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5054 seq=3051
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5059 seq=3056
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5080 seq=3077
 name=localhost
status=0 port=5097 seq=3094
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5221 seq=3218
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5264 seq=3261
 name=localhost
status=0 port=5267 seq=3264
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5276 seq=3273
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5286 seq=3283
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5293 seq=3290
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5315 seq=3312
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5354 seq=3351
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5377 seq=3374
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5409 seq=3406
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5410 seq=3407
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5413 seq=3410
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5419 seq=3416
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5436 seq=3433
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5466 seq=3463
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5489 seq=3486
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5493 seq=3490
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5495 seq=3492
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5520 seq=3517
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5547 seq=3544
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5551 seq=3548
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5563 seq=3560
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5585 seq=3582
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5588 seq=3585
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5602 seq=3599
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5614 seq=3611
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5649 seq=3646
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5660 seq=3657
 name=localhost
status=0 port=5665 seq=3662
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5676 seq=3673
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5708 seq=3705
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5715 seq=3712
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5739 seq=3736
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5792 seq=3789
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5799 seq=3796
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5809 seq=3806
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5813 seq=3810
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5827 seq=3824
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5830 seq=3827
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5857 seq=3854
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5859 seq=3856
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5865 seq=3862
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5868 seq=3865
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5884 seq=3881
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5891 seq=3888
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5914 seq=3911
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5919 seq=3916
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5925 seq=3922
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5938 seq=3935
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5942 seq=3939
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=5979 seq=3976
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6001 seq=3998
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6016 seq=4013
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6037 seq=4034
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6044 seq=4041
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6047 seq=4044
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6062 seq=4059
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6084 seq=4081
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6090 seq=4087
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6102 seq=4099
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6104 seq=4101
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6114 seq=4111
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6139 seq=4136
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6140 seq=4137
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6152 seq=4149
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6206 seq=4203
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6240 seq=4237
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6245 seq=4242
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6260 seq=4257
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6267 seq=4264
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6285 seq=4282
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6302 seq=4299
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6322 seq=4319
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6326 seq=4323
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6349 seq=4346
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6355 seq=4352
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6365 seq=4362
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6419 seq=4416
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6457 seq=4454
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6522 seq=4519
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6525 seq=4522
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6553 seq=4550
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6572 seq=4569
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6596 seq=4593
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6605 seq=4602
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6613 seq=4610
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6625 seq=4622
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6647 seq=4644
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6657 seq=4654
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6660 seq=4657
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6681 seq=4678
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6728 seq=4725
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6747 seq=4744
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6763 seq=4760
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6772 seq=4769
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6789 seq=4786
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6792 seq=4789
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6804 seq=4801
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6807 seq=4804
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6813 seq=4810
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6820 seq=4817
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6823 seq=4820
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6826 seq=4823
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6848 seq=4845
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6859 seq=4856
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6864 seq=4861
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6869 seq=4866
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6873 seq=4870
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6879 seq=4876
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6885 seq=4882
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6900 seq=4897
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6928 seq=4925
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6977 seq=4974
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=6991 seq=4988
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7022 seq=5019
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7023 seq=5020
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7045 seq=5042
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7053 seq=5050
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7081 seq=5078
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7090 seq=5087
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7099 seq=5096
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7101 seq=5098
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7135 seq=5132
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7150 seq=5147
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7159 seq=5156
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7165 seq=5162
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7201 seq=5198
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7207 seq=5204
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7219 seq=5216
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7257 seq=5254
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7267 seq=5264
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7273 seq=5270
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7280 seq=5277
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7317 seq=5314
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7319 seq=5316
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7333 seq=5330
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7362 seq=5359
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7445 seq=5442
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7455 seq=5452
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7460 seq=5457
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7469 seq=5466
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7527 seq=5524
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7610 seq=5607
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7637 seq=5634
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7650 seq=5647
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7677 seq=5674
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7679 seq=5676
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7693 seq=5690
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7695 seq=5692
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7721 seq=5718
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7729 seq=5726
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7733 seq=5730
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7744 seq=5741
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7759 seq=5756
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7762 seq=5759
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7815 seq=5812
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7823 seq=5820
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7827 seq=5824
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7831 seq=5828
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7844 seq=5841
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7881 seq=5878
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7903 seq=5900
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7919 seq=5916
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7938 seq=5935
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7964 seq=5961
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7969 seq=5966
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7970 seq=5967
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=7979 seq=5976
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8045 seq=6042
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8049 seq=6046
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8077 seq=6074
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8110 seq=6107
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8135 seq=6132
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8163 seq=6160
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8167 seq=6164
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8171 seq=6168
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8212 seq=6209
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8245 seq=6242
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8270 seq=6267
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8292 seq=6289
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8337 seq=6334
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8345 seq=6342
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8363 seq=6360
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8375 seq=6372
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8377 seq=6374
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8398 seq=6395
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8429 seq=6426
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8442 seq=6439
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8455 seq=6452
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8478 seq=6475
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8537 seq=6534
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8558 seq=6555
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8587 seq=6584
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8628 seq=6625
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8636 seq=6633
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8638 seq=6635
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8650 seq=6647
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8686 seq=6683
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8691 seq=6688
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8733 seq=6730
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8737 seq=6734
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8749 seq=6746
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8755 seq=6752
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8758 seq=6755
 name=localhost
status=0 port=8771 seq=6768
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8773 seq=6770
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8790 seq=6787
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8792 seq=6789
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8834 seq=6831
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8837 seq=6834
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8845 seq=6842
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8846 seq=6843
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8868 seq=6865
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8869 seq=6866
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8877 seq=6874
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8893 seq=6890
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8909 seq=6906
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8914 seq=6911
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8959 seq=6956
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8961 seq=6958
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=8995 seq=6992
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9018 seq=7015
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9029 seq=7026
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9060 seq=7057
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9079 seq=7076
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9080 seq=7077
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9100 seq=7097
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9121 seq=7118
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9137 seq=7134
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9146 seq=7143
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9195 seq=7192
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9212 seq=7209
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9218 seq=7215
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9221 seq=7218
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9280 seq=7277
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9291 seq=7288
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9303 seq=7300
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9328 seq=7325
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9354 seq=7351
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9369 seq=7366
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9387 seq=7384
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9391 seq=7388
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9410 seq=7407
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9415 seq=7412
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9425 seq=7422
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9443 seq=7440
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9453 seq=7450
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9456 seq=7453
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9477 seq=7474
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9493 seq=7490
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9501 seq=7498
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9585 seq=7582
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9632 seq=7629
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9633 seq=7630
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9671 seq=7668
 name=localhost
status=0 port=9683 seq=7680
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9685 seq=7682
 name=localhost
status=0 port=9686 seq=7683
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9702 seq=7699
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9726 seq=7723
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9744 seq=7741
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9759 seq=7756
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9773 seq=7770
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9796 seq=7793
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9807 seq=7804
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9813 seq=7810
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9825 seq=7822
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9849 seq=7846
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9885 seq=7882
ICMP Port Unreachable from ip=127.0.0.1 get hostname...status=0 port=9890 seq=7887
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9922 seq=7919
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9943 seq=7940
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9957 seq=7954
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9960 seq=7957
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9964 seq=7961
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9993 seq=7990
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=9994 seq=7991
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10018 seq=8015
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10038 seq=8035
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10043 seq=8040
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10044 seq=8041
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10049 seq=8046
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10050 seq=8047
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10097 seq=8094
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10118 seq=8115
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10119 seq=8116
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10137 seq=8134
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10196 seq=8193
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10199 seq=8196
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10223 seq=8220
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10225 seq=8222
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10226 seq=8223
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10227 seq=8224
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10234 seq=8231
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10291 seq=8288
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10293 seq=8290
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10349 seq=8346
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10374 seq=8371
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10381 seq=8378
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10396 seq=8393
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10406 seq=8403
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10472 seq=8469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10481 seq=8478
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10484 seq=8481
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10492 seq=8489
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10497 seq=8494
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10501 seq=8498
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10529 seq=8526
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10547 seq=8544
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10576 seq=8573
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10582 seq=8579
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10591 seq=8588
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10610 seq=8607
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10633 seq=8630
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10645 seq=8642
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10652 seq=8649
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10660 seq=8657
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10696 seq=8693
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10701 seq=8698
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10712 seq=8709
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10719 seq=8716
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10729 seq=8726
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10731 seq=8728
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10735 seq=8732
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10747 seq=8744
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10749 seq=8746
 name=localhost
status=0 port=10767 seq=8764
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10801 seq=8798
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10809 seq=8806
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10814 seq=8811
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10823 seq=8820
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10846 seq=8843
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10876 seq=8873
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10878 seq=8875
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10914 seq=8911
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10929 seq=8926
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10931 seq=8928
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=10962 seq=8959
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11000 seq=8997
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11002 seq=8999
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11009 seq=9006
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11017 seq=9014
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11019 seq=9016
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11101 seq=9098
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11204 seq=9201
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11212 seq=9209
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11215 seq=9212
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11237 seq=9234
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11245 seq=9242
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11284 seq=9281
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11307 seq=9304
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11356 seq=9353
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11374 seq=9371
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11400 seq=9397
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11412 seq=9409
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11425 seq=9422
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11443 seq=9440
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11469 seq=9466
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11472 seq=9469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11475 seq=9472
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11476 seq=9473
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11522 seq=9519
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11533 seq=9530
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11579 seq=9576
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11597 seq=9594
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11614 seq=9611
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11629 seq=9626
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11634 seq=9631
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11643 seq=9640
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11654 seq=9651
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11701 seq=9698
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11703 seq=9700
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11730 seq=9727
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11739 seq=9736
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11747 seq=9744
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11760 seq=9757
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11824 seq=9821
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11839 seq=9836
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11849 seq=9846
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11853 seq=9850
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=11885 seq=9882
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12019 seq=10016
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12022 seq=10019
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12023 seq=10020
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12039 seq=10036
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12087 seq=10084
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12102 seq=10099
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12113 seq=10110
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12118 seq=10115
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12120 seq=10117
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12127 seq=10124
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12139 seq=10136
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12148 seq=10145
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12157 seq=10154
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12197 seq=10194
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12220 seq=10217
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12248 seq=10245
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12255 seq=10252
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12260 seq=10257
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12264 seq=10261
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12277 seq=10274
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12341 seq=10338
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12353 seq=10350
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12368 seq=10365
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12414 seq=10411
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12419 seq=10416
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12422 seq=10419
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12448 seq=10445
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12499 seq=10496
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12504 seq=10501
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12505 seq=10502
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12525 seq=10522
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12562 seq=10559
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12603 seq=10600
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12640 seq=10637
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12669 seq=10666
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12679 seq=10676
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12688 seq=10685
 name=localhost
status=0 port=12692 seq=10689
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12698 seq=10695
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12722 seq=10719
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12724 seq=10721
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12772 seq=10769
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12775 seq=10772
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12777 seq=10774
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12792 seq=10789
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12796 seq=10793
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12820 seq=10817
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12822 seq=10819
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12854 seq=10851
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12882 seq=10879
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12909 seq=10906
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12921 seq=10918
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12970 seq=10967
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12980 seq=10977
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12986 seq=10983
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=12996 seq=10993
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13042 seq=11039
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13053 seq=11050
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13057 seq=11054
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13061 seq=11058
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13063 seq=11060
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13070 seq=11067
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13114 seq=11111
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13127 seq=11124
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13152 seq=11149
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13168 seq=11165
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13238 seq=11235
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13325 seq=11322
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13384 seq=11381
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13419 seq=11416
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13440 seq=11437
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13463 seq=11460
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13465 seq=11462
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13473 seq=11470
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13480 seq=11477
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13493 seq=11490
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13511 seq=11508
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13541 seq=11538
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13561 seq=11558
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13595 seq=11592
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13597 seq=11594
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13631 seq=11628
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13695 seq=11692
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13718 seq=11715
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13744 seq=11741
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13753 seq=11750
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13760 seq=11757
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13764 seq=11761
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13795 seq=11792
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13813 seq=11810
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13842 seq=11839
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13859 seq=11856
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13878 seq=11875
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13936 seq=11933
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13950 seq=11947
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13976 seq=11973
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13980 seq=11977
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13988 seq=11985
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13995 seq=11992
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=13998 seq=11995
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14022 seq=12019
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14043 seq=12040
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14050 seq=12047
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14074 seq=12071
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14075 seq=12072
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14089 seq=12086
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14097 seq=12094
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14109 seq=12106
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14134 seq=12131
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14199 seq=12196
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14209 seq=12206
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14210 seq=12207
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14234 seq=12231
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14263 seq=12260
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14279 seq=12276
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14298 seq=12295
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14302 seq=12299
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14319 seq=12316
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14334 seq=12331
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14338 seq=12335
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14362 seq=12359
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14368 seq=12365
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14380 seq=12377
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14390 seq=12387
 name=localhost
status=0 port=14408 seq=12405
 name=localhost
status=0 port=14445 seq=12442
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14511 seq=12508
 name=localhost
status=0 port=14514 seq=12511
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14549 seq=12546
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14572 seq=12569
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14578 seq=12575
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14610 seq=12607
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14621 seq=12618
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14623 seq=12620
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14632 seq=12629
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14634 seq=12631
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14645 seq=12642
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14654 seq=12651
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14656 seq=12653
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14658 seq=12655
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14671 seq=12668
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14682 seq=12679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14750 seq=12747
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14753 seq=12750
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14770 seq=12767
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14778 seq=12775
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14794 seq=12791
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14800 seq=12797
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14803 seq=12800
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14840 seq=12837
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14849 seq=12846
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14871 seq=12868
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14872 seq=12869
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14874 seq=12871
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14883 seq=12880
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14891 seq=12888
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14899 seq=12896
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14907 seq=12904
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14922 seq=12919
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14923 seq=12920
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14928 seq=12925
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14931 seq=12928
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14938 seq=12935
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14946 seq=12943
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14975 seq=12972
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=14978 seq=12975
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15016 seq=13013
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15031 seq=13028
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15045 seq=13042
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15085 seq=13082
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15142 seq=13139
 name=localhost
status=0 port=15156 seq=13153
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15174 seq=13171
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15180 seq=13177
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15213 seq=13210
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15247 seq=13244
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15262 seq=13259
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15270 seq=13267
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15287 seq=13284
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15294 seq=13291
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15314 seq=13311
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15325 seq=13322
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15351 seq=13348
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15358 seq=13355
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15360 seq=13357
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15361 seq=13358
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15377 seq=13374
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15403 seq=13400
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15407 seq=13404
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15422 seq=13419
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15471 seq=13468
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15490 seq=13487
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15515 seq=13512
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15529 seq=13526
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15539 seq=13536
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15566 seq=13563
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15571 seq=13568
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15583 seq=13580
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15615 seq=13612
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15635 seq=13632
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15655 seq=13652
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15668 seq=13665
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15676 seq=13673
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15694 seq=13691
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15728 seq=13725
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15754 seq=13751
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15764 seq=13761
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15774 seq=13771
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15775 seq=13772
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15792 seq=13789
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15807 seq=13804
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15810 seq=13807
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15823 seq=13820
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15827 seq=13824
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15832 seq=13829
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15850 seq=13847
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15860 seq=13857
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15886 seq=13883
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15895 seq=13892
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15928 seq=13925
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15960 seq=13957
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=15983 seq=13980
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16009 seq=14006
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16010 seq=14007
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16041 seq=14038
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16060 seq=14057
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16085 seq=14082
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16095 seq=14092
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16116 seq=14113
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16143 seq=14140
 name=localhost
status=0 port=16146 seq=14143
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16150 seq=14147
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16155 seq=14152
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16163 seq=14160
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16223 seq=14220
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16248 seq=14245
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16270 seq=14267
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16272 seq=14269
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16277 seq=14274
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16278 seq=14275
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16295 seq=14292
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16297 seq=14294
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16303 seq=14300
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16305 seq=14302
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16326 seq=14323
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16330 seq=14327
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16349 seq=14346
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16386 seq=14383
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16395 seq=14392
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16397 seq=14394
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16407 seq=14404
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16416 seq=14413
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16421 seq=14418
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16425 seq=14422
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16435 seq=14432
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16444 seq=14441
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16485 seq=14482
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16517 seq=14514
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16545 seq=14542
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16547 seq=14544
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16549 seq=14546
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16565 seq=14562
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16567 seq=14564
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16599 seq=14596
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16627 seq=14624
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16634 seq=14631
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16653 seq=14650
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16662 seq=14659
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16677 seq=14674
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16682 seq=14679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16708 seq=14705
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16711 seq=14708
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16743 seq=14740
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16744 seq=14741
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16778 seq=14775
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16790 seq=14787
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16811 seq=14808
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16814 seq=14811
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16827 seq=14824
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16840 seq=14837
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16864 seq=14861
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16871 seq=14868
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16943 seq=14940
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16952 seq=14949
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=16954 seq=14951
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17006 seq=15003
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17015 seq=15012
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17058 seq=15055
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17063 seq=15060
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17066 seq=15063
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17072 seq=15069
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17073 seq=15070
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17074 seq=15071
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17101 seq=15098
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17120 seq=15117
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17122 seq=15119
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17126 seq=15123
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17140 seq=15137
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17142 seq=15139
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17155 seq=15152
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17169 seq=15166
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17180 seq=15177
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17195 seq=15192
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17199 seq=15196
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17221 seq=15218
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17288 seq=15285
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17312 seq=15309
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17325 seq=15322
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17327 seq=15324
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17336 seq=15333
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17349 seq=15346
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17370 seq=15367
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17388 seq=15385
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17393 seq=15390
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17413 seq=15410
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17441 seq=15438
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17464 seq=15461
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17468 seq=15465
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17471 seq=15468
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17483 seq=15480
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17524 seq=15521
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17560 seq=15557
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17612 seq=15609
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17657 seq=15654
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17660 seq=15657
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17682 seq=15679
 name=localhost
status=0 port=17708 seq=15705
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17712 seq=15709
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17727 seq=15724
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17735 seq=15732
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17750 seq=15747
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17761 seq=15758
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17763 seq=15760
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17830 seq=15827
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17835 seq=15832
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17844 seq=15841
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17862 seq=15859
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17864 seq=15861
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17877 seq=15874
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17881 seq=15878
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17903 seq=15900
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17923 seq=15920
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17952 seq=15949
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17963 seq=15960
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17981 seq=15978
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=17994 seq=15991
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18014 seq=16011
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18037 seq=16034
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18051 seq=16048
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18057 seq=16054
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18061 seq=16058
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18077 seq=16074
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18106 seq=16103
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18119 seq=16116
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18158 seq=16155
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18169 seq=16166
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18171 seq=16168
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18209 seq=16206
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18212 seq=16209
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18222 seq=16219
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18254 seq=16251
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18257 seq=16254
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18273 seq=16270
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18276 seq=16273
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18294 seq=16291
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18366 seq=16363
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18380 seq=16377
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18390 seq=16387
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18395 seq=16392
 name=localhost
status=0 port=18527 seq=16524
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18542 seq=16539
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18552 seq=16549
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18560 seq=16557
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18566 seq=16563
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18592 seq=16589
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18601 seq=16598
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18620 seq=16617
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18634 seq=16631
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18650 seq=16647
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18717 seq=16714
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18726 seq=16723
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18732 seq=16729
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18736 seq=16733
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18741 seq=16738
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18744 seq=16741
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18881 seq=16878
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18900 seq=16897
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18929 seq=16926
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18952 seq=16949
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18957 seq=16954
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18958 seq=16955
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18962 seq=16959
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18971 seq=16968
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18981 seq=16978
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=18993 seq=16990
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19003 seq=17000
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19014 seq=17011
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19021 seq=17018
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19034 seq=17031
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19035 seq=17032
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19062 seq=17059
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19063 seq=17060
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19076 seq=17073
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19127 seq=17124
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19129 seq=17126
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19135 seq=17132
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19177 seq=17174
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19180 seq=17177
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19182 seq=17179
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19200 seq=17197
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19211 seq=17208
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19214 seq=17211
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19215 seq=17212
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19220 seq=17217
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19226 seq=17223
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19332 seq=17329
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19351 seq=17348
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19375 seq=17372
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19397 seq=17394
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19402 seq=17399
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19405 seq=17402
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19430 seq=17427
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19439 seq=17436
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19440 seq=17437
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19454 seq=17451
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19472 seq=17469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19486 seq=17483
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19499 seq=17496
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19523 seq=17520
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19527 seq=17524
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19529 seq=17526
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19532 seq=17529
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19555 seq=17552
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19561 seq=17558
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19569 seq=17566
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19632 seq=17629
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19656 seq=17653
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19682 seq=17679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19716 seq=17713
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19722 seq=17719
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19743 seq=17740
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19761 seq=17758
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19766 seq=17763
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19778 seq=17775
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19808 seq=17805
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19813 seq=17810
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19838 seq=17835
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19843 seq=17840
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19852 seq=17849
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19866 seq=17863
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19924 seq=17921
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19941 seq=17938
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=19993 seq=17990
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20012 seq=18009
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20032 seq=18029
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20037 seq=18034
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20044 seq=18041
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20060 seq=18057
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20063 seq=18060
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20075 seq=18072
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20090 seq=18087
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20103 seq=18100
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20105 seq=18102
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20128 seq=18125
 name=localhost
status=0 port=20211 seq=18208
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20233 seq=18230
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20234 seq=18231
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20242 seq=18239
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20245 seq=18242
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20251 seq=18248
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20282 seq=18279
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20301 seq=18298
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20369 seq=18366
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20370 seq=18367
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20403 seq=18400
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20424 seq=18421
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20432 seq=18429
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20453 seq=18450
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20470 seq=18467
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20477 seq=18474
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20508 seq=18505
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20511 seq=18508
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20539 seq=18536
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20548 seq=18545
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20573 seq=18570
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20583 seq=18580
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20595 seq=18592
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20600 seq=18597
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20688 seq=18685
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20692 seq=18689
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20702 seq=18699
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20707 seq=18704
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20728 seq=18725
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20780 seq=18777
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20803 seq=18800
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20815 seq=18812
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20838 seq=18835
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20856 seq=18853
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20868 seq=18865
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20886 seq=18883
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20938 seq=18935
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=20992 seq=18989
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21044 seq=19041
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21045 seq=19042
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21053 seq=19050
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21119 seq=19116
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21125 seq=19122
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21126 seq=19123
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21148 seq=19145
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21152 seq=19149
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21158 seq=19155
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21191 seq=19188
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21226 seq=19223
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21234 seq=19231
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21247 seq=19244
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21260 seq=19257
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21273 seq=19270
 name=localhost
status=0 port=21288 seq=19285
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21294 seq=19291
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21366 seq=19363
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21374 seq=19371
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21432 seq=19429
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21445 seq=19442
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21453 seq=19450
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21470 seq=19467
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21495 seq=19492
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21516 seq=19513
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21522 seq=19519
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21555 seq=19552
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21566 seq=19563
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21574 seq=19571
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21593 seq=19590
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21595 seq=19592
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21597 seq=19594
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21619 seq=19616
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21654 seq=19651
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21682 seq=19679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21686 seq=19683
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21693 seq=19690
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21706 seq=19703
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21712 seq=19709
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21807 seq=19804
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21850 seq=19847
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21884 seq=19881
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21888 seq=19885
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21896 seq=19893
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21907 seq=19904
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21917 seq=19914
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21935 seq=19932
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21939 seq=19936
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21942 seq=19939
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21973 seq=19970
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=21981 seq=19978
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22015 seq=20012
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22069 seq=20066
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22078 seq=20075
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22100 seq=20097
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22126 seq=20123
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22127 seq=20124
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22145 seq=20142
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22154 seq=20151
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22187 seq=20184
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22188 seq=20185
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22191 seq=20188
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22201 seq=20198
 name=localhost
status=0 port=22209 seq=20206
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22260 seq=20257
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22261 seq=20258
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22277 seq=20274
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22305 seq=20302
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22317 seq=20314
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22356 seq=20353
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22392 seq=20389
 name=localhost
status=0 port=22399 seq=20396
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22430 seq=20427
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22450 seq=20447
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22465 seq=20462
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22485 seq=20482
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22489 seq=20486
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22529 seq=20526
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22541 seq=20538
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22569 seq=20566
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22591 seq=20588
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22610 seq=20607
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22705 seq=20702
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22722 seq=20719
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22763 seq=20760
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22772 seq=20769
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22774 seq=20771
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22816 seq=20813
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22819 seq=20816
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22827 seq=20824
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22831 seq=20828
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22872 seq=20869
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22879 seq=20876
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22887 seq=20884
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22897 seq=20894
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22915 seq=20912
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22919 seq=20916
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22924 seq=20921
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22925 seq=20922
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22946 seq=20943
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22990 seq=20987
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22998 seq=20995
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=22999 seq=20996
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23015 seq=21012
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23035 seq=21032
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23064 seq=21061
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23072 seq=21069
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23083 seq=21080
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23098 seq=21095
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23106 seq=21103
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23115 seq=21112
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23126 seq=21123
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23129 seq=21126
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23191 seq=21188
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23202 seq=21199
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23216 seq=21213
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23221 seq=21218
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23233 seq=21230
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23253 seq=21250
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23273 seq=21270
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23303 seq=21300
 name=localhost
status=0 port=23307 seq=21304
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23309 seq=21306
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23311 seq=21308
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23322 seq=21319
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23325 seq=21322
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23354 seq=21351
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23357 seq=21354
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23366 seq=21363
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23373 seq=21370
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23380 seq=21377
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23398 seq=21395
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23407 seq=21404
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23425 seq=21422
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23463 seq=21460
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23472 seq=21469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23501 seq=21498
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23522 seq=21519
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23532 seq=21529
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23564 seq=21561
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23629 seq=21626
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23637 seq=21634
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23649 seq=21646
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23662 seq=21659
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23675 seq=21672
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23682 seq=21679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23742 seq=21739
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23765 seq=21762
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23779 seq=21776
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23790 seq=21787
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23791 seq=21788
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23801 seq=21798
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23819 seq=21816
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23842 seq=21839
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23894 seq=21891
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23896 seq=21893
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23898 seq=21895
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23940 seq=21937
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23960 seq=21957
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=23996 seq=21993
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24005 seq=22002
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24007 seq=22004
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24028 seq=22025
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24050 seq=22047
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24065 seq=22062
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24074 seq=22071
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24076 seq=22073
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24099 seq=22096
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24110 seq=22107
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24117 seq=22114
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24127 seq=22124
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24145 seq=22142
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24168 seq=22165
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24173 seq=22170
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24193 seq=22190
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24196 seq=22193
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24204 seq=22201
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24216 seq=22213
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24251 seq=22248
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24256 seq=22253
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24280 seq=22277
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24286 seq=22283
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24289 seq=22286
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24290 seq=22287
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24317 seq=22314
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24330 seq=22327
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24351 seq=22348
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24352 seq=22349
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24372 seq=22369
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24387 seq=22384
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24400 seq=22397
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24416 seq=22413
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24433 seq=22430
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24434 seq=22431
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24458 seq=22455
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24482 seq=22479
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24487 seq=22484
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24579 seq=22576
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24589 seq=22586
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24622 seq=22619
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24653 seq=22650
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24669 seq=22666
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24670 seq=22667
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24677 seq=22674
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24685 seq=22682
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24731 seq=22728
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24735 seq=22732
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24755 seq=22752
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24761 seq=22758
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24766 seq=22763
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24767 seq=22764
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24793 seq=22790
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24819 seq=22816
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24820 seq=22817
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24828 seq=22825
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24834 seq=22831
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24853 seq=22850
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24864 seq=22861
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24885 seq=22882
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24913 seq=22910
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24915 seq=22912
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24934 seq=22931
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24947 seq=22944
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24957 seq=22954
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=24969 seq=22966
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25024 seq=23021
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25044 seq=23041
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25049 seq=23046
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25084 seq=23081
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25090 seq=23087
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25124 seq=23121
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25128 seq=23125
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25147 seq=23144
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25150 seq=23147
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25171 seq=23168
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25206 seq=23203
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25221 seq=23218
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25254 seq=23251
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25266 seq=23263
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25280 seq=23277
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25284 seq=23281
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25288 seq=23285
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25292 seq=23289
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25302 seq=23299
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25309 seq=23306
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25316 seq=23313
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25319 seq=23316
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25321 seq=23318
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25383 seq=23380
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25385 seq=23382
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25454 seq=23451
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25468 seq=23465
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25469 seq=23466
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25471 seq=23468
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25485 seq=23482
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25493 seq=23490
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25497 seq=23494
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25521 seq=23518
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25537 seq=23534
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25563 seq=23560
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25571 seq=23568
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25578 seq=23575
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25591 seq=23588
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25638 seq=23635
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25648 seq=23645
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25663 seq=23660
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25691 seq=23688
 name=localhost
status=0 port=25694 seq=23691
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25724 seq=23721
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25733 seq=23730
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25752 seq=23749
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25764 seq=23761
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25801 seq=23798
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25815 seq=23812
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25827 seq=23824
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25849 seq=23846
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25857 seq=23854
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25858 seq=23855
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25869 seq=23866
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25878 seq=23875
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25892 seq=23889
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25918 seq=23915
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=25991 seq=23988
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26018 seq=24015
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26019 seq=24016
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26040 seq=24037
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26120 seq=24117
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26148 seq=24145
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26163 seq=24160
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26166 seq=24163
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26167 seq=24164
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26181 seq=24178
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26183 seq=24180
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26192 seq=24189
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26198 seq=24195
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26203 seq=24200
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26217 seq=24214
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26242 seq=24239
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26300 seq=24297
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26312 seq=24309
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26318 seq=24315
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26321 seq=24318
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26323 seq=24320
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26326 seq=24323
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26327 seq=24324
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26351 seq=24348
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26356 seq=24353
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26387 seq=24384
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26397 seq=24394
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26411 seq=24408
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26413 seq=24410
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26417 seq=24414
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26426 seq=24423
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26436 seq=24433
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26445 seq=24442
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26449 seq=24446
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26472 seq=24469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26478 seq=24475
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26487 seq=24484
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26507 seq=24504
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26514 seq=24511
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26520 seq=24517
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26538 seq=24535
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26541 seq=24538
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26577 seq=24574
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26581 seq=24578
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26585 seq=24582
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26595 seq=24592
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26640 seq=24637
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26641 seq=24638
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26642 seq=24639
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26644 seq=24641
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26652 seq=24649
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26653 seq=24650
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26657 seq=24654
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26665 seq=24662
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26666 seq=24663
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26675 seq=24672
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26686 seq=24683
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26687 seq=24684
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26704 seq=24701
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26709 seq=24706
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26714 seq=24711
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26756 seq=24753
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26805 seq=24802
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26809 seq=24806
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26816 seq=24813
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26830 seq=24827
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26831 seq=24828
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26851 seq=24848
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26863 seq=24860
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26869 seq=24866
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26925 seq=24922
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26933 seq=24930
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26970 seq=24967
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=26984 seq=24981
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27039 seq=25036
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27093 seq=25090
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27113 seq=25110
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27153 seq=25150
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27171 seq=25168
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27175 seq=25172
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27180 seq=25177
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27205 seq=25202
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27210 seq=25207
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27222 seq=25219
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27223 seq=25220
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27242 seq=25239
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27247 seq=25244
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27253 seq=25250
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27266 seq=25263
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27344 seq=25341
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27368 seq=25365
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27383 seq=25380
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27388 seq=25385
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27389 seq=25386
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27394 seq=25391
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27434 seq=25431
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27445 seq=25442
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27475 seq=25472
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27487 seq=25484
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27489 seq=25486
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27535 seq=25532
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27536 seq=25533
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27542 seq=25539
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27571 seq=25568
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27577 seq=25574
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27633 seq=25630
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27648 seq=25645
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27655 seq=25652
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27660 seq=25657
 name=localhost
status=0 port=27670 seq=25667
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27673 seq=25670
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27682 seq=25679
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27724 seq=25721
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27730 seq=25727
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27836 seq=25833
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27876 seq=25873
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27905 seq=25902
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27916 seq=25913
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27944 seq=25941
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27946 seq=25943
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=27951 seq=25948
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28015 seq=26012
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28059 seq=26056
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28070 seq=26067
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28099 seq=26096
 name=localhost
status=0 port=28101 seq=26098
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28118 seq=26115
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28119 seq=26116
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28169 seq=26166
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28256 seq=26253
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28296 seq=26293
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28327 seq=26324
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28329 seq=26326
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28364 seq=26361
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28365 seq=26362
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28372 seq=26369
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28382 seq=26379
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28402 seq=26399
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28403 seq=26400
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28419 seq=26416
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28432 seq=26429
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28447 seq=26444
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28461 seq=26458
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28469 seq=26466
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28472 seq=26469
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28475 seq=26472
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28483 seq=26480
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28507 seq=26504
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28514 seq=26511
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28516 seq=26513
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28519 seq=26516
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28533 seq=26530
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28566 seq=26563
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28582 seq=26579
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28598 seq=26595
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28662 seq=26659
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28677 seq=26674
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28681 seq=26678
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28686 seq=26683
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28689 seq=26686
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28693 seq=26690
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28705 seq=26702
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28760 seq=26757
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28778 seq=26775
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28784 seq=26781
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28789 seq=26786
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28790 seq=26787
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28796 seq=26793
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28812 seq=26809
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28813 seq=26810
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28894 seq=26891
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28897 seq=26894
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28909 seq=26906
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28910 seq=26907
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28961 seq=26958
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=28998 seq=26995
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29008 seq=27005
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29031 seq=27028
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29057 seq=27054
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29090 seq=27087
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29100 seq=27097
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29105 seq=27102
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29107 seq=27104
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29117 seq=27114
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29120 seq=27117
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29137 seq=27134
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29153 seq=27150
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29156 seq=27153
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29163 seq=27160
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29165 seq=27162
 name=localhost
status=0 port=29178 seq=27175
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29184 seq=27181
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29195 seq=27192
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29210 seq=27207
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29241 seq=27238
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29271 seq=27268
 name=localhost
status=0 port=29288 seq=27285
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29345 seq=27342
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29348 seq=27345
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29375 seq=27372
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29396 seq=27393
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29464 seq=27461
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29483 seq=27480
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29493 seq=27490
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29501 seq=27498
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29502 seq=27499
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29513 seq=27510
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29532 seq=27529
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29543 seq=27540
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29553 seq=27550
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29556 seq=27553
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29570 seq=27567
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29571 seq=27568
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29575 seq=27572
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29588 seq=27585
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29599 seq=27596
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29609 seq=27606
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29635 seq=27632
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29643 seq=27640
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29656 seq=27653
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29667 seq=27664
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29691 seq=27688
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29709 seq=27706
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29724 seq=27721
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29754 seq=27751
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29762 seq=27759
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29768 seq=27765
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29781 seq=27778
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29795 seq=27792
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29809 seq=27806
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29848 seq=27845
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29866 seq=27863
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29868 seq=27865
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29872 seq=27869
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29877 seq=27874
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29886 seq=27883
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29913 seq=27910
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29919 seq=27916
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29937 seq=27934
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29942 seq=27939
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29948 seq=27945
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=29999 seq=27996
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30044 seq=28041
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30058 seq=28055
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30061 seq=28058
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30076 seq=28073
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30097 seq=28094
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30113 seq=28110
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30125 seq=28122
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30155 seq=28152
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30183 seq=28180
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30195 seq=28192
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30197 seq=28194
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30220 seq=28217
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30230 seq=28227
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30235 seq=28232
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30285 seq=28282
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30305 seq=28302
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30314 seq=28311
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30320 seq=28317
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30322 seq=28319
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30333 seq=28330
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30339 seq=28336
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30345 seq=28342
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30349 seq=28346
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30363 seq=28360
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30368 seq=28365
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30415 seq=28412
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30422 seq=28419
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30432 seq=28429
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30462 seq=28459
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30469 seq=28466
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30483 seq=28480
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30522 seq=28519
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30532 seq=28529
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30570 seq=28567
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30601 seq=28598
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30628 seq=28625
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30686 seq=28683
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30690 seq=28687
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30710 seq=28707
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30719 seq=28716
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30730 seq=28727
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30747 seq=28744
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30755 seq=28752
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30804 seq=28801
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30841 seq=28838
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30859 seq=28856
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30871 seq=28868
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30877 seq=28874
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30886 seq=28883
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30916 seq=28913
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30930 seq=28927
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30952 seq=28949
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=30990 seq=28987
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31007 seq=29004
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31019 seq=29016
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31025 seq=29022
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31029 seq=29026
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31030 seq=29027
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31043 seq=29040
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31050 seq=29047
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31064 seq=29061
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31080 seq=29077
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31085 seq=29082
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31108 seq=29105
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31119 seq=29116
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31125 seq=29122
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31158 seq=29155
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31160 seq=29157
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31193 seq=29190
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31197 seq=29194
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31225 seq=29222
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31229 seq=29226
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31251 seq=29248
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31253 seq=29250
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31281 seq=29278
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31304 seq=29301
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31326 seq=29323
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31338 seq=29335
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31386 seq=29383
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31400 seq=29397
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31415 seq=29412
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31427 seq=29424
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31444 seq=29441
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31449 seq=29446
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31460 seq=29457
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31476 seq=29473
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31496 seq=29493
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31508 seq=29505
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31515 seq=29512
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31543 seq=29540
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31560 seq=29557
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31590 seq=29587
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31609 seq=29606
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31612 seq=29609
 name=localhost
status=0 port=31623 seq=29620
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31676 seq=29673
 name=localhost
status=0 port=31692 seq=29689
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31710 seq=29707
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31713 seq=29710
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31725 seq=29722
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31744 seq=29741
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31745 seq=29742
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31753 seq=29750
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31790 seq=29787
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31805 seq=29802
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31810 seq=29807
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31894 seq=29891
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31914 seq=29911
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31929 seq=29926
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31935 seq=29932
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31957 seq=29954
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31970 seq=29967
ICMP Port Unreachable from ip=127.0.0.1 name=localhost
status=0 port=31972 seq=29969

--- 127.0.0.1 hping statistic ---
30000 packets transmitted, 1688 packets received, 95% packet loss
round-trip min/avg/max = 0.1/1.9/1001.1 ms
31889 packets captured
63778 packets received by filter
0 packets dropped by kernel
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -lh data/*.pcap
-rw-r--r-- 1 tcpdump  tcpdump   11M Oct 28 14:41 data/attack_http.pcap
-rw-r--r-- 1 tcpdump  tcpdump  2.2M Oct 28 14:50 data/attack_syn.pcap
-rw-r--r-- 1 tcpdump  tcpdump  1.9M Oct 28 14:51 data/attack_udp.pcap
-rw-r--r-- 1 tcpdump  tcpdump  313K Oct 28 14:38 data/normal.pcap
-rw-r--r-- 1 raviteja raviteja 313K Oct 28 14:38 data/normal_backup.pcap
[2]+  Done                    sudo tcpdump -i lo -w data/attack_udp.pcap udp port 9999 or icmp
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cat > features.py << 'EOF'
import math
from collections import Counter
import pandas as pd
from scapy.all import PcapReader, IP, TCP, UDP, ICMP

WINDOW = 0.5  # seconds

FILES = [
    ("data/normal.pcap",      "normal", 0),
    ("data/attack_syn.pcap",  "syn",    1),
    ("data/attack_udp.pcap",  "udp",    1),
    ("data/attack_http.pcap", "http",   1),
]

def entropy(counter):
    total = sum(counter.values())
    if not total:
        return 0.0
    return -sum((c / total) * math.log2(c / total) for c in counter.values())

def new_bucket():
    return {"pkts": 0, "bytes": 0, "syn": 0, "ack": 0, "udp": 0,
            "icmp": 0, "src": Counter()}

def to_row(b, label, kind):
    return {
        "pps": b["pkts"] / WINDOW,
        "syn_ack_ratio": b["syn"] / max(b["ack"], 1),
        "unique_src": len(b["src"]),
        "src_entropy": entropy(b["src"]),
        "avg_size": b["bytes"] / max(b["pkts"], 1),
        "udp_ratio": b["udp"] / max(b["pkts"], 1),
        "icmp_ratio": b["icmp"] / max(b["pkts"], 1),
        "label": label,
        "attack_type": kind,
    }

def process(path, kind, label):
    rows, bucket, start = [], new_bucket(), None
    for pkt in PcapReader(path):
        if IP not in pkt:
EOFnt(df.groupby("attack_type").mean(numeric_only=True).round(2))
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 features.py
data/normal.pcap: 153 windows
data/attack_syn.pcap: 72 windows
data/attack_udp.pcap: 70 windows
data/attack_http.pcap: 42 windows
                 pps  syn_ack_ratio  unique_src  src_entropy  avg_size  udp_ratio  icmp_ratio  label
attack_type
http         3276.14           0.09        1.00         0.00    149.50       0.00        0.00    1.0
normal         25.88           0.09        1.00         0.00    145.58       0.00        0.00    0.0
syn           885.75          16.12      417.67         8.40     54.29       0.00        0.00    1.0
udp           911.11           0.00      429.57         8.54     43.65       0.94        0.06    1.0
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -lh data/dataset.csv
head -5 data/dataset.csv
-rw-r--r-- 1 raviteja raviteja 25K Oct 28 14:52 data/dataset.csv
pps,syn_ack_ratio,unique_src,src_entropy,avg_size,udp_ratio,icmp_ratio,label,attack_type
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cp ~/FloodGuard/data/dataset.csv "/mnt/c/Users/Ravi teja/Desktop/dataset.csv"
cp: cannot create regular file '/mnt/c/Users/Ravi teja/Desktop/dataset.csv': No such file or directory
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "/mnt/c/Users/"
'All Users'   Default  'Default User'   Public  'Ravi teja'   defaultuser0   desktop.ini
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "/mnt/c/Users/Ravi teja/Desktop"
ls: cannot access '/mnt/c/Users/Ravi teja/Desktop': No such file or directory
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "/mnt/c/Users/Ravi teja/"
 -1.14-windows.xml                                                                                   NetHood            images
 AndroidStudioProjects                                                                               OneDrive           index.html
 AppData                                                                                             Postman            index.js
'Application Data'                                                                                   PrintHood          mlflow.db
 Contacts                                                                                            Recent             mlflow_project
 Cookies                                                                                            'Saved Games'       mlruns
 Documents                                                                                           Searches           ntuser.dat.LOG1
 Downloads                                                                                           SendTo             ntuser.dat.LOG2
 Favorites                                                                                          'Start Menu'        ntuser.ini
 Links                                                                                               Templates          output
'Local Settings'                                                                                     Untitled.ipynb     package-lock.json
 Music                                                                                               Untitled1.ipynb    package.json
 Music_Recommendation_MLOps.ipynb.pdf                                                                Videos             ravi
'My Documents'                                                                                      'WPS Cloud Files'   ravi.txt
 NTUSER.DAT                                                                                          data               source
 NTUSER.DAT{0ecf456e-aa1c-11ef-86b8-9e5ae0d1150d}.TM.blf                                             exp-4.ipynb        text.txt
 NTUSER.DAT{0ecf456e-aa1c-11ef-86b8-9e5ae0d1150d}.TM.blf.cnpf                                        file.txt           venv
 NTUSER.DAT{0ecf456e-aa1c-11ef-86b8-9e5ae0d1150d}.TMContainer00000000000000000001.regtrans-ms        git-lab           '{'
 NTUSER.DAT{0ecf456e-aa1c-11ef-86b8-9e5ae0d1150d}.TMContainer00000000000000000001.regtrans-ms.cnpf   git-practice       {}package.txt
 NTUSER.DAT{0ecf456e-aa1c-11ef-86b8-9e5ae0d1150d}.TMContainer00000000000000000002.regtrans-ms        gitfolder
 NTUSER.DAT{0ecf456e-aa1c-11ef-86b8-9e5ae0d1150d}.TMContainer00000000000000000002.regtrans-ms.cnpf   handsongit
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "/mnt/c/Users/Ravi teja/OneDrive/Desktop"
ls: cannot access '/mnt/c/Users/Ravi teja/OneDrive/Desktop': No such file or directory
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "/mnt/c/Users/Ravi teja/OneDrive/"
'OneDrive - Shortcut.lnk'   desktop.ini  'one drive'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ powershell.exe -c '[Environment]::GetFolderPath("Desktop")'
C:\Users\Ravi teja\OneDrive\one drive\OneDrive\Documents\Desktop
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ wslpath "$(powershell.exe -c '[Environment]::GetFolderPath("Desktop")' | tr -d '\r')"
/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -d /mnt/c/Users/*/Desktop /mnt/c/Users/*/*/Desktop 2>/dev/null
'/mnt/c/Users/All Users/Application Data/Desktop'  '/mnt/c/Users/Default User/Desktop'   /mnt/c/Users/Public/Desktop
'/mnt/c/Users/All Users/Desktop'                    /mnt/c/Users/Default/Desktop
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop"
'Batch 136'   CapCut.lnk  'ETS Secure Browser.lnk'  'Iperius Remote.lnk'   Telegram.lnk   Wingspan.lnk   desktop.ini   exp  'html practice'   vehicle_maintanince
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ echo 'export WINDESK="/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop"' >> ~/.bashrc
source ~/.bashrc
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls "$WINDESK"
cp myfile.txt "$WINDESK"/
cd "$WINDESK"
'Batch 136'   CapCut.lnk  'ETS Secure Browser.lnk'  'Iperius Remote.lnk'   Telegram.lnk   Wingspan.lnk   desktop.ini   exp  'html practice'   vehicle_maintanince
cp: cannot stat 'myfile.txt': No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ln -s "/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop" ~/Desktop
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ls -l ~/Desktop
ls ~/Desktop
lrwxrwxrwx 1 raviteja raviteja 68 Oct 28 14:58 /home/raviteja/Desktop -> '/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop'
'Batch 136'   CapCut.lnk  'ETS Secure Browser.lnk'  'Iperius Remote.lnk'   Telegram.lnk   Wingspan.lnk   desktop.ini   exp  'html practice'   vehicle_maintanince
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp ~/FloodGuard/output/result.txt ~/Desktop/
cp: cannot stat '/home/raviteja/FloodGuard/output/result.txt': No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ls ~/FloodGuard/output
ls: cannot access '/home/raviteja/FloodGuard/output': No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp ~/FloodGuard/output/<actual-file-name> ~/Desktop/
-bash: actual-file-name: No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp -r ~/FloodGuard/output ~/Desktop/
cp: cannot stat '/home/raviteja/FloodGuard/output': No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ls ~/FloodGuard
alerts.py  attack_http.py  capture.py  data  detect.py  features.py  fusion.py  logs  respond.py  screenshots  traffic_normal.py  venv
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp -r "/mnt/c/Users/Ravi teja/output" ~/Desktop/
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ find ~/FloodGuard -type f \( -name "*.csv" -o -name "*.png" -o -name "*.txt" \) -not -path "*/venv/*" | head -20
/home/raviteja/FloodGuard/data/dataset.csv
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp ~/FloodGuard/your_file.csv ~/Desktop/
cp: cannot stat '/home/raviteja/FloodGuard/your_file.csv': No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp ~/FloodGuard/data/dataset.csv ~/Desktop/
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cp -r ~/FloodGuard/screenshots ~/Desktop/
cp -r ~/FloodGuard/logs ~/Desktop/
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ rsync -av --exclude 'venv' ~/FloodGuard/ ~/Desktop/FloodGuard/
sending incremental file list
created directory /home/raviteja/Desktop/FloodGuard
./
.gitignore
alerts.py
attack_http.py
capture.py
detect.py
features.py
fusion.py
respond.py
traffic_normal.py
.git/
.git/COMMIT_EDITMSG
.git/HEAD
.git/config
.git/description
.git/index
.git/branches/
.git/hooks/
.git/hooks/applypatch-msg.sample
.git/hooks/commit-msg.sample
.git/hooks/fsmonitor-watchman.sample
.git/hooks/post-update.sample
.git/hooks/pre-applypatch.sample
.git/hooks/pre-commit.sample
.git/hooks/pre-merge-commit.sample
.git/hooks/pre-push.sample
.git/hooks/pre-rebase.sample
.git/hooks/pre-receive.sample
.git/hooks/prepare-commit-msg.sample
.git/hooks/push-to-checkout.sample
.git/hooks/sendemail-validate.sample
.git/hooks/update.sample
.git/info/
.git/info/exclude
.git/logs/
.git/logs/HEAD
.git/logs/refs/
.git/logs/refs/heads/
.git/logs/refs/heads/main
.git/objects/
.git/objects/20/
.git/objects/20/db07947090c7b0251984eededab66bd62e4897
.git/objects/52/
.git/objects/52/0d4570170a155a0b939e38fddcedc4ab541742
.git/objects/63/
.git/objects/63/ab57c5f0ead123417c6bd5e928cec04b0528aa
.git/objects/b5/
.git/objects/b5/9ed59bfcab68d8bcf06e6bc206b7a823c4a0aa
.git/objects/c4/
.git/objects/c4/e791375468fae3c210dbfe28c9e113018bbaf1
.git/objects/e6/
.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391
.git/objects/info/
.git/objects/pack/
.git/refs/
.git/refs/heads/
.git/refs/heads/main
.git/refs/tags/
data/
data/attack_http.pcap
data/attack_syn.pcap
data/attack_udp.pcap
data/dataset.csv
data/normal.pcap
data/normal_backup.pcap
logs/
screenshots/

sent 16,242,284 bytes  received 1,011 bytes  10,828,863.33 bytes/sec
total size is 16,234,326  speedup is 1.00
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ls ~/Desktop
'Batch 136'  'ETS Secure Browser.lnk'  'Iperius Remote.lnk'   Wingspan.lnk   desktop.ini  'html practice'   output        vehicle_maintanince
 CapCut.lnk   FloodGuard                Telegram.lnk          dataset.csv    exp           logs             screenshots
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ^[[200~rm ~/Desktop/dataset.csv

rm: command not found
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ rm -r ~/Desktop/logs ~/Desktop/screenshots~
rm: cannot remove '/home/raviteja/Desktop/screenshots~': No such file or directory
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ls ~/Desktop
'Batch 136'  'ETS Secure Browser.lnk'  'Iperius Remote.lnk'   Wingspan.lnk   desktop.ini  'html practice'   screenshots
 CapCut.lnk   FloodGuard                Telegram.lnk          dataset.csv    exp           output           vehicle_maintanince
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ rm ~/Desktop/dataset.csv
rm -r ~/Desktop/screenshots
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ bind 'set enable-bracketed-paste off'
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ echo "bind 'set enable-bracketed-paste off'" >> ~/.bashrc
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ ls ~/Desktop/FloodGuard/data ~/Desktop/FloodGuard/logs
/home/raviteja/Desktop/FloodGuard/data:
attack_http.pcap  attack_syn.pcap  attack_udp.pcap  dataset.csv  normal.pcap  normal_backup.pcap

/home/raviteja/Desktop/FloodGuard/logs:
raviteja@BOOK-ENGGBTEIIG:/mnt/c/Users/Ravi teja/OneDrive/one drive/OneDrive/Documents/Desktop$ cd ~/FloodGuard
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ head -5 data/dataset.csv
pps,syn_ack_ratio,unique_src,src_entropy,avg_size,udp_ratio,icmp_ratio,label,attack_type
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
24.0,0.09090909090909091,1,-0.0,145.58333333333334,0.0,0.0,0,normal
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 detect.py
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 detect.py
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ source venv/bin/activate
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ source venv/bin/activate
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cut -d, -f8 data/dataset.csv | sort | uniq -c
    153 0
    184 1
      1 label
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ head -1 data/dataset.csv
pps,syn_ack_ratio,unique_src,src_entropy,avg_size,udp_ratio,icmp_ratio,label,attack_type
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ sed -n '200p' data/dataset.csv
912.0,16.53846153846154,431,8.564882486375994,54.228070175438596,0.0,0.0,1,syn
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ tail -20 detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ grep -n "__main__\|print" detect.py fusion.py respond.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ tail -20 detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ grep -ln "__main__" *.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -la *.py
-rw-r--r-- 1 raviteja raviteja    0 Oct 28 14:09 alerts.py
-rw-r--r-- 1 raviteja raviteja  460 Oct 28 14:40 attack_http.py
-rw-r--r-- 1 raviteja raviteja    0 Oct 28 14:09 capture.py
-rw-r--r-- 1 raviteja raviteja    0 Oct 28 14:09 detect.py
-rw-r--r-- 1 raviteja raviteja 2258 Oct 28 14:51 features.py
-rw-r--r-- 1 raviteja raviteja    0 Oct 28 14:09 fusion.py
-rw-r--r-- 1 raviteja raviteja    0 Oct 28 14:09 respond.py
-rw-r--r-- 1 raviteja raviteja  365 Oct 28 14:19 traffic_normal.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ wc -l *.py
   0 alerts.py
  18 attack_http.py
   0 capture.py
   0 detect.py
  75 features.py
   0 fusion.py
   0 respond.py
  15 traffic_normal.py
 108 total
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ find ~ /mnt/c/Users/"Ravi teja" -name "detect.py" -not -path "*/venv/*" 2>/dev/null
/home/raviteja/airflow/airflow_venv/lib/python3.12/site-packages/dill/detect.py
/home/raviteja/FloodGuard/detect.py
^C
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ wc -c *.py
   0 alerts.py
 460 attack_http.py
   0 capture.py
   0 detect.py
2258 features.py
   0 fusion.py
   0 respond.py
 365 traffic_normal.py
3083 total
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cat detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cat features.py
import math
from collections import Counter
import pandas as pd
from scapy.all import PcapReader, IP, TCP, UDP, ICMP

WINDOW = 0.5  # seconds

FILES = [
    ("data/normal.pcap",      "normal", 0),
    ("data/attack_syn.pcap",  "syn",    1),
    ("data/attack_udp.pcap",  "udp",    1),
    ("data/attack_http.pcap", "http",   1),
]

def entropy(counter):
    total = sum(counter.values())
    if not total:
        return 0.0
    return -sum((c / total) * math.log2(c / total) for c in counter.values())

def new_bucket():
    return {"pkts": 0, "bytes": 0, "syn": 0, "ack": 0, "udp": 0,
            "icmp": 0, "src": Counter()}

def to_row(b, label, kind):
    return {
        "pps": b["pkts"] / WINDOW,
        "syn_ack_ratio": b["syn"] / max(b["ack"], 1),
        "unique_src": len(b["src"]),
        "src_entropy": entropy(b["src"]),
        "avg_size": b["bytes"] / max(b["pkts"], 1),
        "udp_ratio": b["udp"] / max(b["pkts"], 1),
        "icmp_ratio": b["icmp"] / max(b["pkts"], 1),
        "label": label,
        "attack_type": kind,
    }

def process(path, kind, label):
    rows, bucket, start = [], new_bucket(), None
    for pkt in PcapReader(path):
        if IP not in pkt:
            continue
        t = float(pkt.time)
        if start is None:
            start = t
        while t - start >= WINDOW:
            if bucket["pkts"] > 0:
                rows.append(to_row(bucket, label, kind))
            bucket, start = new_bucket(), start + WINDOW
        bucket["pkts"] += 1
        bucket["bytes"] += len(pkt)
        bucket["src"][pkt[IP].src] += 1
        if TCP in pkt:
            f = int(pkt[TCP].flags)
            if f & 0x02 and not f & 0x10:
                bucket["syn"] += 1
            if f & 0x10:
                bucket["ack"] += 1
        elif UDP in pkt:
            bucket["udp"] += 1
        elif ICMP in pkt:
            bucket["icmp"] += 1
    if bucket["pkts"] > 0:
        rows.append(to_row(bucket, label, kind))
    return rows

all_rows = []
for path, kind, label in FILES:
    r = process(path, kind, label)
    print(f"{path}: {len(r)} windows")
    all_rows += r

df = pd.DataFrame(all_rows)
df.to_csv("data/dataset.csv", index=False)
print(df.groupby("attack_type").mean(numeric_only=True).round(2))
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cut -d, -f9 data/dataset.csv | sort | uniq -c
      1 attack_type
     42 http
    153 normal
     72 syn
     70 udp
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ head -40 features.py
import math
from collections import Counter
import pandas as pd
from scapy.all import PcapReader, IP, TCP, UDP, ICMP

WINDOW = 0.5  # seconds

FILES = [
    ("data/normal.pcap",      "normal", 0),
    ("data/attack_syn.pcap",  "syn",    1),
    ("data/attack_udp.pcap",  "udp",    1),
    ("data/attack_http.pcap", "http",   1),
]

def entropy(counter):
    total = sum(counter.values())
    if not total:
        return 0.0
    return -sum((c / total) * math.log2(c / total) for c in counter.values())

def new_bucket():
    return {"pkts": 0, "bytes": 0, "syn": 0, "ack": 0, "udp": 0,
            "icmp": 0, "src": Counter()}

def to_row(b, label, kind):
    return {
        "pps": b["pkts"] / WINDOW,
        "syn_ack_ratio": b["syn"] / max(b["ack"], 1),
        "unique_src": len(b["src"]),
        "src_entropy": entropy(b["src"]),
        "avg_size": b["bytes"] / max(b["pkts"], 1),
        "udp_ratio": b["udp"] / max(b["pkts"], 1),
        "icmp_ratio": b["icmp"] / max(b["pkts"], 1),
        "label": label,
        "attack_type": kind,
    }

def process(path, kind, label):
    rows, bucket, start = [], new_bucket(), None
    for pkt in PcapReader(path):
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ # detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ import sys
Command 'import' not found, but can be installed with:
sudo apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.42-1, or
sudo apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.6ubuntu1
sudo apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.6ubuntu1
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ import joblib
Command 'import' not found, but can be installed with:
sudo apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.42-1, or
sudo apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.6ubuntu1
sudo apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.6ubuntu1
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ import pandas as pd
Command 'import' not found, but can be installed with:
sudo apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.42-1, or
sudo apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.6ubuntu1
sudo apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.6ubuntu1
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ from sklearn.ensemble import RandomForestClassifier
Command 'from' not found, but can be installed with:
sudo apt install mailutils
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ from sklearn.model_selection import train_test_split
Command 'from' not found, but can be installed with:
sudo apt install mailutils
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ from sklearn.metrics import classification_report
Command 'from' not found, but can be installed with:
sudo apt install mailutils
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ FEATURES = ["pps", "syn_ack_ratio", "unique_src", "src_entropy",
FEATURES: command not found
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$             "avg_size", "udp_ratio", "icmp_ratio"]
avg_size,: command not found
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ MODEL_PATH = "model.pkl"
MODEL_PATH: command not found
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ def train(csv="data/dataset.csv"):
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     df = pd.read_csv(csv)
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     X, y = df[FEATURES], df["label"]
X,: command not found
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     X_tr, X_te, y_tr, y_te = train_test_split(
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$         X, y, test_size=0.25, random_state=42, stratify=y)
-bash: syntax error near unexpected token `)'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     model = RandomForestClassifier(n_estimators=100, random_state=42)
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     model.fit(X_tr, y_tr)
-bash: syntax error near unexpected token `X_tr,'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     print(classification_report(y_te, model.predict(X_te),
-bash: syntax error near unexpected token `classification_report'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$                                 target_names=["normal", "attack"]))
-bash: syntax error near unexpected token `)'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     joblib.dump(model, MODEL_PATH)
-bash: syntax error near unexpected token `model,'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     print(f"Model saved to {MODEL_PATH}")
-bash: syntax error near unexpected token `f"Model saved to {MODEL_PATH}"'
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     return model
-bash: return: model: numeric argument required
-bash: return: can only `return' from a function or sourced script
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ def load():
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     return joblib.load(MODEL_PATH)
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ def predict(model, row):
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     """row: dict with the 7 FEATURES. Returns (label, confidence)."""
row: dict with the 7 FEATURES. Returns (label, confidence).: command not found
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     X = pd.DataFrame([row])[FEATURES]
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     proba = model.predict_proba(X)[0]
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     label = int(proba.argmax())
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$     return label, float(proba[label])
-bash: syntax error near unexpected token `('
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ if __name__ == "__main__":
>     train()
> import pandas as pd^C
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ nano detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 detect.py
              precision    recall  f1-score   support

      normal       1.00      1.00      1.00        39
      attack       1.00      1.00      1.00        46

    accuracy                           1.00        85
   macro avg       1.00      1.00      1.00        85
weighted avg       1.00      1.00      1.00        85

Model saved to model.pkl
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ ls -la ~/FloodGuard/model.pkl
-rw-r--r-- 1 raviteja raviteja 84681 Oct 28 15:43 /home/raviteja/FloodGuard/model.pkl
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ wc -c ~/FloodGuard/detect.py
1210 /home/raviteja/FloodGuard/detect.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ nano alerts.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ nano respond.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ nano main.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ source venv/bin/activate
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 main.py
Traceback (most recent call last):
  File "/home/raviteja/FloodGuard/main.py", line 4, in <module>
    from respond import block
ImportError: cannot import name 'block' from 'respond' (/home/raviteja/FloodGuard/respond.py)
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ cd ~/FloodGuard
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ wc -c alerts.py respond.py main.py
269 alerts.py
  0 respond.py
437 main.py
706 total
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ nano respond.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ nano alerts.py
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ wc -c alerts.py respond.py
269 alerts.py
 98 respond.py
367 total
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$ python3 main.py
[NORMAL] pps=24 confidence=1.00
[ALERT]  attack detected | pps=930 unique_src=437 confidence=1.00
[RESPONSE] Blocking 437 source IPs (simulated)
(venv) raviteja@BOOK-ENGGBTEIIG:~/FloodGuard$