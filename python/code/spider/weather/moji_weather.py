#!/usr/bin/python3
# -*- coding:UTF-8 -*-

'''
墨迹天气，获取天气的详细信息
抓取页面：https://tianqi.moji.com/weather/china/guangdong/nanshan-district
'''
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymongo
import time

class mojiSpiderCity:

    _host = 'mongodb://127.0.0.1:27017/'

    _db = 'test'  # 库

    _colCity = 'city'

    _col = 'weather_daily'  # 集合

    _colCal = 'weather_calendar'  # 天气日历

    _client = ''  # 连接

    #_isFlush = False  # 是否情况原有的城市数据

    _isFlush = True  # 是否情况原有的城市数据

    _mojiHost = 'https://tianqi.moji.com'  # 墨迹天气的域名

    _provinceDic = {}  # 省份字典（辅助字段）

    _updateTime = 0

    def __init__(self):
        self._client = pymongo.MongoClient(self._host)[self._db]
        self._updateTime = time.time()
        if self._isFlush:
            today = time.strftime("%Y%m%d", time.localtime())
            self._client[self._col].delete_many({'day': today})
            month = time.strftime("%m", time.localtime())
            self._client[self._colCal].delete_many({'month': month})

    # 将数据写入DB
    def _updateDb(self, id, params, col='weather'):
        params['update_time'] = int(self._updateTime)
        #print(params)
        if col == 'weather':
            self._client[self._col].update_one({"_id": id}, {"$set": params}, upsert=True)
        else:
            self._client[self._colCal].update_one({"_id": id}, {"$set": params}, upsert=True)

    def spiderWeather(self):
        cityAll = self._client[self._colCity].find({'parent': {'$ne': 'china'}})
        today = time.strftime("%Y%m%d", time.localtime())
        c = 0
        for cityInfo in cityAll:
            print('start ......')
            id = cityInfo['_id'] + '_' + today
            weaInfo = {
                'day': today,
                'city': cityInfo['_id']
            }
            soup = BeautifulSoup(urlopen(cityInfo['url']), 'html.parser')  # parser 解析
            # 位置
            weaInfo['location'] = soup.find('div', class_='search_default').em.text.strip()
            weaAlert = soup.find('div', class_='wea_alert').find_all('li')
            # 空气质量
            weaInfo['quality'] = weaAlert[0].em.text.strip()
            # 风力预警
            if len(weaAlert) >= 2:
                weaInfo['wind_alert'] = weaAlert[1].em.text.strip()
            else:
                weaInfo['wind_alert'] = ''
            #print(weaInfo)
            # 当前温度
            weaDiv = soup.find('div', class_='wea_weather')
            weaInfo['temp'] = weaDiv.em.text.strip()
            # 天气
            weaInfo['wea'] = weaDiv.img.attrs['alt'].strip()
            weaInfo['wea_img'] = weaDiv.img.attrs['src'].strip()
            # 最后更新时间
            weaInfo['last_update'] = weaDiv.strong.text.strip()
            aboutDiv = soup.find('div', class_='wea_about')
            # 湿度
            weaInfo['humidity'] = aboutDiv.span.text.strip()
            # 风力
            weaInfo['wind'] = aboutDiv.em.text.strip()
            # 天气提示
            weaInfo['tips'] = soup.find('div', class_='wea_tips').em.text.strip()
            # 预报
            preWea = {}
            days = soup.find_all('ul', class_='days')
            i = 0
            for day in days:
                li = day.find_all('li')
                preDic = {}
                k = ['today', 'tomorrow', 'after_tomorrow'][i]
                preDic['day'] = li[0].a.text.strip()  # 今天，明天，后天
                preDic['wea'] = li[1].text.strip()  # 天气
                preDic['temp'] = li[2].text.strip()  # 温度
                preDic['wind'] = li[3].em.text.strip()  # 风向
                preDic['wind_level'] = li[3].b.text.strip()  # 风力
                preDic['quality'] = li[4].text.strip()  # 空气质量
                preWea[k] = preDic
                i += 1
            weaInfo['pre_weather'] = preWea
            # print(weaInfo)
            self._updateDb(id, weaInfo)

            # 天气日历
            calSoup = soup.find(id='calendar_grid').find_all('li', class_='item')
            for cal in calSoup:
                if cal.em and cal.img and cal.find_all('p'):
                    weaCal = {}
                    weaCal['city'] = cityInfo['_id']
                    weaCal['month'] = time.strftime("%m", time.localtime())
                    weaCal['day'] = cal.em.text.strip()
                    weaCal['weather'] = cal.img.attrs['alt'].strip()
                    weaCal['temp'] = cal.find_all('p')[0].text.strip()
                    weaCal['wind'] = cal.find_all('p')[0].text.strip()
                    id = cityInfo['_id'] + '_' + time.strftime("%Y%m", time.localtime()) + weaCal['day']
                    # print(weaCal)
                    self._updateDb(id, weaCal, 'weather_calendar')
            c += 1
            #s = random.randint(1, 3)
            s = 1
            time.sleep(s)
            print(cityInfo['name'], c, 'sleep=' + str(s))
            #break

if __name__ == '__main__':
    spider = mojiSpiderCity()
    spider.spiderWeather()

