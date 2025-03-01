from flask import Blueprint, render_template, request, redirect, flash
from models import Cliente
from database import db

bp_cliente = Blueprint('clientes', __name__, template_folder='templates')

@bp_cliente.route('/')
def index():
    dados = Cliente.query.all()
    return render_template('clientes.html', clientes = dados)

@bp_cliente.route('/add')
def add():
    return render_template('clientes_add.html')

@bp_cliente.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    if nome and email:
        bd_cliente = Cliente(nome=nome, email=email)
        db.session.add(bd_cliente)
        db.session.commit()
        flash('Cliente salvo com sucesso!!!')
        return redirect('/clientes')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/clientes/add')





