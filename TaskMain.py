import csv
from datetime import datetime, timedelta
from twilio.rest import Client


#obtain current date and calculate date 7 days from now
current_date = datetime.now()
target_date = current_date + timedelta(days=7)
target_date_string = target_date.strftime('%m/%d/%Y')
  #print(target_date_string)

#Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
client = Client(account_sid, auth_token)


#Open and read the CSV contacts file
with open('contacts.csv', mode='r', newline='') as contactsFile:
    csv_reader = csv.DictReader(contactsFile)

    #loop to iterate through rows in CSV
    for row in csv_reader:
        date = row['Part Date']
        phone_number = row['Phone Number']
        contact_name = row['Name']

        if date == target_date_string:
            #print("hello")
            #dates are the same, send SMS
            message = client.messages.create(
                body=f"This is a reminder for {row['Name']}: Your assigned task is on {row['Part Date']}.",
                from_=twilio_phone_number,
                to=phone_number
            )
            print(f"Sent message to {contact_name} at {phone_number}")

print("Script finished.")





