"""1.0.0 Initial faz-cord version

Revision ID: 305fa6683a43
Revises:
Create Date: 2024-10-26 23:44:12.333059

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "305fa6683a43"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "discord_guild",
        sa.Column(
            "guild_id",
            mysql.BIGINT(display_width=20),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("guild_name", mysql.VARCHAR(length=36), nullable=False),
        sa.PrimaryKeyConstraint("guild_id"),
        mysql_collate="utf8mb4_uca1400_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "discord_user",
        sa.Column(
            "user_id",
            mysql.BIGINT(display_width=20),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("username", mysql.VARCHAR(length=36), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
        mysql_collate="utf8mb4_uca1400_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "whitelist_group",
        sa.Column("id", mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
        sa.Column("type", mysql.VARCHAR(length=32), nullable=False),
        sa.Column("reason", mysql.VARCHAR(length=255), nullable=True),
        sa.Column("from", mysql.DATETIME(), nullable=False),
        sa.Column("until", mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint("id", "type"),
        mysql_collate="utf8mb4_uca1400_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "discord_channel",
        sa.Column(
            "channel_id",
            mysql.BIGINT(display_width=20),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("channel_name", mysql.VARCHAR(length=36), nullable=False),
        sa.Column(
            "guild_id",
            mysql.BIGINT(display_width=20),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["guild_id"], ["discord_guild.guild_id"], name="discord_channel_ibfk_1"
        ),
        sa.PrimaryKeyConstraint("channel_id"),
        mysql_collate="utf8mb4_uca1400_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "track_entry",
        sa.Column("id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
        sa.Column(
            "channel_id",
            mysql.BIGINT(display_width=20),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "created_by",
            mysql.BIGINT(display_width=20),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "created_on",
            mysql.DATETIME(),
            server_default=sa.text("current_timestamp()"),
            nullable=False,
        ),
        sa.Column(
            "type",
            mysql.ENUM("GUILD", "HUNTED", "ONLINE", "PLAYER", "STAFF"),
            nullable=False,
        ),
        sa.Column(
            "enabled",
            mysql.TINYINT(display_width=1),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["channel_id"], ["discord_channel.channel_id"], name="track_entry_ibfk_1"
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["discord_user.user_id"],
            name="track_entry_ibfk_2",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_uca1400_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "track_entry_associations",
        sa.Column("id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
        sa.Column(
            "track_entry_id",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("associated_value", sa.BINARY(length=16), nullable=False),
        sa.ForeignKeyConstraint(
            ["track_entry_id"],
            ["track_entry.id"],
            name="track_entry_associations_ibfk_1",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_uca1400_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_index("channel_id", "track_entry", ["channel_id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("track_entry_associations")
    op.drop_table("track_entry")
    op.drop_table("discord_channel")
    op.drop_table("whitelist_group")
    op.drop_table("discord_user")
    op.drop_table("discord_guild")
    # ### end Alembic commands ###
