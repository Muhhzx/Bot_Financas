from models import db, User, Despesa, Conta
from datetime import datetime

# ================== DESPESAS ==================
def registrar_despesa(numero_wpp, descricao, valor):
    user = User.query.filter_by(numero_wpp=numero_wpp).first()
    if not user:
        return "Usuário não encontrado."

    despesa = Despesa(descricao=descricao, valor=valor, usuario_id=user.id)
    db.session.add(despesa)
    db.session.commit()
    return f"✅ Despesa '{descricao}' de R${valor:.2f} registrada!"

def listar_despesas(numero_wpp):
    user = User.query.filter_by(numero_wpp=numero_wpp).first()
    if not user:
        return "Usuário não encontrado."

    despesas = Despesa.query.filter_by(usuario_id=user.id).all()
    if not despesas:
        return "Nenhuma despesa registrada."

    return "\n".join([f"{d.id}. {d.descricao} - R${d.valor:.2f}" for d in despesas])

def deletar_despesa(numero_wpp, despesa_id):
    user = User.query.filter_by(numero_wpp=numero_wpp).first()
    if not user:
        return "Usuário não encontrado."

    despesa = Despesa.query.filter_by(usuario_id=user.id, id=despesa_id).first()
    if not despesa:
        return "Despesa não encontrada."

    db.session.delete(despesa)
    db.session.commit()
    return f"✅ Despesa '{despesa.descricao}' deletada!"

# ================== CONTAS A PAGAR ==================
def registrar_conta(numero_wpp, descricao, valor, data_vencimento):
    user = User.query.filter_by(numero_wpp=numero_wpp).first()
    if not user:
        return "Usuário não encontrado."

    conta = Conta(
        descricao=descricao,
        valor=valor,
        data_vencimento=data_vencimento,
        usuario_id=user.id
    )
    db.session.add(conta)
    db.session.commit()
    return f"✅ Conta '{descricao}' de R${valor:.2f} registrada para {data_vencimento.strftime('%d/%m/%Y')}!"

def listar_contas(numero_wpp):
    user = User.query.filter_by(numero_wpp=numero_wpp).first()
    if not user:
        return "Usuário não encontrado."

    hoje = datetime.utcnow()
    contas = Conta.query.filter(Conta.usuario_id==user.id, Conta.pago==False).order_by(Conta.data_vencimento).all()
    if not contas:
        return "Nenhuma conta pendente."

    return "\n".join([f"{c.id}. {c.descricao} - R${c.valor:.2f} - Vence {c.data_vencimento.strftime('%d/%m/%Y')}" for c in contas])

def pagar_conta(numero_wpp, conta_id):
    user = User.query.filter_by(numero_wpp=numero_wpp).first()
    if not user:
        return "Usuário não encontrado."

    conta = Conta.query.filter_by(usuario_id=user.id, id=conta_id).first()
    if not conta:
        return "Conta não encontrada."

    conta.pago = True
    db.session.commit()
    return f"✅ Conta '{conta.descricao}' marcada como paga!"
