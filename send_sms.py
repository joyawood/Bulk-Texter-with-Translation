# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Whatup you twilio'd the crap out of that tutorial. #killing it",
                     from_='+17207385004',
                     to='+18024585969'
                 )

print(message.sid)
