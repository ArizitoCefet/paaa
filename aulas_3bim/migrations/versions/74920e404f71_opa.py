"""opa

Revision ID: 74920e404f71
Revises: 
Create Date: 2024-11-18 15:47:01.938079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74920e404f71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('departamento', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido',
    sa.Column('id_pedido', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('valor_total', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id_pedido')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pedido')
    op.drop_table('cliente')
    # ### end Alembic commands ###
