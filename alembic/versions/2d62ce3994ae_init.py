"""init

Revision ID: 2d62ce3994ae
Revises: 0001_init_project_table
Create Date: 2026-04-25 14:23:19.181605

"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "2d62ce3994ae"
down_revision: Union[str, None] = "0001_init_project_table"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
