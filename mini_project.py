import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&query=%EC%98%A4%EB%8A%98+%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&ie=utf8&sm=tab_she&qdt=0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#맑음, 어제보다 00 
cast0 = soup.find("span", attrs={"class":"weather before_slash"}).get_text()
cast1 = soup.find("p", attrs={"class":"summary"}).get_text()
cast2 = soup.find("span", attrs={"class":"temperature down"}).get_text()
cast3 = soup.find("span", attrs={"class":"blind"}).get_text()



#현재 온도
curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("온도", "")
min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
max_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")


#강수 확률
# rainfalls = soup.find_all("span", {"rainfall"})[0].text()
# rainfalls = soup.find("span", attrs={"class":"rainfall"}).get_text()
rainfalls = soup.find("span", {"class":"week_list"}).find_all("span",{"class":"rainfall"})
print(rainfalls)





# def scrape_weather():
#     print("[오늘의 날씨]")
#     url = "https://search.naver.com/search.naver?where=nexearch&query=%EC%98%A4%EB%8A%98+%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&ie=utf8&sm=tab_she&qdt=0"
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
    
#     #맑음, 어제보다 00 
#     cast0 = soup.find("span", attrs={"class":"weather before_slash"}).get_text()
#     cast1 = soup.find("p", attrs={"class":"summary"}).get_text()
#     cast2 = soup.find("span", attrs={"class":"temperature down"}).get_text()
#     cast3 = soup.find("span", attrs={"class":"blind"}).get_text()

#     #현재 온도
#     curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text()
#     min_temp = None
#     max_temp = None






# if __name__ == "__main__":
#     scrape_weather() #오늘의 날씨 정보 가져 오기