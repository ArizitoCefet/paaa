from database import db

class Cliente(db.Model):
    __tablename__='cliente'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return "<Cliente {}>".format(self.nome)


class Pedido(db.Model):
    __tablename__ = 'pedido'
    id_pedido = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    valor_total = db.Column(db.Numeric(10, 2))

    def __init__(self, id_pedido, data, id_cliente, valor_total):
        self.id_pedido = id_pedido
        self.data = data
        self.id_cliente = id_cliente
        self.valor_total = valor_total

    def __repr__(self):
        return "<Pedido {} - {} - {}>".format(self.cliente_nome, self.pedido.valor_total, self.data)