import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()  # загружает данные из файла .env

@contextmanager
def get_connection():
    """Удобное и безопасное подключение к базе"""
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "computer_club_new"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD")
        )
        yield conn
        conn.commit()
    except Error as e:
        if conn:
            conn.rollback()
        print("Ошибка базы данных:", e)
        raise
    finally:
        if conn:
            conn.close()


# ===== Пример использования =====
if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM tariffs;")
            rows = cur.fetchall()
            
            print(f"Найдено записей: {len(rows)}")
            for row in rows:
                print(dict(row))