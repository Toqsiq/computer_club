from typing import List
from psycopg2.extras import RealDictCursor
from app.repositories.base import BaseRepository
from app.db import get_connection


class SessionRepository(BaseRepository):
    table_name = "sessions"

    def get_active_sessions(self) -> List[dict]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT s.* 
                    FROM sessions s
                    JOIN session_statuses st ON s.status_id = st.id
                    WHERE st.name = 'active'
                """)
                return cur.fetchall()