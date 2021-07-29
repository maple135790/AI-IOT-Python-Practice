import math

def sigmoid(x):
    sig = 1 / (1+math.exp(-x))
    return sig

class Weight:
    hn1 = [2.04616, 4.95659, -6.79302, -13.1236]
    hn2 = [-1.08756, 8.08309, -6.73166, -13.4051]
    setosa = [-0.00052, 1.00052]
    versicolor = [1.01335, -1.00449]
    virginica = [-1.01267, 0.00388]

class Bias:
    hn1 = 28.5359
    hn2 = -0.96226
    setosa = 0.00002
    versicolor = -0.0089
    virginica = 1.00879

X = [float(input('>> ')), 
     float(input('>> ')),
     float(input('>> ')), 
     float(input('>> '))]

hiddenNodes = list()
hn1R = 0
hn2R = 0
for i in range(len(X)):
    hn1R += X[i]*Weight.hn1[i]
    hn2R += X[i]*Weight.hn2[i]
hiddenNodes.append(sigmoid(hn1R+Bias.hn1))
hiddenNodes.append(sigmoid(hn2R+Bias.hn2))

seR = 0
veR = 0
viR = 0
for i in range(len(hiddenNodes)):
    seR += hiddenNodes[i]*Weight.setosa[i]
    veR += hiddenNodes[i]*Weight.versicolor[i]
    viR += hiddenNodes[i]*Weight.virginica[i]
setosa = sigmoid(seR+Bias.setosa)
versicolor = sigmoid(veR+Bias.versicolor)
virginica = sigmoid(viR+Bias.virginica)

print()

if max([setosa, versicolor, virginica]) == setosa:
    print('setosa')
elif max([setosa, versicolor, virginica]) == versicolor:
    print('versicolor')
else:
    print('virginica')
