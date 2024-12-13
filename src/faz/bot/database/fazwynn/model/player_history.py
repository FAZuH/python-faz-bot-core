from __future__ import annotations

from datetime import datetime as dt
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from faz.bot.database.fazwynn.model._unique_id_model import UniqueIdModel

if TYPE_CHECKING:
    from faz.bot.database.fazwynn.model.player_info import PlayerInfo


class PlayerHistory(UniqueIdModel):
    __tablename__ = "player_history"

    uuid: Mapped[bytes] = mapped_column(
        BINARY(16),
        ForeignKey("player_info.uuid"),
        nullable=False,
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(VARCHAR(16), nullable=False)
    support_rank: Mapped[str] = mapped_column(VARCHAR(45), default=None)
    playtime: Mapped[float] = mapped_column(DECIMAL(8, 2, unsigned=True), nullable=False)
    guild_name: Mapped[str] = mapped_column(VARCHAR(30), default=None)
    guild_rank: Mapped[str] = mapped_column(
        ENUM("OWNER", "CHIEF", "STRATEGIST", "CAPTAIN", "RECRUITER", "RECRUIT"),
        default=None,
    )
    rank: Mapped[str] = mapped_column(VARCHAR(30), default=None)
    datetime: Mapped[dt] = mapped_column(DATETIME, nullable=False, primary_key=True)
    unique_id: Mapped[bytes] = mapped_column(BINARY(16), nullable=False)

    player_info: Mapped[PlayerInfo] = relationship(
        "PlayerInfo",
        back_populates="stat_history",
    )

    __table_args__ = (
        Index(None, datetime.desc()),
        Index(None, uuid),
        UniqueConstraint("unique_id"),
    )
