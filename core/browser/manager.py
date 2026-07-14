from playwright.sync_api import sync_playwright
import os


class BrowserManager:


    def __init__(self, headless=False):

        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None


    def start(self):

        self.playwright = sync_playwright().start()


        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )


        self.context = self.browser.new_context(
            storage_state="sessions/session.json"
            if os.path.exists("sessions/session.json")
            else None
        )


        return self.context



    def new_page(self):

        if not self.context:

            self.start()


        return self.context.new_page()



    def save_session(self):

        if self.context:

            self.context.storage_state(
                path="sessions/session.json"
            )



    def close(self):

        self.save_session()


        if self.browser:

            self.browser.close()


        if self.playwright:

            self.playwright.stop()