"""Change quantity column to Float

Revision ID: 1a2b3c4d5e6f
Revises: c2947bcd2648
Create Date: 2025-06-30 00:00:00.000000
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "1a2b3c4d5e6f"
down_revision: Union[str, Sequence[str], None] = "c2947bcd2648"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("signals", "quantity", existing_type=sa.Integer(), type_=sa.Float())


def downgrade() -> None:
    op.alter_column("signals", "quantity", existing_type=sa.Float(), type_=sa.Integer())
