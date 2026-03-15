# AGENTS.md

## 목적
- 이 저장소는 Selenium을 MCP 도구로 노출하는 로컬 브라우저 자동화 서버 프로젝트다.
- 브라우저 조작의 재현 가능성과 기록 일관성을 유지하는 것이 핵심이다.

## 우선순위
1. 재현 가능성
2. 선택자 정확성
3. 기록 품질
4. 최소 변경

## 필수 규칙
- 시작 시 `rules.md`를 먼저 읽고 그 규칙을 따른다.
- 사이트별 지침 파일이 있으면 먼저 읽는다. 파일명 형식은 `{site}-{YYYYMMDD}.md`를 우선 찾는다.
- 새로 추가하는 md 파일은 항상 UTF-8로 저장한다.

## 작업 원칙
- 답변과 작업 보고는 항상 한국어로 한다.
- 결론을 먼저 말한다.
- 브라우저 자동화는 재현 가능한 절차 중심으로 설명한다.
- DOM을 추측하지 말고 화면과 선택자를 확인한 뒤 행동한다.
- 불필요한 전체 HTML 수집은 피한다.

## 프로젝트 성격
- `server.py`: Selenium MCP 서버
- `rules.md`: MCP 명령 목록 및 운영 규칙
- `system.md`, `system_jp.md`: 시스템 프롬프트/운영 문서
- `mail-*.md`, `naver-*.md`: 사이트/작업별 기록 예시

## 더 엄격한 도구 사용 규칙
- 기본 도구 집합: `open_browser`, `navigate`, `click`, `type_text`, `get_text`, `get_page_source`, `screenshot`, `close_browser`
- 사이트 탐색 전 최소 1회 스크린샷을 남긴다.
- `css`/`xpath` 중 하나는 항상 명확히 지정한다.
- HTML은 꼭 필요할 때만 `get_page_source()`로 가져온다.
- 선택자 근거가 없으면 클릭/입력을 강행하지 않는다.
- 작업 종료 시 가능하면 `close_browser()`까지 수행한다.

## 기록 규칙
- 웹 탐색 작업 후에는 재현 가능한 완전 기록 md를 남긴다.
- 각 단계는 `action + selector + 결과` 형식 한 줄로 기록한다.
- 성공/실패/timeout 여부를 명시한다.
- 절대경로, 사용자명, PC 종속 정보는 기록하지 않는다.
- 복잡한 탐색은 스크린샷 파일명과 함께 남긴다.

## 파일 수정 규칙
- MCP 도구 이름/파라미터를 바꾸면 아래를 함께 수정 여부 확인한다.
  - `README.md`
  - `rules.md`
  - `system.md`
  - `system_jp.md`
- Selenium/ChromeDriver 전제 조건이 바뀌면 설치 문서를 같이 갱신한다.
- 기존 AGENTS의 핵심 규칙은 삭제하지 말고 확장한다.

## 검증 규칙
- 최소 검증 절차:
  1. Python 문법 오류 확인
  2. 서버 기동 가능 여부 확인
  3. 도구 파라미터 호환성 확인
  4. 브라우저 종료 누락 여부 확인
- 실제 브라우저 실행 검증을 못 하면 반드시 그 사실을 적는다.

## 실행/테스트 명령어
```powershell
# 상태 확인
git status --short
Get-Content .\rules.md

# 의존성 설치
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 문법/기동 확인
python -m py_compile .\server.py
python .\server.py

# 환경 변수 예시
$env:MCP_HOST="127.0.0.1"
$env:MCP_PORT="8001"
$env:MCP_PATH="/mcp"
```

## 금지 사항
- 확인되지 않은 선택자를 확정적으로 적지 않는다.
- 필요 없는 전체 페이지 소스 수집을 반복하지 않는다.
- 사이트별 기록 없이 복잡한 자동화 절차를 남기지 않는다.
- 브라우저 상태 정리 없이 장시간 세션을 방치하지 않는다.

## 권장 응답 형식
- 결론
- 실행/수정 내용
- 검증 결과
- 남은 리스크
