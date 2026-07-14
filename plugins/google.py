class GooglePlugin:

    def run(self, page, job):

        print("[PLUGIN] Google")

        page.goto(
            "https://www.google.com",
            timeout=60000
        )

        page.screenshot(
            path=f"screenshots/job_{job[0]}_google.png"
        )

        return True