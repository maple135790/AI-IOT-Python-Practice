import cv2
import numpy as np
from MNISTDataset import MNISTDataset

mnist_train =MNISTDataset('.\\0728\\train-images.idx3-ubyte',
                          '.\\0728\\train-labels.idx1-ubyte')

winSize = (28,28)
blockSize = (28,28)
blockStride = (1,1)
cellSize = (14,14)
nbins = 9

HOG = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)

n_train =len(mnist_train)

trainImageMat =np.zeros((n_train,36),dtype =np.float32)
trainLabelMat =np.zeros((n_train),dtype =int)

for i in range(n_train):
  # get an item
  image ,label =mnist_train.getitem(i)

  # apply HOG Desciptor
  a_hog =HOG.compute(image)
  a_hog =a_hog.reshape(-1)
  a_hog =a_hog.astype(np.float32)
  
  trainImageMat[i] =a_hog
  trainLabelMat[i] =label

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 10000, 1e-6))

svm.train(trainImageMat,cv2.ml.ROW_SAMPLE,trainLabelMat)

mnist_test =MNISTDataset('.\\0728\\t10k-images.idx3-ubyte',
                          '.\\0728\\t10k-labels.idx1-ubyte')

n_test =len(mnist_test)
n_correct =0
n_wrong =0

for i in range(n_test):
  image ,label =mnist_test.getitem(i)

  a_hog =HOG.compute(image)
  a_hog =a_hog.reshape((1,-1))
  a_hog =a_hog.astype(np.float32)

  result =svm.predict(a_hog)
  result =int(result[1])

  if (result ==label):
    n_correct +=1
  else:
    n_wrong +=1

accuracy =n_correct /n_test
print('accuracy','{:.2f}'.format(accuracy))