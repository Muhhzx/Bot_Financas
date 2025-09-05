from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Despesa(db.Model):
    __tablename__ = "despesas"

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    usuario = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Despesa {self.descricao} - R${self.valor:.2f}>"
