from __future__ import (absolute_import,division,
                        print_function,unicode_literals)
try:
    # Python 2.x版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x版本
    from urllib.request import urlopen 
import json
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# # 读取数据
# req = response.read()
# # 将数据写入文件
# with open('btc_close_2017_urllib.json','wb') as f:
#     f.write(req)
# # 加载json格式
# file_urllib = json.loads(req) 
# print(file_urllib)



# import requests
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url) 
# # 将数据写入文件
# with open('btc_close_2017_request.json','w') as f:
#     f.write(req.text) 
# file_requests = req.json() 


# print(file_urllib == file_requests)


import json

file_name='btc_close_2017_request.json'
with open (file_name) as f:
    json_data=json.load(f)


# [{
#     "date": "2017-01-01",
#     "month": "01",
#     "week": "52",
#     "weekday": "Sunday",
#     "close": "6928.6492"
# },
# {
#     "date": "2017-01-02",
#     "month": "01",
#     "week": "1",
#     "weekday": "Monday",
#     "close": "7070.2554"
# },
    
    dates = []
    months = []
    weeks = []
    weekdays = []
    closes =[]
    for btc_dict in json_data:
        date=btc_dict['date']
        dates.append(date)
        month=int(btc_dict['month'])
        months.append(month)
        week=int(btc_dict['week'])
        weeks.append(week)
        weekday=btc_dict['weekday']
        weekdays.append(weekday)
        close=int(float(btc_dict['close']))
        closes.append(close)
        # print("{} is momoth {} week {} ,{} ,the close price is {} RMB".format(date,month,week,weekday,close))

import pygal
import math
line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = '收盘价(¥)'
line_chart.x_labels = dates
N = 20
closes_log = [math.log10() for _ in closes]
line_chart.x_labels_major = dates[::N]
line_chart.add('log收盘价',closes_log)
line_chart.render_to_file("收盘价对数变换折线图.svg")


# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)  # ①
# line_chart.title = '收盘价（¥）'
# line_chart.x_labels = dates
# N = 20  # x轴坐标每隔20天显示一次
# line_chart.x_labels_major = dates[::N]  # ②
# line_chart.add('收盘价', closes)
# line_chart.render_to_file('收盘价折线图（¥）.svg')