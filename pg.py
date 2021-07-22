a = 0
aList = list()

while(True):
    a = float(input(">> "))
    if a != -1:
        aList.append(a)
    else:
        b =float(input(">> "))
        break

for a in aList:
    print(a*b)