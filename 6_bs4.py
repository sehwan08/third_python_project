import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

#URL을 통해 가져온 HTML문서를 'lxml'을 통해 파싱을 하고 객체로 만듬
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find("a", attrs={"onclick":"nclk_v2(event,'rnk*p.cont','570503','1')"}))
# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank1.find_next_siblings("li")

webtoon = soup.find("a", text="연애혁명-375. 입장정리")
print(webtoon)
