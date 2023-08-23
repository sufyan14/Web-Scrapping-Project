import requests
import pandas as pd
from bs4 import BeautifulSoup

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.10.10:8000",
}

data = {'title': [], 'price': []}

url = "https://www.ebay.com/itm/354586733872?_trkparms=pageci%3A1a2720bf-4113-11ee-b135-be5081a9b63b%7Cparentrq%3A1e562f2f18a0a8cc3c19d5d1ffff0906%7Ciid%3A1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# div = soup.find(class_="card-fs-content-body J_FSBody") # Print the div with this class
# print(div)

# div = soup.find(class_="a-row.a-size-base.a-color-secondary")
# # for span in spans:
# print(div)

spans = soup.find(class_="x-item-title__mainTitle")  # Title Scrapped
prices = soup.find(class_="x-price-primary")  # Price scrapped

if spans:
    title = spans.get_text()
    print(title)
    data['title'].append(title)
else:
    print("Title not found.")

if prices:
    price_value = prices.get_text()
    print(price_value)
    data['price'].append(price_value)
else:
    print("Price not found.")


df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)
