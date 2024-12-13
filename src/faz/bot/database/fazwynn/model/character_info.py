from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from faz.bot.database.fazwynn.model.base_fazwynn_model import BaseFazwynnModel

if TYPE_CHECKING:
    from faz.bot.database.fazwynn.model.character_history import CharacterHistory
    from faz.bot.database.fazwynn.model.player_info import PlayerInfo


class CharacterInfo(BaseFazwynnModel):
    """
    Assumptions:
        - character_uuid, uuid and type never changes
    """

    __tablename__ = "character_info"

    character_uuid: Mapped[bytes] = mapped_column(BINARY(16), nullable=False, primary_key=True)
    uuid: Mapped[bytes] = mapped_column(BINARY(16), ForeignKey("player_info.uuid"), nullable=False)
    type: Mapped[str] = mapped_column(
        ENUM("ARCHER", "ASSASSIN", "MAGE", "SHAMAN", "WARRIOR"), nullable=False
    )

    player: Mapped[PlayerInfo] = relationship(
        "PlayerInfo",
        back_populates="characters",
        lazy="selectin",
    )

    latest_stat: Mapped[CharacterHistory] = relationship(
        "CharacterHistory",
        primaryjoin="and_(CharacterHistory.character_uuid == CharacterInfo.character_uuid, "
        "CharacterHistory.datetime == (select(func.max(CharacterHistory.datetime))"
        ".where(CharacterHistory.character_uuid == CharacterInfo.character_uuid)"
        ".scalar_subquery()))",
        viewonly=True,
        uselist=False,
    )
    stat_history: Mapped[list[CharacterHistory]] = relationship(
        "CharacterHistory",
        back_populates="character_info",
        order_by="CharacterHistory.datetime.desc()",
        lazy="selectin",
    )
