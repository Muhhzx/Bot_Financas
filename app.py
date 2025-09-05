from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os
from services.reset_service import resetar_despesas
from controllers.bot_controller import bot_bp
from models import db

load_dotenv()



app = Flask(__name__)
app.register_blueprint(bot_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///despesas.db"
app.config ["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP")
NUMERO_USUARIO = os.getenv("NUMERO_USUARIO")
client = Client(ACCOUNT_SID, AUTH_TOKEN)

scheduler = BackgroundScheduler()
scheduler.add_job(resetar_despesas, "cron", day=30, hour=0, minute=0)  # todo dia 30 às 00h
scheduler.start()






if __name__ == "__main__":
    app.run(debug=True)
