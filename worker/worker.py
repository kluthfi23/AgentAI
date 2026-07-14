from core.browser.manager import BrowserManager
from core.task.engine import TaskEngine
from core.task.executor import TaskExecutor
from database.database import Database
from plugins.manager import PluginManager


class Worker:

    def __init__(self):

        self.browser = BrowserManager()
        self.task_engine = TaskEngine()
        self.task_executor = TaskExecutor()

    def normalize_url(self, url):

        url = url.strip().lower()

        if not url.startswith("http"):

            if "." not in url:
                url += ".com"

            url = "https://" + url

        return url

    def run(self, job):

        db = Database()

        page = None

        try:

            # ==========================
            # Update Status -> Running
            # ==========================

            db.update_status(
                job[0],
                "Running"
            )

            print("\n========================================")
            print(f"[AI] Menjalankan Job #{job[0]}")
            print("========================================")

            website = job[1]
            username = job[2]
            command = job[3]

            print(f"Website : {website}")
            print(f"Username: {username}")
            print(f"Command : {command}")

            url = self.normalize_url(website)

            # ==========================
            # Browser
            # ==========================

            self.browser.start()

            page = self.browser.new_page()

            # ==========================
            # Plugin
            # ==========================

            plugin = PluginManager().load(url)

            # ==========================
            # Task
            # ==========================

            tasks = self.task_engine.create_task(
                command
            )

            print("\nTask List")

            for task in tasks:

                print(task.to_dict())

            # ==========================
            # Execute Task
            # ==========================

            self.task_executor.execute(
                page,
                plugin,
                tasks
            )

            # ==========================
            # Save Session
            # ==========================

            self.browser.save_session()

            page.close()

            # ==========================
            # Update Status -> Selesai
            # ==========================

            db.update_status(
                job[0],
                "Selesai"
            )

            print("\n[AI] Job selesai")

            return True

        except Exception as e:

            print(f"\n[ERROR] {e}")

            # ==========================
            # Update Status -> Gagal
            # ==========================

            db.update_status(
                job[0],
                "Gagal"
            )

            return False

        finally:

            try:

                if page:
                    page.close()

            except:
                pass

            db.close()

    def close(self):

        self.browser.close()