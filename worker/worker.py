import time

class Worker:

    def run(self, job):

        print(f"[AI] Memulai Job #{job[0]}")
        print(f"[AI] Membuka {job[1]}")
        print("[AI] Analisa halaman...")
        print("[AI] Mengisi Form...")
        print("[AI] Submit...")

        time.sleep(2)

        print(f"[AI] Job #{job[0]} selesai")

        return True
