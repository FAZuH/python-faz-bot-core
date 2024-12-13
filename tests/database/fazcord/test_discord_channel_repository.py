from typing import override

from faz.bot.database.fazcord.repository.discord_channel_repository import DiscordChannelRepository
from tests.database.fazcord._common_fazcord_repository_test import CommonFazcordRepositoryTest


class TestDiscordChannelRepository(CommonFazcordRepositoryTest.Test[DiscordChannelRepository]):
    @override
    async def _create_table(self) -> None:
        await self.database.discord_guild.create_table()
        await self.database.discord_user.create_table()
        await self.database.discord_channel.create_table()
        await self.database.track_entry.create_table()
        mock_data = self._get_discord_guild_mock_data()
        await self.database.discord_guild.insert([mock_data[0]])

    @override
    def _get_mock_data(self):
        return self._get_discord_channel_mock_data()

    @property
    @override
    def repo(self):
        return self.database.discord_channel
