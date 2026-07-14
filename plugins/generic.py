class GenericPlugin:

    def run(self, page, job):

        url = job[1].strip()

        if not url.startswith("http"):

            if "." not in url:
                url += ".com"

            url = "https://" + url

        print(f"[PLUGIN] Membuka {url}")

        page.goto(
            url,
            timeout=60000
        )

        page.screenshot(
            path=f"screenshots/job_{job[0]}.png"
        )

        return True