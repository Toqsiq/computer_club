from __future__ import annotations

from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Boolean, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class ComputerStatus(Base):
    __tablename__ = "computer_statuses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    computers: Mapped[List["Computer"]] = relationship(back_populates="status")


class SessionStatus(Base):
    __tablename__ = "session_statuses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    sessions: Mapped[List["Session"]] = relationship(back_populates="status")


class Club(Base):
    __tablename__ = "clubs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String(500))
    phone: Mapped[Optional[str]] = mapped_column(String(50))

    zones: Mapped[List["ComputerZone"]] = relationship(
        back_populates="club", cascade="all, delete-orphan"
    )


class ComputerZone(Base):
    __tablename__ = "computer_zones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    club_id: Mapped[int] = mapped_column(ForeignKey("clubs.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    hourly_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    club: Mapped["Club"] = relationship(back_populates="zones")
    computers: Mapped[List["Computer"]] = relationship(back_populates="zone")


class Tariff(Base):
    __tablename__ = "tariffs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    sessions: Mapped[List["Session"]] = relationship(back_populates="tariff")


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class Computer(Base):
    __tablename__ = "computers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    zone_id: Mapped[int] = mapped_column(ForeignKey("computer_zones.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("computer_statuses.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    zone: Mapped["ComputerZone"] = relationship(back_populates="computers")
    status: Mapped["ComputerStatus"] = relationship(back_populates="computers")
    sessions: Mapped[List["Session"]] = relationship(back_populates="computer")


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    phone: Mapped[Optional[str]] = mapped_column(String(50), unique=True)

    sessions: Mapped[List["Session"]] = relationship(back_populates="client")


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    computer_id: Mapped[int] = mapped_column(ForeignKey("computers.id"), nullable=False)
    tariff_id: Mapped[int] = mapped_column(ForeignKey("tariffs.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("session_statuses.id"), nullable=False)

    client: Mapped["Client"] = relationship(back_populates="sessions")
    computer: Mapped["Computer"] = relationship(back_populates="sessions")
    tariff: Mapped["Tariff"] = relationship(back_populates="sessions")
    status: Mapped["SessionStatus"] = relationship(back_populates="sessions")
