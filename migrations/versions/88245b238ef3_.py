"""empty message

Revision ID: 88245b238ef3
Revises: 94e00cbf879f
Create Date: 2017-07-16 21:07:17.241513

"""

# revision identifiers, used by Alembic.
revision = '88245b238ef3'
down_revision = '94e00cbf879f'

from alembic import op
import sqlalchemy as sa
import citext
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('errored_pages')
    op.drop_table('siteartistnames')
    op.drop_table('retreival_times')
    op.drop_table('retrieved_pages')
    op.drop_table('statusdb')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statusdb',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sitename', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('sectionname', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('statustext', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='statusdb_pkey'),
    sa.UniqueConstraint('sitename', 'sectionname', name='statusdb_sitename_sectionname_key')
    )
    op.create_table('retrieved_pages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sitename', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('artistname', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('pageurl', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('retreivaltime', sa.REAL(), autoincrement=False, nullable=False),
    sa.Column('downloadpath', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('itempagecontent', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('itempagetitle', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seqnum', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='retrieved_pages_pkey'),
    sa.UniqueConstraint('sitename', 'artistname', 'pageurl', 'seqnum', name='retrieved_pages_sitename_artistname_pageurl_seqnum_key')
    )
    op.create_table('retreival_times',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sitename', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('artistname', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('retreivaltime', sa.REAL(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='retreival_times_pkey'),
    sa.UniqueConstraint('sitename', 'artistname', name='retreival_times_sitename_artistname_key')
    )
    op.create_table('siteartistnames',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sitename', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('artistname', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('uploadeh', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=True),
    sa.Column('last_fetched', postgresql.DOUBLE_PRECISION(precision=53), server_default=sa.text('0'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='siteartistnames_pkey'),
    sa.UniqueConstraint('sitename', 'artistname', name='siteartistnames_sitename_artistname_key')
    )
    op.create_table('errored_pages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sitename', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('artistname', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('pageurl', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('retreivaltime', sa.REAL(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='errored_pages_pkey'),
    sa.UniqueConstraint('sitename', 'artistname', 'pageurl', name='errored_pages_sitename_artistname_pageurl_key')
    )
    ### end Alembic commands ###
