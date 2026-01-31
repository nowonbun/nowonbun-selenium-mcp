# MCP Commands (Selenium)

이 프로젝트의 MCP 서버에서 사용할 수 있는 명령어(툴) 목록입니다.

## 사용 가능 명령어
- `open_browser(start_url)`
  - 브라우저를 열고 `start_url`로 이동합니다. 기본값: `about:blank`
- `navigate(url)`
  - 현재 브라우저에서 지정한 `url`로 이동합니다.
- `click(css=None, xpath=None, timeout_sec=10)`
  - 지정한 요소를 클릭합니다. `css` 또는 `xpath` 중 하나는 필수입니다.
- `type_text(text, css=None, xpath=None, clear_first=True, timeout_sec=10)`
  - 지정한 입력 요소에 텍스트를 입력합니다. `css` 또는 `xpath` 중 하나는 필수입니다.
- `get_text(css=None, xpath=None, timeout_sec=10)`
  - 지정한 요소의 텍스트를 가져옵니다. `css` 또는 `xpath` 중 하나는 필수입니다.
- `get_page_source()`
  - 현재 페이지의 HTML 소스를 반환합니다.
- `screenshot(path)`
  - 현재 화면을 `path`에 스크린샷으로 저장합니다.
- `close_browser()`
  - 브라우저를 종료합니다.

## 간단 예시
- `open_browser("https://www.example.com")`
- `click(css="#login")`
- `type_text("hello", css="input[name='q']")`
- `get_page_source()`

## 운영 규칙
- 새로 추가하는 md 파일은 항상 UTF-8로 저장한다.
- 특정 사이트를 호출할 때는 `{site}-{YYYYMMDD}.md`를 먼저 읽고 그 지침을 따른다.
- 사이트 탐색 전에는 스크린샷을 저장하고, 화면을 먼저 이해한 다음 일반 브라우저처럼 개발자 도구 흐름으로 DOM 탐색을 진행한다.
- 전체 HTML을 무조건 가져오지 말고, 필요할 때만 `get_page_source()`를 사용한다.
- 웹을 읽을 때는 스크린샷으로 자주 확인해 빠르게 탐색하고, 이미지 기반 UI(버튼 등)로 인해 HTML만으로 이해가 어려운 경우를 대비한다.
- 웹 탐색 작업 후에는 재현 가능한 "완전 기록" 형식의 md를 남긴다.
  - 각 단계는 `action + selector + 결과`를 한 줄로 기록한다.
  - selector는 css/xpath를 그대로 남기고, 성공/timeout 같은 결과를 명시한다.
  - 필요한 경우 반복 횟수(xN)와 범위([i..j])를 표기한다.
  - PC 종속 정보(절대 경로, 사용자명 등)는 기록하지 않는다.

