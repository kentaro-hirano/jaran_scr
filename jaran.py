# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup

url = "https://www.jalan.net/ranking/ryokan/index.html"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
hotels = soup.select('.mgt15')

data = []
for hotel in hotels:
    h_name = hotel.find('a').text
    n_trim_name = h_name.replace('　', '')

    hotel_sub_title = hotel.find(class_="tx14_333b").text

    hotel_rank = hotel.find('img').get('alt')

    hotel_detail = hotel.find(class_="tx_basic").text.split('\n')[0].replace('\r', '')
    
    bf_address = hotel.text.split('[住所]')[1].split('\xa0')[0].replace('[最寄駅]', '')
    hotel_address = bf_address.replace(' ', '')

    bf_closest_station = hotel.text.split('[住所]')[1].split('\xa0')[1].replace('[最寄駅]', '')
    closest_station = bf_closest_station.split('\n')[0].replace(' ', '')

    most_low_price = hotel.find(class_= "red").text

    eval = float(hotel.find(class_= "s14_30b").text)

    bf_detail_link = hotel.find(class_= "mgt15")
    detail_link = hotel.find('a').get('href')

    datum = {}
    datum['順位'] = hotel_rank
    datum['名称'] = n_trim_name
    datum['小見出し'] = hotel_sub_title
    datum['詳細'] = hotel_detail
    datum['住所'] = hotel_address
    datum['最寄駅'] = closest_station
    datum['最安値'] = most_low_price
    datum['クチコミ総合'] = eval
    datum['詳細リンク'] = detail_link
    data.append(datum)
data

import pandas as pd

df = pd.DataFrame(data)
df

df.to_csv('じゃらん.csv')