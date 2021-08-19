from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4e698c33bfeebb74"
auth_token = "7c34333da888886f50bb9fe68c7"

client = Client(account_sid, auth_token)
message = client.messages.create(
    # 这里中国的号码前面需要加86
    to="+8615968040165", 
    from_="+14158959062",
    body="Hello from fdsafsadfsafdsafsafdsafsda!")
print(message.sid)


print(2342143213)
