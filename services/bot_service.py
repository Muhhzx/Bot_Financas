from models import db, Despesa
from datetime import datetime

def registrar_despesa(usuario, descricao, valor):
    nova = Despesa(
        descricao=descricao,
        valor=valor,
        data=datetime.now(),
        usuario=usuario
    )
    db.session.add(nova)
    db.session.commit()
    return f"Despesa registrada: {descricao} - R$ {valor:.2f}"

def listar_despesas(usuario):
    despesas = Despesa.query.filter_by(usuario=usuario).all()
    if not despesas:
        return "Nenhuma despesa encontrada."
    resposta = "Suas despesas:\n"
    for d in despesas:
        resposta += f"- {d.descricao}: R$ {d.valor:.2f}\n"
    return resposta


def deletar_despesa(usuario, id_despesa): 
     despesa = Despesa.query.filter_by(id=id_despesa, usuario=usuario).first()
     if not despesa:
        return "Despesa não encontrada."
     db.session.delete(despesa)
     db.session.commit()
     return f"Despesa '{despesa.descricao}' removida com sucesso!"