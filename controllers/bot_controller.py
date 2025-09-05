from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from services.bot_service import registrar_despesa, listar_despesas, deletar_despesa

bot_bp = Blueprint("bot", __name__)

@bot_bp.route("/whatsapp", methods=["POST"])
def bot_financas():
    user = request.form.get("From")
    msg = request.form.get("Body").strip().lower()
    resp = MessagingResponse()

    if msg.startswith("add "):  # Exemplo: "add pizza 45.90"
        try:
            _, descricao, valor = msg.split(" ", 2)
            resposta = registrar_despesa(user, descricao, float(valor))
        except ValueError:
            resposta = "Formato inválido! Use: add <descricao> <valor>"

    elif msg == "listar":
        resposta = listar_despesas(user)

    elif msg.startswith("del "):  # Exemplo de uso: "del 3"
        try:
            _, id_str = msg.split(" ", 1)
            resposta = deletar_despesa(user, int(id_str))
        except ValueError:
            resposta = "Formato inválido! Use: del numero da despesa"

    else:
        resposta = (
            "Comandos disponíveis:\n"
            "- add <descricao> <valor>\n"
            "- listar\n"
            "- del numero da despesa"
        )

    resp.message(resposta)
    return str(resp)
