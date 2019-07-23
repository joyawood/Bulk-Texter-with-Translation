from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import translate

translate_client = translate.Client()

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])



def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # The text to translate
    text = u'Glad to hear it!'
    # The target language
    target = 'ru'
    translation = translate_client.translate(
    text,
    target_language=target)

    newText = format(translation['translatedText'])

    # Add a message
    resp.message(newText)
    print(newText)
    return str(resp)

if __name__ == "__main__":
        app.run(debug=True)
