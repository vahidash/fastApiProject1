"""add content column to posts table

Revision ID: 12240d46f0ef
Revises: 716df9780055
Create Date: 2024-04-17 09:40:10.989644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12240d46f0ef'
down_revision: Union[str, None] = '716df9780055'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
