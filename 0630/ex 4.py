# 4. 將 1 到 1000之中的奇數累加起來，但是當累加值超過3000就不再累加。印出結果。
sum =0
for i in range(1,1001):
    if (sum <3000):
        sum +=i if i%2==1 else 0
    else:
        break
print(sum)