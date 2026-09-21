from sqlalchemy import select

from app.db import get_session
from app.models import Client
from app.repositories.base import BaseRepository


class ClientRepository(BaseRepository[Client]):
    model = Client

    def get_by_phone(self, phone: str) -> Client | None:
        with get_session() as session:
            return session.scalar(select(Client).where(Client.phone == phone))
