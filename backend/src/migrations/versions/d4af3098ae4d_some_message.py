"""some message

Revision ID: d4af3098ae4d
Revises: 
Create Date: 2024-05-03 11:54:47.396819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4af3098ae4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divisions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_divisions'))
    )
    op.create_table('parks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('borough', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_parks'))
    )
    op.create_table('schools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_schools'))
    )
    op.create_table('fields',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('park_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['park_id'], ['parks.id'], name=op.f('fk_fields_park_id_parks')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_fields'))
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('registration', sa.Boolean(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.Column('division_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['division_id'], ['divisions.id'], name=op.f('fk_teams_division_id_divisions')),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], name=op.f('fk_teams_school_id_schools')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_teams'))
    )
    op.create_table('coaches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('pronouns', sa.String(), nullable=True),
    sa.Column('usau', sa.Integer(), nullable=True),
    sa.Column('team_role', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_coaches_team_id_teams')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_coaches')),
    sa.UniqueConstraint('usau', name=op.f('uq_coaches_usau'))
    )
    op.create_table('permits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('field_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['field_id'], ['fields.id'], name=op.f('fk_permits_field_id_fields')),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_permits_team_id_teams')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_permits'))
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('pronouns', sa.String(), nullable=True),
    sa.Column('jersey_number', sa.Integer(), nullable=True),
    sa.Column('usau', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.Column('grade', sa.String(), nullable=True),
    sa.Column('is_captain', sa.Boolean(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_players_team_id_teams')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_players')),
    sa.UniqueConstraint('usau', name=op.f('uq_players_usau'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    op.drop_table('permits')
    op.drop_table('coaches')
    op.drop_table('teams')
    op.drop_table('fields')
    op.drop_table('schools')
    op.drop_table('parks')
    op.drop_table('divisions')
    # ### end Alembic commands ###
