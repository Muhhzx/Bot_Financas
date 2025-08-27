from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask (__name__)

@app.route("/whatsapp", methods=['POST'])
def bot_financas():
    msg= request.form.get('Body').lower()
    
    response = MessagingResponse()
    response.message(f"Voce disse: {msg}")

    return str(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)