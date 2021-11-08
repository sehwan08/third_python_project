from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C+%EC%98%88%EC%95%BD&oquery=%ED%95%AD%EA%B3%B5%EA%B6%8C&tqi=hhUfClprvOsssZqbnu0ssssss3o-087722"
browser.get(url)

# 가는날 선택 클릭
time.sleep(1)
browser.find_element_by_link_text("가는날 선택").click()

#가는 날짜 / 오는 날짜 선택
time.sleep(1)
browser.find_elements_by_link_text("27")[0].click() #달변경은 [""] 1,2,3 으로 바꾸면 된다
browser.find_elements_by_link_text("28")[1].click()


#제주도 선택
# browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li/[1]/div/a").click()
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()
#엘리멘트가 나올때까지 기다려줌
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))
    print(elem.text) #첫번째 결과 출력
finally:
    browser.quit()

#첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)

# # 가는날 선택 클릭
# time.sleep(2)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# #가는 날짜 선택
# time.sleep(2)

# # browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table[0]/tbody/tr[2]/td[5]/button").click()
# # time.sleep(2)
# # browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table[1]/tbody/tr[2]/td[5]/button").click()



# #//*[@id="_flight_section"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]' -> 열렸을때 xpath
