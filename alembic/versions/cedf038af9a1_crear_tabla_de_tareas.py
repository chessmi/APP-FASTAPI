from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'cedf038af9a1'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'todos',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.Text),
        sa.Column('completed', sa.Boolean, nullable=False, server_default=sa.text('false'))
    )

def downgrade():
    op.drop_table('todos')

