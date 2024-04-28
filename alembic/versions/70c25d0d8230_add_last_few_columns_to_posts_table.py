"""add last few columns to posts table

Revision ID: 70c25d0d8230
Revises: c75630062c26
Create Date: 2024-04-17 10:56:54.850427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70c25d0d8230'
down_revision: Union[str, None] = 'c75630062c26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'publised')
    op.drop_column('posts', 'created_at')
    pass
