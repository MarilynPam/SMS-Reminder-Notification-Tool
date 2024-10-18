# SMS Task Reminder Tool

This is a simple Python program that sends task reminder text messages using the Twilio API.

## Modules to Import

```python
import csv
from datetime import datetime, timedelta
from twilio.rest import Client
```

## How To Use
1. Set Up Twilio: Open the program and enter your Twilio account details. You can customize the reminder message to fit your needs.
2. Create CSV File: Open the CSV file with Microsoft Excel and enter the information in the following columns: name, phone number, and date of assignment. Note: do not change the name of the CSV file.
3. Run the Program: Execute the program to send reminder texts.
4. Automate the Process: Use an automation tool to run the program daily, ensuring that reminders are sent consistently.
