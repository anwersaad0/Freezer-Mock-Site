"""empty message

Revision ID: 744643d4f587
Revises: 
Create Date: 2024-06-02 19:18:01.622453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa860962c557'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('clearance', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('forum_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=False),
    sa.Column('ip', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media_like',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('media_id', sa.Integer(), nullable=False),
    sa.Column('reaction', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['media_id'], ['media.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'media_id')
    )
    op.create_table('post_like',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('reaction', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['forum_posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.create_table('replies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['forum_posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reply_like',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('reply_id', sa.Integer(), nullable=False),
    sa.Column('reaction', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['reply_id'], ['replies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'reply_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply_like')
    op.drop_table('replies')
    op.drop_table('post_like')
    op.drop_table('media_like')
    op.drop_table('media')
    op.drop_table('forum_posts')
    op.drop_table('users')
    op.drop_table('shop_items')
    # ### end Alembic commands ###
