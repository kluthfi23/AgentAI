import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("agentai.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def create_admin(self):

        self.cursor.execute("""
        INSERT OR IGNORE INTO users
        (username, password)
        VALUES (?, ?)
        """, (
            "admin",
            "123456"
        ))

        self.conn.commit()

    def login(self, username, password):

        self.cursor.execute("""
        SELECT *
        FROM users
        WHERE username=? AND password=?
        """, (
            username,
            password
        ))

        return self.cursor.fetchone()

    def add_job(self, website, username):

        self.cursor.execute("""
        INSERT INTO jobs (website, username)
        VALUES (?, ?)
        """, (
            website,
            username
        ))

        self.conn.commit()

    def get_jobs(self):

        self.cursor.execute("""
        SELECT *
        FROM jobs
        ORDER BY id
        """)

        return self.cursor.fetchall()

    def update_status(self, job_id, status):

        self.cursor.execute("""
        UPDATE jobs
        SET status=?
        WHERE id=?
        """, (
            status,
            job_id
        ))

        self.conn.commit()

    def delete_job(self, job_id):

        self.cursor.execute("""
        DELETE FROM jobs
        WHERE id=?
        """, (
            job_id,
        ))

        self.conn.commit()

    def find_job(self, website):

        self.cursor.execute("""
        SELECT *
        FROM jobs
        WHERE website LIKE ?
        """, (
            "%" + website + "%",
        ))

        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
