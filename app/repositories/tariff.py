from sqlalchemy import select

from app.models import Tariff
from app.db import get_session
from app.repositories.base import BaseRepository


class TariffRepository(BaseRepository[Tariff]):
    model = Tariff

    def get_active(self) -> list[Tariff]:
        with get_session() as session:
            return list(session.scalars(select(Tariff).where(Tariff.is_active.is_(True))).all())
