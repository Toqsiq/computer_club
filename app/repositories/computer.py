from sqlalchemy import select

from app.db import get_session
from app.models import Computer, ComputerStatus
from app.repositories.base import BaseRepository


class ComputerRepository(BaseRepository[Computer]):
    model = Computer

    def get_by_zone(self, zone_id: int) -> list[Computer]:
        with get_session() as session:
            return list(session.scalars(select(Computer).where(Computer.zone_id == zone_id)).all())

    def get_available(self) -> list[Computer]:
        with get_session() as session:
            stmt = (
                select(Computer)
                .join(Computer.status)
                .where(
                    ComputerStatus.name == "available",
                    Computer.is_active.is_(True),
                )
            )
            return list(session.scalars(stmt).all())
