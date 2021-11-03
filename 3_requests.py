import requests
res = requests.get("http://google.com") #.get("URL") -> URL 정보를 가져옴
res.raise_for_status()
print("Web scraping starts!")


print(len(res.text))

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)