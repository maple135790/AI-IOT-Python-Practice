import cv2
import numpy as np
import matplotlib.pyplot as plt

inImage =cv2.imread(".\\0727\\license_plate.bmp",0)

grad_X =cv2.Sobel(inImage,cv2.CV_16S,1,0)
grad_y =cv2.Sobel(inImage,cv2.CV_16S,0,1)

abs_grad_x =cv2.convertScaleAbs(grad_X)
abs_grad_y =cv2.convertScaleAbs(grad_y)

print(abs_grad_x.shape)
print(abs_grad_y.shape)

grad_image =cv2.addWeighted(abs_grad_x ,1.0,abs_grad_y,1.0,0)

thrv, sobelImage=cv2.threshold(grad_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


inImage =cv2.cvtColor(inImage,cv2.COLOR_BGR2RGB)
sobelImage =cv2.cvtColor(sobelImage,cv2.COLOR_BGR2RGB)

fig ,ax =plt.subplots(1,2)
fig.suptitle("sobel algo",fontsize =16)
ax[0].set_title("input")
ax[0].imshow(inImage)
ax[1].set_title("output")
ax[1].imshow(sobelImage)

plt.show()