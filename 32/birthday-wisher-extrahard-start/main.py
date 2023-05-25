# ---------------------- Extra Hard Starting Project -------------------------
import csv
import datetime
from random import randint
import smtplib

import pandas as pd

# Constants
EMAIL = "from_mail@gmail.com"
PASSWORD = "*********"


# Functions
def select_a_letter(name):
    file_name = f"./letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_name) as letter_file:
        letter_data = letter_file.read()
        letter_data = letter_data.replace("[NAME]", name)
    return letter_data


def send_mail(content, mail_to):
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=mail_to, msg=f"Subject:Birthday Wishes!\n\n{content}")


# 1. Update the birthdays.csv
if input("Do you want to add birthday? (y/n) : ") == 'y':
    data = [input("Enter name : "), input("Enter email : "), input("Year (YYYY) : "), input("Month (MM) : "),
            input("Date (DD) : ")]
    with open("birthdays.csv", "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)
else:
    # 2. Check if today matches a birthday in the birthdays.csv
    csv_data = pd.read_csv("birthdays.csv")
    csv_data = csv_data.to_dict(orient="records")
    today = datetime.datetime.now()
    day, month, year = today.day, today.month, today.year
    for i in csv_data:
        if i["day"] == day and i["month"] == month and i["year"] == year:
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
            # name from birthdays.csv
            content_to_send = select_a_letter(name=i["name"])

            # 4. Send the letter generated in step 3 to that person's email address.
            send_mail(content_to_send, i["email"])
