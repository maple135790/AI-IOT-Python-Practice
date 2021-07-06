import json
import matplotlib.pyplot as plt
import math

# 每日雨量-局屬地面測站每日雨量資料
# https://opendata.cwb.gov.tw/index

def rainPlot(location: str = '臺北', showsAll: bool = False):
    with open('.\\0706\\json\\C-B0025-001.json', 'r') as f:
        rawData = json.load(f)
        locations = rawData['cwbdata']['resources']['resource']['data']['surfaceObs']['location']
        if not showsAll:
            for l in locations:
                if l['station']['stationName'] == location:
                    station = l
                    break
                else:
                    station = {}
            if(bool(station)):
                locationMonthRain = station['stationObsStatistics']['precipitation']['monthly']

                month = []
                monthRain = []
                for t in locationMonthRain:
                    month.append(int(t['dataYearMonth'][-2:]))
                    # if axis's value is not numeric, it'll be wierd
                    monthRain.append(float(t['total']))
                plt.title(label='{}測站月雨量資料'.format(location),
                          fontname="Source Han Sans TW")
                plt.plot(month, monthRain, 'go-')
                plt.show()
        else:
            colCount = math.ceil(len(locations)/4)
            plotCount = 1
            for l in locations:
                stationName = l['station']['stationName']
                locationMonthRain = l['stationObsStatistics']['precipitation']['monthly']

                month = []
                monthRain = []
                for t in locationMonthRain:
                    _rain = t['total'] if(t['total'] != 'T') else 0
                    month.append(int(t['dataYearMonth'][-2:]))
                    # if axis's value is not numeric, it'll be wierd
                    monthRain.append(float(_rain))
                tmp = plt.subplot(colCount, 4, plotCount)
                tmp.set_title(stationName, fontname="Source Han Sans TW")
                tmp.plot(month, monthRain, 'go-')
                plotCount += 1
            plt.suptitle('局屬地面全測站每月雨量資料', fontname="Source Han Sans TW")
            plt.show()


if(__name__ == '__main__'):
    rainPlot(showsAll=True)
