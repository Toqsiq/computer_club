from sqlalchemy import select

from app.db import get_session
from app.models import Service
from app.repositories.base import BaseRepository


class ServiceRepository(BaseRepository[Service]):
    model = Service

    def get_active(self) -> list[Service]:
        with get_session() as session:
            return list(session.scalars(select(Service).where(Service.is_active.is_(True))).all())
