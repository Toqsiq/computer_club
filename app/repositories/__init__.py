from app.repositories.base import BaseRepository
from app.repositories.tariff import TariffRepository
from app.repositories.service import ServiceRepository
from app.repositories.computer import ComputerRepository
from app.repositories.client import ClientRepository
from app.repositories.session import SessionRepository

__all__ = [
    "BaseRepository",
    "TariffRepository",
    "ServiceRepository",
    "ComputerRepository",
    "ClientRepository",
    "SessionRepository",
]