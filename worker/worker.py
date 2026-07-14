from playwright.sync_api import sync_playwright


class Worker:

    def run(self, job):

        print(f"\n[AI] Memulai Job #{job[0]}")
        print(f"[AI] Website : {job[1]}")
        print(f"[AI] User    : {job[2]}")

        try:

            with sync_playwright() as p:

                browser = p.chromium.launch(
                    headless=False
                )

                page = browser.new_page()

                # Ambil URL
                url = job[1].strip()

                # Tambahkan https:// jika belum ada
                if not url.startswith("http"):

                    # Tambahkan .com jika belum ada domain
                    if "." not in url:
                        url += ".com"

                    url = "https://" + url

                print(f"[AI] Membuka website: {url}")

                page.goto(
                    url,
                    timeout=60000
                )

                print("[AI] Halaman berhasil dibuka.")

                page.screenshot(
                    path=f"screenshots/job_{job[0]}.png"
                )

                browser.close()

            print("[AI] Job selesai.\n")

            return True

        except Exception as e:

            print(f"[ERROR] {e}")

            return False