from app.repositories.base import BaseRepository
from app.repositories.client import ClientRepository
from app.repositories.computer import ComputerRepository
from app.repositories.service import ServiceRepository
from app.repositories.session import SessionRepository
from app.repositories.tariff import TariffRepository

__all__ = [
    "BaseRepository",
    "TariffRepository",
    "ServiceRepository",
    "ComputerRepository",
    "ClientRepository",
    "SessionRepository",
]
