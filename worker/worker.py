from core.browser.manager import BrowserManager
from database.database import Database
from plugins.manager import PluginManager

class Worker:

    def __init__(self):

        self.browser = BrowserManager()


    def run(self, job):

        db = Database()

        db.update_status(
    job[0],
    "Running"
)

        print(f"\n[AI] Memulai Job #{job[0]}")
        print(f"[AI] Website : {job[1]}")
        print(f"[AI] User    : {job[2]}")

        try:

            browser = self.browser.start()

            page = self.browser.new_page()


            url = job[1].strip()


            if not url.startswith("http"):

                if "." not in url:
                    url += ".com"

                url = "https://" + url


            print(f"[AI] Membuka website: {url}")


            page.goto(
                url,
                timeout=60000
            )


            print("[AI] Website berhasil dibuka")


            page.screenshot(
                path=f"screenshots/job_{job[0]}.png"
            )


            print(
                f"[AI] Screenshot tersimpan: job_{job[0]}.png"
            )

            self.browser.save_session()

            page.close()

            db.update_status(
               job[0],
               "Selesai"
)

            return True


        except Exception as e:

            print(
                f"[ERROR] {e}"
            )

            return False


    def close(self):

        self.browser.close()