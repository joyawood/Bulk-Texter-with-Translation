# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
number = os.environ['USER_NUMBER']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Whatup you twilio'd the crap out of that tutorial. #killing it",
                     from_='+17207385004',
                     to=number
                 )

print(message.sid)
