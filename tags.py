import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()  # html_doc will now contain the content of sample.html

soup = BeautifulSoup(html_doc, 'html.parser')  # soup object

# print(soup.prettify()) # simply prints it
# print(soup.div.string, type(soup.div.string)) # can print one tag from the file
# print(soup.find_all("div"))

# printing all the links
for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get_text())

s = soup.find(id="link3")
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.span.get("class"))

# print(soup.find(id="italic"))