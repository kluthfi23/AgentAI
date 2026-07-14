class GenericPlugin:

    def open(self, page, url):

        if not url.startswith("http"):

            url = "https://" + url

        print(f"[PLUGIN] Open {url}")

        page.goto(
            url,
            timeout=60000
        )


    def search(self, page, keyword):

        print(
            f"[PLUGIN] Search {keyword}"
        )

        # Placeholder
        # Nanti kita cari textbox otomatis


    def screenshot(self, page):

        page.screenshot(
            path="screenshots/plugin.png"
        )


    def download(self, page):

        print(
            "[PLUGIN] Download"
        )