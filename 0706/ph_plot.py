import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import json

# 每日酸雨pH值
# https://opendata.cwb.gov.tw/index

with open(".\\0706\\json\\O-A0004-001.json", 'r')as f:
    rawJson = json.load(f)
    tpeData = list()
    monthData = list(rawJson['cwbopendata']['dataset']['weatherElement'])
    for md in monthData:
        for lmd in md['location']:
            if lmd['locationName'] == '台北' or lmd['locationName'] == '臺北':
                tpeData.append(lmd)
                break

    tpeDict = defaultdict(dict)
    for tpeMonthData in tpeData:
        for t in tpeMonthData['time']:
            # str(t['dataTime']).split('-')[1] is month
            # str(t['dataTime']).split('-')[2] is date
            value = t['value'] if((t['value'] != '-')
                                  and (t['value'] != None)) else 0
            tpeDict[str(t['dataTime']).split('-')[1]
                    ][str(t['dataTime']).split('-')[2]] = value

    i = 1
    for month in tpeDict:
        tmp = plt.subplot(2, 4, i)
        days = list(int(k) for k in tpeDict[month].keys())
        ph = list(float(p) for p in tpeDict[month].values())
        tmp.plot(days, ph)
        tmp.set_title(month)
        i += 1
    plt.suptitle('台北每月每日酸雨pH值', fontname="Source Han Sans TW")
    plt.show()
