from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session

ModelT = TypeVar("ModelT")


class BaseRepository(Generic[ModelT]):
    model: Type[ModelT]

    def get_all(self) -> List[ModelT]:
        with get_session() as session:
            return list(session.scalars(select(self.model)).all())

    def get_by_id(self, id: int) -> Optional[ModelT]:
        with get_session() as session:
            return session.get(self.model, id)

    def create(self, data: dict) -> ModelT:
        with get_session() as session:
            obj = self.model(**data)
            session.add(obj)
            session.flush()
            session.refresh(obj)
            return obj

    def update(self, id: int, data: dict) -> Optional[ModelT]:
        with get_session() as session:
            obj = session.get(self.model, id)
            if obj is None:
                return None
            for key, value in data.items():
                setattr(obj, key, value)
            session.flush()
            session.refresh(obj)
            return obj

    def delete(self, id: int) -> bool:
        with get_session() as session:
            obj = session.get(self.model, id)
            if obj is None:
                return False
            session.delete(obj)
            return True
