import sqlite3
from twilio.rest import Client
import os

def resetar_despesas(client):
    conn = sqlite3.connect("financas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM despesas")
    conn.commit()
    conn.close()

    client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP"),
        body="✅ Suas despesas foram resetadas para o novo mês!",
        to=os.getenv("NUMERO_USUARIO")
    )