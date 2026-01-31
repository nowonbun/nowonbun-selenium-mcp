import os
from typing import Optional

from mcp.server.fastmcp import FastMCP
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    from webdriver_manager.chrome import ChromeDriverManager
except Exception:  # pragma: no cover
    ChromeDriverManager = None

_host = os.environ.get("MCP_HOST", "127.0.0.1")
_port = int(os.environ.get("MCP_PORT", "8001"))
_path = os.environ.get("MCP_PATH", "/mcp")

mcp = FastMCP(
    "selenium-mcp",
    host=_host,
    port=_port,
    streamable_http_path=_path,
)
_driver: Optional[webdriver.Chrome] = None


def _build_driver() -> webdriver.Chrome:
    browser = os.environ.get("SELENIUM_BROWSER", "chrome").lower()

    if browser != "chrome":
        raise ValueError("Only chrome is supported in this sample. Set SELENIUM_BROWSER=chrome")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver_path = os.environ.get("CHROMEDRIVER_PATH")
    if driver_path:
        service = ChromeService(executable_path=driver_path)
        return webdriver.Chrome(service=service, options=options)

    if ChromeDriverManager is None:
        return webdriver.Chrome(options=options)

    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def _get_driver() -> webdriver.Chrome:
    global _driver
    if _driver is None:
        _driver = _build_driver()
    return _driver


def _find(css: Optional[str], xpath: Optional[str], timeout_sec: int):
    if not css and not xpath:
        raise ValueError("Either css or xpath is required")

    driver = _get_driver()
    wait = WebDriverWait(driver, timeout_sec)
    if css:
        return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
    return wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))


@mcp.tool()
def open_browser(start_url: str = "about:blank") -> str:
    driver = _get_driver()
    driver.get(start_url)
    return f"opened {start_url}"


@mcp.tool()
def navigate(url: str) -> str:
    driver = _get_driver()
    driver.get(url)
    return f"navigated {url}"


@mcp.tool()
def click(css: Optional[str] = None, xpath: Optional[str] = None, timeout_sec: int = 10) -> str:
    try:
        el = _find(css, xpath, timeout_sec)
        el.click()
        return "clicked"
    except TimeoutException as exc:
        return f"timeout: {exc}"


@mcp.tool()
def type_text(
    text: str,
    css: Optional[str] = None,
    xpath: Optional[str] = None,
    clear_first: bool = True,
    timeout_sec: int = 10,
) -> str:
    try:
        el = _find(css, xpath, timeout_sec)
        if clear_first:
            el.clear()
        el.send_keys(text)
        return "typed"
    except TimeoutException as exc:
        return f"timeout: {exc}"


@mcp.tool()
def get_text(css: Optional[str] = None, xpath: Optional[str] = None, timeout_sec: int = 10) -> str:
    try:
        el = _find(css, xpath, timeout_sec)
        return el.text
    except TimeoutException as exc:
        return f"timeout: {exc}"


@mcp.tool()
def get_page_source() -> str:
    driver = _get_driver()
    return driver.page_source


@mcp.tool()
def screenshot(path: str) -> str:
    driver = _get_driver()
    driver.save_screenshot(path)
    return f"saved {path}"


@mcp.tool()
def close_browser() -> str:
    global _driver
    if _driver is None:
        return "no browser"
    _driver.quit()
    _driver = None
    return "closed"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
