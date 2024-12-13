from datetime import datetime as dt

from sqlalchemy import Index
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from faz.bot.database.fazwynn.model._unique_id_model import UniqueIdModel


class GuildMemberHistory(UniqueIdModel):
    __tablename__ = "guild_member_history"

    uuid: Mapped[bytes] = mapped_column(BINARY(16), nullable=False, primary_key=True)
    contributed: Mapped[int] = mapped_column(BIGINT(unsigned=True), nullable=False)
    joined: Mapped[dt] = mapped_column(DATETIME, nullable=False, primary_key=True)
    datetime: Mapped[dt] = mapped_column(DATETIME, nullable=False)
    unique_id: Mapped[bytes] = mapped_column(BINARY(16), nullable=False)

    __table_args__ = (
        Index(None, datetime.desc()),
        Index(None, uuid),
        UniqueConstraint("unique_id"),
    )
