from app.engine import AgentAI
from app.logger import log
from database.database import Database

bot = AgentAI()

log("Memulai AgentAI")

bot.start()

db = Database()

db.create_tables()

db.add_job(
    "https://contoh-website.com",
    "admin"
)

print("\nDaftar Job")

db.show_jobs()

db.close()
