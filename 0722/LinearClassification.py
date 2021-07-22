import pandas
import numpy
from sklearn import linear_model
from sklearn.metrics import r2_score #
import matplotlib.pyplot as plt

df = pandas.read_csv("classdata2.csv")

X = df[['x1', 'x2']]
y = df['Class']
print(type(y))

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
print(regr.intercept_)


print(regr.predict(X))

def checkV(x):
    if x>0:
        return 1
    elif x<0:
        return -1
result = list(map(checkV,regr.predict(X)))

print("分類的結果:")
print(result)
print()


print("實際的分類:")      
str1=""
for s in y:
  str1=str1 + str(s)+"," + " "

  
print(str1) 