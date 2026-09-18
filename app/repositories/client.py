from typing import Optional
from psycopg2.extras import RealDictCursor
from app.repositories.base import BaseRepository
from app.db import get_connection


class ClientRepository(BaseRepository):
    table_name = "clients"

    def get_by_phone(self, phone: str) -> Optional[dict]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    f"SELECT * FROM {self.table_name} WHERE phone = %s",
                    (phone,)
                )
                return cur.fetchone()