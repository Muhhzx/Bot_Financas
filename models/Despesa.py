from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    numero_wpp = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=True)
    despesas = db.relationship("Despesa", backref="usuario", lazy=True)
    contas = db.relationship("Conta", backref="usuario", lazy=True)

class Despesa(db.Model):
    __tablename__ = "despesas"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

class Conta(db.Model):
    __tablename__ = "contas"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    pago = db.Column(db.Boolean, default=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
