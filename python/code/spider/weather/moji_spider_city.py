#!/usr/bin/python3
# -*- coding:UTF-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymongo
import time

class mojiSpiderCity:

    _host = 'mongodb://127.0.0.1:27017/'

    _db = 'test'  # 库

    _col = 'city'  # 集合

    _client = ''  # 连接

    #_isFlush = False  # 是否情况原有的城市数据

    _isFlush = True  # 是否情况原有的城市数据

    _mojiHost = 'https://tianqi.moji.com'  # 墨迹天气的域名

    _provinceDic = {}  # 省份字典（辅助字段）

    _updateTime = 0

    def __init__(self):
        self._client = pymongo.MongoClient(self._host)[self._db][self._col]
        self._updateTime = time.time()
        if self._isFlush:
            self._client.remove({})

    # 将数据写入DB
    def _updateDb(self, id, params):
        params['update_time'] = int(self._updateTime)
        self._client.update_one({"_id": id}, {"$set": params}, upsert=True)

    # 爬取：省份
    def spiderProvince(self):
        htmlContent = urlopen('https://tianqi.moji.com/weather/china/')
        soupAll = BeautifulSoup(htmlContent, 'html.parser')  # parser 解析
        emList = soupAll.select('.city .clearfix li a')
        for em in emList:
            url = em.attrs['href']
            cityCN = em.text
            cityEN = url.split('/')[-1]
            params = {'_id': cityEN, 'name': cityCN, 'name_en': cityEN, 'parent': 'china', 'url': self._mojiHost + url}
            self._provinceDic[cityEN] = params
            # print(url, cityCN, cityEN)
            self._updateDb(cityEN, params)

    # 爬取：城市
    def spiderCity(self):
        for info in self._provinceDic.values():
            time.sleep(1)
            soup = BeautifulSoup(urlopen(info['url']), 'html.parser')
            emList = soup.select('.city_hot li a')
            for em in emList:
                url = em.attrs['href']
                cityCN = em.text
                cityEN = '/'.join(url.split('/')[-2:])
                print(url, cityCN, cityEN)
                self._updateDb(cityEN, {'name': cityCN, 'name_en': cityEN, 'parent': info['_id'], 'url': url})


if __name__ == '__main__':
    spider = mojiSpiderCity()
    spider.spiderProvince()
    spider.spiderCity()
    print('墨迹天气的城市信息，已同步完成')
    exit(0)



