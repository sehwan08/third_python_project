from selenium import webdriver

#경로가 다르면 Chrome()안에 정확히 경로를 넣어 주자
browser = webdriver.Chrome() #"./chromedriver.exe"

browser.get("http://naver.com")