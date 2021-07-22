import math
import pandas as pd
from sklearn import linear_model

class Data:
    def __init__(self, x1, x2, cls):
        self.x1 = x1
        self.x2 = x2
        self.cls = cls


df = pd.read_csv('.\\0721\\values.csv', delimiter=',')
dataList = list()
for i in range(len(df)):
    dataList.append(Data(x1=df.iloc[i]['x1'],
                         x2=df.iloc[i]['x2'],
                         cls=df.iloc[i]['Class']))

x = [[d.x1, d.x2] for d in dataList]
x_test = x[math.floor(len(x)/2):]
x_pred = x[:math.floor(len(x)/2)]


clsf = [1.0 if(d.cls == "Good") else -1.0 for d in dataList]
clsf_test = clsf[math.floor(len(clsf)/2):]
clsf_pred = clsf[:math.floor(len(clsf)/2)]  # true condition


model = linear_model.LinearRegression()
model.fit(x_test, clsf_test)
y_pred = model.predict(x_pred)
y_pred = [1.0 if yp > 0 else -1.0 for yp in y_pred]  # predicted condition

print(model.coef_)
print(model.intercept_)
print(y_pred)
print(clsf_pred)

truePositive = 0
trueNegative = 0
falseNegative = 0
falsePositive = 0
for i in range(len(y_pred)):
    truePositive += 1 if (y_pred[i] == 1 and clsf_pred[i] == 1) else 0
    falsePositive += 1 if (y_pred[i] == 1 and clsf_pred[i] == -1) else 0
    falseNegative += 1 if (y_pred[i] == -1 and clsf_pred[i] == 1) else 0
    trueNegative += 1 if (y_pred[i] == -1 and clsf_pred[i] == -1) else 0

print(truePositive/len(y_pred),
      falseNegative/len(y_pred),
      falsePositive/len(y_pred),
      trueNegative/len(y_pred))

print(truePositive,
      falseNegative,
      falsePositive,
      trueNegative)
