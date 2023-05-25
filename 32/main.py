import smtplib
import datetime as dt
from random import choice


def send_mail():
    my_email = "from_mail@gmail.com"
    my_email_password = "*****"
    sender_email = "to_mail@gmail.com"

    with open("quotes.txt") as data_file:
        lines = data_file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        connection.sendmail(from_addr=my_email, to_addrs=sender_email,
                            msg=f"Subject:A quote for you.\n\n{choice(lines)}")


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = days[dt.datetime.now().weekday()]

if now == "Wednesday":
    send_mail()
    print("Mail send")
