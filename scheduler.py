from worker.worker import Worker


class Scheduler:

    def __init__(self, database):
        self.db = database
        self.worker = Worker()

    def process_jobs(self):

        jobs = self.db.get_jobs()

        print("\n=== Scheduler ===")

        for job in jobs:

            if job[3] == "Selesai":
                continue

            print(f"Memproses Job #{job[0]} -> {job[1]}")

            self.db.update_status(job[0], "Running")

            sukses = self.worker.run(job)

            if sukses:
                self.db.update_status(job[0], "Selesai")
            else:
                self.db.update_status(job[0], "Gagal")


