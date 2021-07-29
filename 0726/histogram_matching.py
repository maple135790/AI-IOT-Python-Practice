import cv2
import numpy as np
import matplotlib.pyplot as plt

inImage =cv2.imread(".\\0726\\lena.bmp",0)
tarImage =cv2.imread(".\\0726\\license_plate.bmp",0)

inHist = cv2.calcHist([inImage],[0],None,[256],[0,256])
inHist = inHist.reshape(256)

tarHist = cv2.calcHist([tarImage],[0],None,[256],[0,256])
tarHist = tarHist.reshape(256)

inHistogram =np.zeros((256), dtype =float)
for row in range(inImage.shape[0]):
  for col in range(inImage.shape[1]):
    gValue = inImage[row,col]
    inHistogram[gValue] =inHistogram[gValue] +1
  
for i in range(256):
  inHistogram[i] = inHistogram[i]/(inImage.shape[0] *inImage.shape[1])

tarHistogram =np.zeros((256), dtype =float)
for row in range(tarImage.shape[0]):
  for col in range(tarImage.shape[1]):
    gValue = tarImage[row,col]
    tarHistogram[gValue] =tarHistogram[gValue] +1
  
for i in range(256):
  tarHistogram[i] = tarHistogram[i]/(tarImage.shape[0] *tarImage.shape[1])

accInHistogram =np.zeros(256,dtype=float)
for i in range(255):
  accInHistogram[i+1] =accInHistogram[i]+inHistogram[i]

T =np.zeros(256,dtype=int)
for i in range(len(accInHistogram)):
  T[i] = int(255*accInHistogram[i])

accTarHistogram =np.zeros(256,dtype=float)
for i in range(255):
  accTarHistogram[i+1] =accTarHistogram[i]+tarHistogram[i]

G =np.zeros(256,dtype=int)
for i in range(len(accTarHistogram)):
  G[i] =np.round(255*accTarHistogram[i])
iG =np.zeros(256,dtype =int) 
for x_inv in range(256):
  for x in range(256):
    if x_inv <=G[x]:
      iG[x_inv] =x
      break

Z =np.zeros(256,dtype =int)
for x in range(256):
  y =T[x]
  Z[x] = iG[y]
 
outImage =np.zeros(inImage.shape,dtype =np.uint8)
print(np.shape(inImage))
print(np.shape(outImage))
for row in range(outImage.shape[0]):
  for col in range(outImage.shape[1]):
    gValue =inImage[row][col]
    outValue =Z[gValue]
    outImage[row][col] =outValue

outHist =cv2.calcHist([outImage],[0],None,[256],[0,256])
outHist =outHist.reshape(256)

inImage = cv2.cvtColor(inImage, cv2.COLOR_BGR2RGB)
tarImage = cv2.cvtColor(tarImage, cv2.COLOR_BGR2RGB)
outImage = cv2.cvtColor(outImage, cv2.COLOR_BGR2RGB)

fig,ax =plt.subplots(2,3)
fig.suptitle("Histogram matching",fontsize =16)
ax[0,0].set_title("input")
ax[0,0].imshow(inImage)
ax[0,0].axis()
ax[1,0].bar(range(inHist.shape[0]),inHist)
ax[0,1].set_title("matching image")
ax[0,1].imshow(tarImage)
ax[0,1].axis()
ax[1,1].bar(range(tarHist.shape[0]),tarHist)
ax[0,2].set_title("output")
ax[0,2].imshow(outImage)
ax[0,2].axis()
ax[1,2].bar(range(outHist.shape[0]),outHist)
plt.show()