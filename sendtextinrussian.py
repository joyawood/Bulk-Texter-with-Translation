# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
# Imports the Google Cloud client library
from google.cloud import translate

translate_client = translate.Client()

# The text to translate
text = u'Hello, Alena! How are you?'
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))

newText = format(translation['translatedText'])


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
number = os.environ['USER_NUMBER']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= newText,
                     from_='+17207385004',
                     to=number
                 )

print(message.sid)
