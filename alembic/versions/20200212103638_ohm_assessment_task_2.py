"""ohm_assessment_task_2

Revision ID: 97e6fc74a79
Revises: b1909833151
Create Date: 2020-02-12 10:36:38.517339

"""

# revision identifiers, used by Alembic.
revision = '97e6fc74a79'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user
                  SET point_balance=5000.0
                  WHERE user_id=1
               ''')
    op.execute('''UPDATE user
                  SET tier="Silver"
                  WHERE user_id=3
               ''')
    op.execute('''INSERT INTO rel_user (user_id, rel_lookup, attribute)
                  VALUES (2, 'LOCATION', 'USA')
               ''')


def downgrade():
    op.execute('''UPDATE user
                  SET point_balance=0.0
                  WHERE user_id=1
               ''')
    op.execute('''UPDATE user
                  SET tier="Carbon"
                  WHERE user_id=3
               ''')
    op.execute('''DELETE FROM rel_user
                  WHERE user_id=2
               ''')
