from typing import List
from psycopg2.extras import RealDictCursor
from app.repositories.base import BaseRepository
from app.db import get_connection


class TariffRepository(BaseRepository):
    table_name = "tariffs"

    def get_active(self) -> List[dict]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    f"SELECT * FROM {self.table_name} WHERE is_active = true"
                )
                return cur.fetchall()