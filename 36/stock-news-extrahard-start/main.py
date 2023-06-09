import os

import requests
from dotenv import load_dotenv
from os import environ
import datetime as dt
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CHANGE = 1

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# My Code from here
AV_API_KEY = environ["AV_API_KEY"]
NEWS_API_KEY = environ["NEWS_API_KEY"]
TWILIO_SID = environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = environ["TWILIO_AUTH_TOKEN"]

AV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={AV_API_KEY}'
NEWS_URL = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}'
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Stock Data
r = requests.get(AV_URL)
stock_data = r.json()
time_series_data = stock_data['Time Series (60min)']
# News Data
r = requests.get(NEWS_URL)
news_data = r.json()['articles']


def get_news(percentage_change):
    if percentage_change > 0:
        emoji = '🔺'
    else:
        emoji = '🔻'
    msg = f'{STOCK} : {emoji} {percentage_change}\n'
    for i in range(3):
        msg += f"----------- News {i + 1}----------\nHeadline : {news_data[i]['title']}\nBrief : {news_data[i]['description']}\n"
    return msg


yesterday = str(dt.datetime.now().date() - dt.timedelta(days=2)) + ' 19:00:00'
day_before_yesterday = str(dt.datetime.now().date() - dt.timedelta(days=3)) + ' 19:00:00'
stock_change = float(time_series_data[yesterday]['4. close']) - float(
    time_series_data[day_before_yesterday]['4. close'])
stock_change_percentage = stock_change / float(time_series_data[day_before_yesterday]['4. close']) * 100
print(stock_change_percentage)
if abs(stock_change_percentage) > CHANGE:
    to_send_data = get_news(stock_change_percentage)
    message = client.messages.create(
        body=to_send_data,
        from_='+13614181333',
        to=environ['PHONE_NO']
    )
    print(message.sid)
