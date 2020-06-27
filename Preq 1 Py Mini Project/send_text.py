from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "----------------------------"
# Your Auth Token from twilio.com/console
auth_token = "----------------------------"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+91----------",
    from_="+1------------",
    body="We are going to mars, Sarim Chaudhary")

print(message.sid)
