from typing import List
from psycopg2.extras import RealDictCursor
from app.repositories.base import BaseRepository
from app.db import get_connection


class ComputerRepository(BaseRepository):
    table_name = "computers"

    def get_by_zone(self, zone_id: int) -> List[dict]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    f"SELECT * FROM {self.table_name} WHERE zone_id = %s",
                    (zone_id,)
                )
                return cur.fetchall()

    def get_available(self) -> List[dict]:
        """Компьютеры со статусом 'available'"""
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT c.* 
                    FROM computers c
                    JOIN computer_statuses s ON c.status_id = s.id
                    WHERE s.name = 'available' AND c.is_active = true
                """)
                return cur.fetchall()