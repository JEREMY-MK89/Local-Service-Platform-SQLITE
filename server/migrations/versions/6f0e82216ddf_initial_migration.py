from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic
revision = '6f0e82216ddf'
down_revision = 'cc9e0abce627'
branch_labels = None
depends_on = None

def _has_table(table_name):
    inspector = Inspector.from_engine(op.get_bind())
    return table_name in inspector.get_table_names()

def _has_column(table_name, column_name):
    inspector = Inspector.from_engine(op.get_bind())
    return column_name in [col['name'] for col in inspector.get_columns(table_name)]

def upgrade():
    # Drop the _alembic_tmp_user table if it exists
    op.execute("DROP TABLE IF EXISTS _alembic_tmp_user")
    
    # Your migration code here
    with op.batch_alter_table('user', schema=None) as batch_op:
        if _has_table('user'):
            if not _has_column('user', 'password_hash'):
                batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))  # Change nullable to True
            if _has_column('user', 'password'):
                batch_op.drop_column('password')

def downgrade():
    # Your downgrade code here
    pass
