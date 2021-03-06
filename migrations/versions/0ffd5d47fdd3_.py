"""empty message

Revision ID: 0ffd5d47fdd3
Revises: b39882573f06
Create Date: 2022-03-28 16:52:40.194691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffd5d47fdd3'
down_revision = 'b39882573f06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Ads',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.String(length=255), nullable=True),
    sa.Column('ad_review_feedback', sa.String(length=255), nullable=True),
    sa.Column('adlabels', sa.String(length=255), nullable=True),
    sa.Column('adset', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Ads')
    # ### end Alembic commands ###
