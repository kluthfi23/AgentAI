from playwright.sync_api import sync_playwright


class BrowserManager:

    def __init__(self, headless=False):

        self.headless = headless
        self.playwright = None
        self.browser = None


    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )

        return self.browser


    def new_page(self):

        if not self.browser:
            self.start()

        return self.browser.new_page()


    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()