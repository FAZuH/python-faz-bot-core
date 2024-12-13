from __future__ import annotations

from typing import Any, override

from faz.bot.wynn.api.base_ratelimit_handler import BaseRatelimitHandler
from faz.bot.wynn.api.model.headers import Headers


class WynnRatelimitHandler(BaseRatelimitHandler):
    def __init__(self, min_limit: int, total: int) -> None:
        self._min_limit = min_limit
        self._remaining = total
        self._total = total
        self._reset: float = 0.0

    @override
    def update(self, headers: dict[str, Any]) -> None:
        header = Headers(headers)
        self._total = header.ratelimit_limit
        self._remaining = header.ratelimit_remaining
        self._reset = header.ratelimit_reset

    @property
    @override
    def min_limit(self) -> int:
        return self._min_limit

    @property
    @override
    def remaining(self) -> int:
        return self._remaining

    @property
    @override
    def total(self) -> int:
        return self._total

    @property
    @override
    def reset(self) -> float:
        return self._reset
