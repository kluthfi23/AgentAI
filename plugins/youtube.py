class YouTubePlugin:

    def run(self, page, job):

        print("[PLUGIN] YouTube")

        page.goto(
            "https://www.youtube.com",
            timeout=60000
        )

        page.screenshot(
            path=f"screenshots/job_{job[0]}_youtube.png"
        )

        return True