import sqlite3


class Migrator:


    def __init__(self, db_name="agentai.db"):

        self.conn = sqlite3.connect(db_name)

        self.cursor = self.conn.cursor()



    def column_exists(self, table, column):

        self.cursor.execute(
            f"PRAGMA table_info({table})"
        )

        columns = [
            row[1]
            for row in self.cursor.fetchall()
        ]

        return column in columns



    def add_column(
        self,
        table,
        column,
        column_type
    ):

        if not self.column_exists(
            table,
            column
        ):

            self.cursor.execute(
                f"""
                ALTER TABLE {table}
                ADD COLUMN {column}
                {column_type}
                """
            )

            print(
                f"[MIGRATION] Added {column}"
            )



    def run(self):

        print(
            "[MIGRATION] Checking database..."
        )


        # Tambah command ke jobs

        self.add_column(
            "jobs",
            "command",
            "TEXT"
        )


        # Tambah hasil eksekusi

        self.add_column(
            "jobs",
            "result",
            "TEXT"
        )


        # Tambah waktu mulai

        self.add_column(
            "jobs",
            "started_at",
            "TIMESTAMP"
        )


        # Tambah waktu selesai

        self.add_column(
            "jobs",
            "finished_at",
            "TIMESTAMP"
        )


        self.conn.commit()


        print(
            "[MIGRATION] Done"
        )



    def close(self):

        self.conn.close()