import psycopg2
from contextlib import contextmanager
from app.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


@contextmanager
def get_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        yield conn
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()