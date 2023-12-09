"""empty message

Revision ID: 1475ad158bc0
Revises: 64c8ed112095
Create Date: 2023-12-09 19:04:42.118987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision: str = '1475ad158bc0'
down_revision: Union[str, None] = '64c8ed112095'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('content', sa.String(length=256), nullable=False),
    sa.Column('announcement_id', sa.UUID(), nullable=False),
    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['announcement_id'], ['announcements.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###