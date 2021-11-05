import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "market capitalization 1~200 rank.csv"
                        #csv저장시 한글깨짐 방지
f = open(filename, "w", encoding="utf-8-sig", newline="") #newline = 자동 줄바꿈을 공백으로
writer = csv.writer(f)
#.split("\t")으로 공백을 처리하면 리스트 형식으로 저장 됨
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns] #이미 리스트 형식으로 받아옴
        # print(data)
        writer.writerow(data) #.writerow()는 반드시 리스트 형태로 넣어야 함