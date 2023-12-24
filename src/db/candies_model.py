from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Candies(Base):
    """Конфеты.
    state: full, half, eaten"""

    __tablename__ = "candies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None] = mapped_column(String(200), nullable=True)
    state: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="full"
    )
    owner: Mapped[str] = mapped_column(
        String(100), nullable=False, server_default="teacher"
    )
