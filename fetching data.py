import requests

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.10.10:8000",
}

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)


url = "https://www.amazon.com/dp/B0C7GW9F88/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t"

fetchAndSaveToFile(url, "data/amazon.html")
