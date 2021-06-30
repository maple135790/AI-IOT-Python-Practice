# 1. 使用random模組與迴圈，模擬擲骰子10000次，然後統計每一個數字出現的次數與機率。
import random as rand

store = {}
for i in range(10000):
    point = rand.randint(1, 6)
    if store.get(point) != None:
        store[point] += 1
    else:
        store[point] = 1
        
for p in store:
    print('{}: {} times, {}'.format(p, store[p], store[p]/10000))