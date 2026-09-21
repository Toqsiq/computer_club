from sqlalchemy import select

from app.db import get_session
from app.models import Session, SessionStatus
from app.repositories.base import BaseRepository


class SessionRepository(BaseRepository[Session]):
    model = Session

    def get_active_sessions(self) -> list[Session]:
        with get_session() as session:
            stmt = (
                select(Session)
                .join(Session.status)
                .where(SessionStatus.name == "active")
            )
            return list(session.scalars(stmt).all())
