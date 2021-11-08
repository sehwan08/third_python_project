from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C+%EC%98%88%EC%95%BD&oquery=%ED%95%AD%EA%B3%B5%EA%B6%8C&tqi=hhUfClprvOsssZqbnu0ssssss3o-087722"
browser.get(url)

# 가는날 선택 클릭
time.sleep(2)
browser.find_element_by_xpath("//*[@id='_flight_section']/div/div[2]/div[2]/div[2]/div/div[1]/div[1]").click()

#가는 날짜 선택
time.sleep(2)

# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table[0]/tbody/tr[2]/td[5]/button").click()
# time.sleep(2)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table[1]/tbody/tr[2]/td[5]/button").click()



#//*[@id="_flight_section"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]' -> 열렸을때 xpath











# # 가는날 선택 클릭
# time.sleep(2)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# #가는 날짜 선택
# time.sleep(2)

# # browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table[0]/tbody/tr[2]/td[5]/button").click()
# # time.sleep(2)
# # browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table[1]/tbody/tr[2]/td[5]/button").click()



# #//*[@id="_flight_section"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]' -> 열렸을때 xpath
