import hashlib
from typing import Any

from faz.bot.database.fazwynn.model.base_fazwynn_model import BaseFazwynnModel


class UniqueIdModel(BaseFazwynnModel):
    __abstract__ = True

    def __init__(self, **kw: Any):
        super().__init__(**kw)
        self._compute_unique_id()

    def _compute_unique_id(self) -> None:
        columns = [
            str(getattr(self, col.name))
            for col in self.get_table().columns
            if col.name not in {"unique_id", "datetime"}
        ]
        to_hash = "".join(columns).encode()
        hashed_columns = hashlib.md5(to_hash).digest()
        self.unique_id = hashed_columns
