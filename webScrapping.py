import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.10.10:8000",
}

url = "https://www.amazon.com/s?k=gaming+headsets&_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=d84946d3-5597-4c20-ad3c-d60061ef2fa9&pd_rd_w=nhLOi&pd_rd_wg=Qc1kb&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=2ZKB30403A4XJS8JRAMF&ref=pd_gw_unk"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

div = soup.find(class_="card-fs-content-body J_FSBody") # Print the div with this class
print(div)

# div = soup.find(class_="a-row.a-size-base.a-color-secondary")
# # for span in spans:
# print(div)
