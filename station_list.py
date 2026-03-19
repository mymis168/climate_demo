from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms


# 建立座標
loc = ms.Point(24.19352298812673, 120.66940049145083)
sv = ms.Point(37.39322970859948, -121.5466194773837)

slist = ms.stations.nearby(sv,limit=3)

print("在指定座標附近的偵測點如下: ")
print( slist )