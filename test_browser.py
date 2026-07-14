from core.browser.manager import BrowserManager


browser = BrowserManager()

page = browser.new_page()

page.goto("https://www.google.com")

page.screenshot(
    path="screenshots/test.png"
)

browser.close()

print("Browser OK")