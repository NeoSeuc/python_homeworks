import sqlite3

from OOP_Homework.News import News


class DBManager:
    def __init__(self, db_path: str = "records.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table_if_not_exists(self, table_name: str):
        if table_name == "news":
            self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    text TEXT,
                    city TEXT,
                    publish_date TEXT
                )
            """)
            self.conn.commit()

    def record_exists(self, table_name: str, title: str, text: str) -> bool:
        self.cursor.execute(f"""
            SELECT 1 FROM {table_name}
            WHERE title = ? AND text = ?
        """, (title, text))
        return self.cursor.fetchone() is not None

    def insert_news(self, news: News):
        table_name = "news"
        self.create_table_if_not_exists(table_name)

        if self.record_exists(table_name, news.title, news.text):
            print(f"❗ Duplicate detected: \"{news.title}\". Skipping.")
            return

        self.cursor.execute(f"""
            INSERT INTO {table_name} (title, text, city, publish_date)
            VALUES (?, ?, ?, ?)
        """, (news.title, news.text, news.city, news.publish_date.isoformat()))
        self.conn.commit()
        print(f"✅ Inserted news: \"{news.title}\"")

    def close(self):
        self.conn.close()


def main():
    db = DBManager()

    # Створюємо новини (одна з них дублікат)
    news_items = [
        News("Storm in Paris", "Heavy rains flooded the city center.", "Paris"),
        News("Storm in Paris", "Heavy rains flooded the city center.", "Paris"),  # дубль
        News("Sunny in Rome", "Great day to visit the Colosseum.", "Rome"),
    ]

    for news in news_items:
        db.insert_news(news)

    db.close()


if __name__ == "__main__":
    main()
