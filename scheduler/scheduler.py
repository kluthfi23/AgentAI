import time

from worker.worker import Worker


class Scheduler:


    def __init__(self, database):

        self.db = database
        self.worker = Worker()
        self.running = True



    def process_jobs(self):

        jobs = self.db.get_jobs()


        print("\n=== Scheduler ===")


        found = False


        for job in jobs:


            if job[4] != "Pending":
                continue


            found = True


            print(
                f"[SCHEDULER] Menjalankan Job #{job[0]} -> {job[1]}"
            )


            success = self.worker.run(job)


            if success:

                self.db.update_status(
                    job[0],
                    "Selesai"
                )

                print(
                    f"[SCHEDULER] Job #{job[0]} selesai"
                )


            else:

                self.db.update_status(
                    job[0],
                    "Gagal"
                )

                print(
                    f"[SCHEDULER] Job #{job[0]} gagal"
                )



        if not found:

            print(
                "[SCHEDULER] Tidak ada job Pending"
            )



    def start(self):

        print(
            "\nAgentAI Scheduler Aktif..."
        )


        while self.running:


            try:

                self.process_jobs()


                # cek setiap 5 detik
                time.sleep(5)


            except KeyboardInterrupt:

                print(
                    "\nScheduler dihentikan"
                )

                self.running = False



    def stop(self):

        self.running = False

        self.worker.close()