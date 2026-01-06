"""
하림님 챗봇 런처
- 터미널 창 없이 백그라운드 실행
- 시스템 트레이 아이콘
- 브라우저 자동 열기
"""
import subprocess
import webbrowser
import time
import sys
import os

# 현재 디렉토리로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 서버 시작 (창 숨김)
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

process = subprocess.Popen(
    [sys.executable, "app.py"],
    startupinfo=startupinfo,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# 서버 시작 대기
time.sleep(2)

# 브라우저 열기
webbrowser.open("http://localhost:8000")

# 프로세스 유지
try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
