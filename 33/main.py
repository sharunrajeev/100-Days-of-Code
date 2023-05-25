import datetime
import smtplib
import time

import requests

MY_LAT = 51.2639
MY_LONG = 59.0944
MY_MAIL = "my_mail@gmail.com"
PASSWORD = "*****"
TO_MAIL = "to_mail@gmail.com"


def send_mail():
    with smtplib.SMTP("smtp.google.com") as conn:
        conn.starttls()
        conn.login(user=MY_MAIL, password=PASSWORD)
        conn.sendmail(from_addr=MY_MAIL, to_addrs=TO_MAIL,
                      msg="Subject:ISS above you!\n\nCheck out the sky to see the ISS")


def check_if_iss_is_above():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    location = (
        float(iss_response.json()["iss_position"]["latitude"]), float(iss_response.json()["iss_position"]["longitude"]))

    if MY_LAT - 5 < location[0] < MY_LAT + 5 and MY_LONG - 5 < location[1] < MY_LONG + 5:
        sun_response = requests.get(
            url=f"https://api.sunrise-sunset.org/json?lat={location[0]}&lng={location[1]}&formatted=0")
        sun_response.raise_for_status()

        print(sun_response.json()["results"])
        sunrise = int(sun_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(sun_response.json()["results"]["sunset"].split("T")[1].split(":")[0])

        hour_now = datetime.datetime.now().hour

        print(sunrise, hour_now, sunset)

        if sunrise < hour_now > sunset:
            send_mail()


while True:
    time.sleep(60)
    check_if_iss_is_above()