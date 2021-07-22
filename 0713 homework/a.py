import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

X = [[2], [3], [4]]
y = [5, 8, 9]
regr = linear_model.LinearRegression()
regr.fit(X, y)
xpred =np.linspace(0,8,50)
ypred =regr.predict([[d] for d in xpred])

plt.scatter(X, y)
plt.plot(xpred,ypred)
plt.show()
print(regr.coef_)
print(regr.intercept_)

prediction = regr.predict([[4]])
print(prediction)