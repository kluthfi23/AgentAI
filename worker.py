import time

class Worker:

    def run(self, website, username):
        print(f"[Worker] Membuka {website}")

        time.sleep(1)

        print(f"[Worker] Login sebagai {username}")

        time.sleep(1)

        print("[Worker] Menjalankan tugas...")

        time.sleep(2)

        print("[Worker] Berhasil\n")

        return True
