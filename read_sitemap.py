import requests
from bs4 import BeautifulSoup
import json

sitemap_url = "https://mr90.top/sitemap.xml"
response = requests.get(sitemap_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")

    urls = []
    for loc in soup.find_all("guid"):
        url = loc.text
        if "/zh/" in url:
            urls.append({"url": url, "variables": {"lang": ["zh-CN"]}})
        else:
            urls.append({"url": url, "variables": {"lang": ["en-US"]}})

    data = {
        "index_name": "ryan",
        "start_urls": urls,
        "selectors": {
            "lvl0": "#app .prose h1",
            "lvl1": "#app article .prose h1",
            "lvl2": "#app article .prose h3",
            "lvl3": "#app article .prose h4",
            "lvl4": "#app article .prose h5",
            "lvl5": "#app article .prose h6",
            "text": "#app header p,#app article .prose p,#app article .prose ol",
        },
    }

    print(data)

    with open("config.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Data saved to data.json")
else:
    print("Failed to fetch sitemap.xml")
