from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from models import db, User
from services.bot_service import (
    registrar_despesa, listar_despesas, deletar_despesa,
    registrar_conta, listar_contas, pagar_conta
)
from datetime import datetime

bot_bp = Blueprint("bot", __name__)

@bot_bp.route("/whatsapp", methods=["POST"])
def bot_financas():
    numero = request.form.get("From")
    msg = request.form.get("Body").strip().lower()
    resp = MessagingResponse()

    # Cria usuário automaticamente se não existir
    user = User.query.filter_by(numero_wpp=numero).first()
    if not user:
        user = User(numero_wpp=numero)
        db.session.add(user)
        db.session.commit()

    # ===== COMANDOS =====
    if msg.startswith("add "):
        try:
            _, descricao, valor = msg.split(" ", 2)
            resposta = registrar_despesa(numero, descricao, float(valor))
        except ValueError:
            resposta = "Formato inválido! Use: add <descricao> <valor>"

    elif msg == "listar":
        resposta = listar_despesas(numero)

    elif msg.startswith("del "):
        try:
            _, id_str = msg.split(" ", 1)
            resposta = deletar_despesa(numero, int(id_str))
        except ValueError:
            resposta = "Formato inválido! Use: del numero da despesa"

    elif msg.startswith("conta add "):
        try:
            _, descricao, valor, data_str = msg.split(" ", 3)
            data_vencimento = datetime.strptime(data_str, "%d/%m/%Y")
            resposta = registrar_conta(numero, descricao, float(valor), data_vencimento)
        except ValueError:
            resposta = "Formato inválido! Use: conta add <descricao> <valor> <dd/mm/yyyy>"

    elif msg == "conta listar":
        resposta = listar_contas(numero)

    elif msg.startswith("conta pagar "):
        try:
            _, id_str = msg.split(" ", 2)
            resposta = pagar_conta(numero, int(id_str))
        except ValueError:
            resposta = "Formato inválido! Use: conta pagar <id>"

    else:
        resposta = (
            "Comandos disponíveis:\n"
            "- add <descricao> <valor>\n"
            "- listar\n"
            "- del <id>\n"
            "- conta add <descricao> <valor> <dd/mm/yyyy>\n"
            "- conta listar\n"
            "- conta pagar <id>"
        )

    resp.message(resposta)
    return str(resp)
