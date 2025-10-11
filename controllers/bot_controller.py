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
    numero = request.form.get("From", "").replace("whatsapp:", "").strip()
    msg = request.form.get("Body", "").strip().lower()
    resp = MessagingResponse()

    user = User.query.filter_by(numero_wpp=numero).first()
    if not user:
        user = User(numero_wpp=numero)
        db.session.add(user)
        db.session.commit()

    # ===== COMANDOS =====
    if msg.startswith("add "):
        try:
            partes = msg.split(" ")
            descricao = " ".join(partes[1:-1])
            valor = float(partes[-1])
            resposta = registrar_despesa(numero, descricao, valor)
        except ValueError:
            resposta = "❌ Formato inválido! Use: add <descrição> <valor>"

    elif msg == "listar":
        resposta = listar_despesas(numero)

    elif msg.startswith("del "):
        try:
            _, id_str = msg.split(" ", 1)
            resposta = deletar_despesa(numero, int(id_str))
        except ValueError:
            resposta = "❌ Formato inválido! Use: del <id>"

    elif msg.startswith("conta add "):
        try:
            partes = msg.split(" ")
            descricao = " ".join(partes[2:-2])
            valor = float(partes[-2])
            data_venc = datetime.strptime(partes[-1], "%d/%m/%Y")
            resposta = registrar_conta(numero, descricao, valor, data_venc)
        except Exception:
            resposta = "❌ Use: conta add <descrição> <valor> <dd/mm/yyyy>"

    elif msg == "conta listar":
        resposta = listar_contas(numero)

    elif msg.startswith("conta pagar "):
        try:
            _, _, id_str = msg.split(" ", 2)
            resposta = pagar_conta(numero, int(id_str))
        except ValueError:
            resposta = "❌ Use: conta pagar <id>"

    else:
        resposta = (
            "📘 *Comandos disponíveis:*\n"
            "- add <descrição> <valor>\n"
            "- listar\n"
            "- del <id>\n"
            "- conta add <descrição> <valor> <dd/mm/yyyy>\n"
            "- conta listar\n"
            "- conta pagar <id>"
        )

    resp.message(resposta)
    return str(resp)
