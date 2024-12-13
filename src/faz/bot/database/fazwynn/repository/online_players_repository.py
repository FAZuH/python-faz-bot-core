from __future__ import annotations

from typing import Any, TYPE_CHECKING

from faz.utils.database.base_repository import BaseRepository

from faz.bot.database.fazwynn.model.online_players import OnlinePlayers

if TYPE_CHECKING:
    from faz.utils.database.base_mysql_database import BaseMySQLDatabase
    from sqlalchemy.ext.asyncio import AsyncSession


class OnlinePlayersRepository(BaseRepository[OnlinePlayers, Any]):
    def __init__(self, database: BaseMySQLDatabase) -> None:
        super().__init__(database, OnlinePlayers)

    async def update(
        self, entities: list[OnlinePlayers], *, session: AsyncSession | None = None
    ) -> None:
        # TODO: confirm this works properly
        async with self.database.must_enter_async_session(session) as s:
            await self.truncate(session=s)
            await self.insert(entities, session=s)
