#!/usr/bin/python3
# -*- coding:UTF-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymongo
import time

host = 'https://tianqi.moji.com'
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client.test
isFlush = False
if isFlush:
    db.city.remove({})

def update_db(id, params):
    db.city.update_one({"_id": id}, {"$set": params}, upsert=True)

# url = urlopen('https://tianqi.moji.com/weather/china/beijing/haidian-district')
# soup = BeautifulSoup(url, 'html.parser')   # parser 解析
#
# alert = soup.find('div', class_="wea_alert clearfix").em
# print("空气质量：" + alert.string)
#
# weather = soup.find('div', class_="wea_weather clearfix")
# print("当前温度：" + weather.em.string + "℃")
# print("天气：" + weather.b.string)


def spiderProvince():
    htmlContent = urlopen('https://tianqi.moji.com/weather/china/')
    soupAll = BeautifulSoup(htmlContent, 'html.parser')   # parser 解析
    emList = soupAll.select('.city .clearfix li a')
    provinceDic = {}
    for em in emList:
        #s = BeautifulSoup(em, 'html.parser')
        #city = s.select('a')
        url = em.attrs['href']
        cityCN = em.text
        cityEN = url.split('/')[-1]
        provinceDic[cityEN] = cityCN
        print(url, cityCN, cityEN)
        update_db(cityEN, {'name': cityCN, 'name_en': cityEN, 'parent': 'china', 'url': url})

#spiderProvince()
#exit()

def spiderCity(url, city):
    soup = BeautifulSoup(urlopen(host + url), 'html.parser')
    emList = soup.select('.city_hot li a')
    for em in emList:
        curl = em.attrs['href']
        cityCN = em.text
        cityEN = curl.split('/')[-1]
        # print({'id': cityEN, 'name': cityCN, 'parent': city})
        print(cityCN)
        update_db(curl, {'name': cityCN, 'name_en': cityEN, 'parent': city})

def getCity():
    all = db.city.find({})
    for v in all:
        print(v['_id'])
        spiderCity(v['_id'], v['name_en'])
        time.sleep(1)


getCity()
#spiderCity('guangdong')

# for p in provinceDic.keys():
#     url = host + '/weather/china/' + p
#     print(url)
#     #soup = BeautifulSoup(urlopen(host + '/weather/china/' + p), 'html.parser')
#     break

def spiderWeather(cityInfo):
    url = host + '/weather/' + cityInfo['parent'] + '/' + cityInfo['_id']
    print(url)


spiderWeather({
	"_id" : "nanshan-district",
	"name" : "鹤岗市南山区",
	"parent" : "heilongjiang"
})
