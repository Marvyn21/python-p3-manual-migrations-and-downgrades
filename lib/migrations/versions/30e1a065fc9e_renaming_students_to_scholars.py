"""Renaming students to scholars

Revision ID: 30e1a065fc9e
Revises: 791279dd0760
Create Date: 2023-06-02 14:41:09.700050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30e1a065fc9e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('students', 'scholars')
