#!/usr/bin/env python
#-*-coding:utf-8-*-
import json
import urllib


def get_weather(city):
    if city:
        url = 'http://sou.qq.com/online/get_weather.php?callback=Weather&city='
        city = urllib.quote(city)
        weather = json.loads(urllib.urlopen(url + city).read()[8:-2])
        date_list = [u'今', u'明', u'后']
        wea_city = weather['future']['name']
        wea_real = weather['real']['temperature']
        weather_result = u'%s天气:\n实时温度是%s摄氏度\n' % (wea_city, wea_real)
        for i in range(3):
            weather_result += u'%s天天气是%s,%s到%s摄氏度\n' % (
                date_list[i],
                weather['future']['wea_%s' % i],
                weather['future']['tmin_%s' % i],
                weather['future']['tmax_%s' % i])
        return weather_result
    else:
        return 'I don\'t know.'

if __name__ == '__main__':
    import platform
    sysstr = platform.system()
    cityname = None
    if sysstr == "Windows":
        info = u'请输入城市中文名:'
        info = info.encode('GBK')  # windows默认的是GBK字体
        cityname = raw_input(info)
        cityname = cityname.decode('GBK').encode('utf-8')
    elif(sysstr == "Linux"):
        cityname = raw_input('请输入城市中文名:')
    print(get_weather(cityname))
