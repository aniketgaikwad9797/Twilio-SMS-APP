from twilio.rest import Client
from credentials import account_sid,authentication_token,my_phone,my_twilio_number

client = Client(account_sid, authentication_token)

my_message = input("Enter something silly to be send on your phone number \n")

message = client.messages.create(to=my_phone,body=my_message,from_=my_twilio_number)


