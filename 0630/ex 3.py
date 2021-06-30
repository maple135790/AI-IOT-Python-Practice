# 3. 將 1 到 1000之中的偶數累加起來。印出結果。
sum =0
for i in range(1,1001):
    sum +=i if i%2==0 else 0
print(sum)