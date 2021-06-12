"""Create inital event model

Revision ID: 0d96de75543b
Revises: 
Create Date: 2021-06-12 15:52:55.101360

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0d96de75543b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blockchain_state_events', sa.Column('ts', sa.DateTime(), nullable=False),
                    sa.Column('space', sa.String(length=32), nullable=True),
                    sa.Column('diffculty', sa.Integer(), nullable=True),
                    sa.Column('peak_height', sa.String(length=32), nullable=True),
                    sa.Column('synced', sa.Boolean(), nullable=True), sa.PrimaryKeyConstraint('ts'))
    op.create_table('connection_events', sa.Column('ts', sa.DateTime(), nullable=False),
                    sa.Column('full_node_count', sa.Integer(), nullable=True),
                    sa.Column('farmer_count', sa.Integer(), nullable=True),
                    sa.Column('wallet_count', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('ts'))
    op.create_table('farming_info_events', sa.Column('ts', sa.DateTime(), nullable=False),
                    sa.Column('challenge_hash', sa.String(length=66), nullable=True),
                    sa.Column('signage_point', sa.String(length=66), nullable=True),
                    sa.Column('passed_filter', sa.Integer(), nullable=True),
                    sa.Column('proofs', sa.Integer(), nullable=True), sa.PrimaryKeyConstraint('ts'))
    op.create_index(op.f('ix_farming_info_events_challenge_hash'),
                    'farming_info_events', ['challenge_hash'],
                    unique=False)
    op.create_index(op.f('ix_farming_info_events_signage_point'),
                    'farming_info_events', ['signage_point'],
                    unique=False)
    op.create_table('harvester_events', sa.Column('ts', sa.DateTime(), nullable=False),
                    sa.Column('plot_count', sa.Integer(), nullable=True),
                    sa.Column('plot_size', sa.Integer(), nullable=True), sa.PrimaryKeyConstraint('ts'))
    op.create_table('signage_point_events', sa.Column('ts', sa.DateTime(), nullable=False),
                    sa.Column('challenge_hash', sa.String(length=66), nullable=True),
                    sa.Column('signage_point', sa.String(length=66), nullable=True),
                    sa.Column('signage_point_index', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('ts'))
    op.create_index(op.f('ix_signage_point_events_challenge_hash'),
                    'signage_point_events', ['challenge_hash'],
                    unique=False)
    op.create_index(op.f('ix_signage_point_events_signage_point'),
                    'signage_point_events', ['signage_point'],
                    unique=False)
    op.create_table('wallet_balance_events', sa.Column('ts', sa.DateTime(), nullable=False),
                    sa.Column('confirmed', sa.String(length=32), nullable=True),
                    sa.PrimaryKeyConstraint('ts'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet_balance_events')
    op.drop_index(op.f('ix_signage_point_events_signage_point'), table_name='signage_point_events')
    op.drop_index(op.f('ix_signage_point_events_challenge_hash'), table_name='signage_point_events')
    op.drop_table('signage_point_events')
    op.drop_table('harvester_events')
    op.drop_index(op.f('ix_farming_info_events_signage_point'), table_name='farming_info_events')
    op.drop_index(op.f('ix_farming_info_events_challenge_hash'), table_name='farming_info_events')
    op.drop_table('farming_info_events')
    op.drop_table('connection_events')
    op.drop_table('blockchain_state_events')
    # ### end Alembic commands ###
