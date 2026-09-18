from typing import List, Optional
from psycopg2.extras import RealDictCursor
from app.db import get_connection


class BaseRepository:
    table_name: str = ""

    def get_all(self) -> List[dict]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"SELECT * FROM {self.table_name}")
                return cur.fetchall()

    def get_by_id(self, id: int) -> Optional[dict]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    f"SELECT * FROM {self.table_name} WHERE id = %s",
                    (id,)
                )
                return cur.fetchone()

    def create(self, data: dict) -> dict:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        values = list(data.values())

        query = f"""
            INSERT INTO {self.table_name} ({columns})
            VALUES ({placeholders})
            RETURNING *
        """

        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, values)
                return cur.fetchone()

    def update(self, id: int, data: dict) -> Optional[dict]:
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        values = list(data.values()) + [id]

        query = f"""
            UPDATE {self.table_name}
            SET {set_clause}
            WHERE id = %s
            RETURNING *
        """

        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, values)
                return cur.fetchone()

    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"DELETE FROM {self.table_name} WHERE id = %s",
                    (id,)
                )
                return cur.rowcount > 0