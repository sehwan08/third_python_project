import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})

# 만화 제목 + 링크 가져 오기
# print(cartoons)
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)



# 평점 구하기
total_ratings = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rating = cartoon.strong.get_text()
    print(rating)
    total_ratings += float(rating)

print("Total Ratings: ",total_ratings)
print("Average Ratings: ",total_ratings / len(cartoons))

