from requests import get
from bs4 import BeautifulSoup
import lxml

r = get("https://www.amazon.in/URBN-10000-22-5W-Charging-Output/dp/B08JW1GVS7/ref=sr_1_8?keywords=power%2Bbank%2Bfast"
        "%2Bcharging%2Btype%2Bc&qid=1689866068&sprefix=power%2Bbank%2Bfast%2Bcharging%2B%2Caps%2C218&sr=8-8&th=1",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8"
        })

soup = BeautifulSoup(r.content, "lxml")

price = soup.select(selector="#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > "
                             "span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child("
                             "2) > span.a-price-whole")[0].text

if price <= 1000:
    print("Buy now!")
