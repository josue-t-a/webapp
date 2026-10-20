
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from webapp.database import Base


class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )
    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
