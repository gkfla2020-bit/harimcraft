<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Claude_Opus_4-191919?style=for-the-badge&logo=anthropic&logoColor=white"/>
</p>

<h1 align="center">⛏️ HarimCraft</h1>

<p align="center">
  <b>Claude Opus 4 기반 개인 AI 코딩 어시스턴트</b><br>
  퀀트 연구 · 논문 리뷰 · Python 코딩에 특화된 웹 챗봇
</p>

<p align="center">
  <img src="https://img.shields.io/badge/마인크래프트_테마-5b8731?style=flat-square"/>
  <img src="https://img.shields.io/badge/다중_파일_지원-4aedd9?style=flat-square"/>
  <img src="https://img.shields.io/badge/웹_검색-fcdb05?style=flat-square"/>
  <img src="https://img.shields.io/badge/수식_렌더링-ff6b6b?style=flat-square"/>
</p>

---

## ✨ 주요 기능

### 💬 AI 채팅
- **Claude Opus 4** - Anthropic 최고 성능 모델 사용
- **프롬프트 캐싱** - 반복 대화 시 비용 90% 절감
- **다중 채팅방** - 주제별 대화 관리, 자동 저장

### 📎 다양한 파일 분석
| 문서 | 코드 |
|------|------|
| PDF, Word (.docx) | Python, JavaScript |
| Excel (.xlsx), CSV | Java, SQL, JSON |
| PowerPoint (.pptx) | HTML, CSS, YAML |

### 🔍 실시간 웹 검색
- DuckDuckGo + Wikipedia 통합 검색
- "최신", "현재", "검색해줘" 등 자연어 트리거
- 검색 결과 기반 답변 생성

### 🎨 마인크래프트 테마 UI
- 픽셀 폰트 & 3D 버튼 효과
- 다크/라이트 테마 전환
- 반응형 디자인 (모바일 지원)

### 📐 수학 수식 지원
```
인라인: $E = mc^2$
블록: $$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$
```
KaTeX로 LaTeX 수식 완벽 렌더링

### 💻 코드 하이라이팅
- Syntax highlighting (Python, JS, SQL 등)
- 원클릭 복사 버튼
- 언어별 아이콘 표시

---

## 🚀 설치 및 실행

### 1. 클론
```bash
git clone https://github.com/yourusername/harimcraft.git
cd harimcraft
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. API 키 설정
```bash
# .env 파일 생성
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

### 4. 실행
```bash
python app.py
```
브라우저에서 `http://localhost:8000` 접속

---

## 📁 프로젝트 구조

```
harimcraft/
├── app.py              # 메인 서버 (FastAPI)
├── requirements.txt    # 의존성 목록
├── .env               # API 키 (gitignore)
├── start.bat          # Windows 실행 스크립트
├── start.pyw          # 백그라운드 실행
└── data/
    ├── chats.json     # 채팅 히스토리
    └── settings.json  # 사용자 설정
```

---

## 🛠️ 기술 스택

| 분류 | 기술 |
|------|------|
| **Backend** | Python, FastAPI, Uvicorn |
| **AI** | Claude Opus 4 (Anthropic API) |
| **Frontend** | Vanilla JS, HTML5, CSS3 |
| **문서 파싱** | PyPDF2, python-docx, openpyxl, python-pptx |
| **수식** | KaTeX |
| **코드** | Highlight.js |
| **검색** | DuckDuckGo API, Wikipedia API |

---

## 💡 사용 예시

### 퀀트 연구
> "샤프 비율 계산하는 Python 코드 짜줘"

### 논문 리뷰
> 📎 논문.pdf 첨부 → "이 논문의 핵심 contribution이 뭐야?"

### 웹 검색
> "비트코인 현재 가격 검색해줘"

### 수학 질문
> "블랙숄즈 공식 설명해줘"

---

## ⚙️ 설정

| 항목 | 기본값 | 설명 |
|------|--------|------|
| 모델 | claude-opus-4 | Anthropic 최신 모델 |
| max_tokens | 6,000 | 응답당 최대 토큰 |
| 테마 | Dark | 다크/라이트 선택 가능 |
| 글자 크기 | Medium | 작게/보통/크게 |

---

## 📄 라이선스

MIT License

---

<p align="center">
  Made with ⛏️ by <b>Harim</b>
</p>
