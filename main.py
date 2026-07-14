from app.engine import AgentAI
from app.logger import log

from database.database import Database
from scheduler.scheduler import Scheduler

import time
from database.migration.migrator import Migrator

def main():
    bot = AgentAI()

    log("Memulai AgentAI")
    bot.start()

    db = Database()
    db.create_tables()
    db.create_admin()

    migration = Migrator()
    
    migration.run()

    migration.close()



    scheduler = Scheduler(db)

    scheduler.start()


    print("\nAgentAI Scheduler Berjalan...")

    try:
        while True:
            scheduler.process_jobs()
            time.sleep(10)  # cek job baru setiap 10 detik

    except KeyboardInterrupt:
        print("\nScheduler dihentikan")

    finally:
        db.close()


if __name__ == "__main__":
    main()
