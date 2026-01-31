# Selenium MCP (local)

Selenium을 로컬에서 실행하고 MCP tool로 제어하는 최소 예시입니다.

## 준비물
- Python 3.10+
- Chrome 또는 Chromium
- ChromeDriver (PATH에 추가)

## 설치
```
pip install -r requirements.txt
```

## 실행
```
python server.py
```
기본으로 `http://127.0.0.1:8001/mcp` 에서 HTTP MCP 서버가 뜹니다.
포트/경로 변경이 필요하면 환경변수를 사용하세요.
```
set MCP_HOST=127.0.0.1
set MCP_PORT=8001
set MCP_PATH=/mcp
```

## Codex MCP 설정 예시
```
[mcp_servers.selenium]
url = "http://127.0.0.1:8001/mcp"

[mcp_servers.selenium.env]
SELENIUM_BROWSER = "chrome"
```

## 제공되는 tools
- `open_browser(start_url)`
- `navigate(url)`
- `click(css=None, xpath=None, timeout_sec=10)`
- `type_text(text, css=None, xpath=None, clear_first=True, timeout_sec=10)`
- `get_text(css=None, xpath=None, timeout_sec=10)`
- `screenshot(path)`
- `close_browser()`

## 참고
- ChromeDriver 버전은 Chrome 버전과 맞아야 합니다.
- `webdriver-manager`를 사용하면 자동 다운로드가 가능하지만, 네트워크가 필요합니다.
