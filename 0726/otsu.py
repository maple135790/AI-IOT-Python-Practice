import cv2
import matplotlib.pyplot as plt

inImage =cv2.imread(".\\0726\\lena.bmp",0)
thrv, otsuImage=cv2.threshold(inImage,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

inImage =cv2.cvtColor(inImage,cv2.COLOR_BGR2RGB)
otsuImage =cv2.cvtColor(otsuImage,cv2.COLOR_BGR2RGB)

fig ,ax =plt.subplots(1,2)
fig.suptitle("Otsu algo",fontsize =16)
ax[0].set_title("input")
ax[0].imshow(inImage)
ax[1].set_title("output")
ax[1].imshow(otsuImage)

plt.show()