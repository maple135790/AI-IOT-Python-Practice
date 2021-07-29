import pandas
import numpy
from sklearn import linear_model
from sklearn.metrics import classification_report, confusion_matrix

df = pandas.read_csv(".\\0722\\irisTwoClass.csv")

X = df[['SL', 'SW', 'PL', 'PW']]
y = df['Species']
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

print(type(y))
print(type(result))

print(classification_report(y,result,target_names=["Bad","Good"]))
conMtx=confusion_matrix(y,result)
print(conMtx)



