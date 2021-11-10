from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

interval = 2

browser = webdriver.Chrome(options=options)
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)


time.sleep(1)


#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval) #로딩이 더 걸리면 interval을 늘리면 됨

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")


soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

    # 할인 전
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "<할인 되지 않은 영화>")
        continue
    
    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목:{title}")
    print(f"할인 전 가격:{original_price}")
    print(f"할인 후 가격:{price}")
    print("링크:","https://play.google.com"+link)
    print("-"*100)

browser.quit()