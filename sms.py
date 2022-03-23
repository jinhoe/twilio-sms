import config
from twilio.rest import Client

client = Client(config.account_sid, config.auth_token)

message = client.messages.create(
    to="+6588888888 [RECEIVER NUMBER]",
    from_="+13388888888 [TWILIO NUMBER]",
    body="This is our first message."
)

print(message.sid)