import cv2
from matplotlib import pyplot as plt
import numpy as np

img_OpenCV = cv2.imread('logo.png')

b,g,r = cv2.split((img_OpenCV))

img_matplotlib = cv2.merge([r,g,b])

plt.subplot(121)
plt.imshow(img_OpenCV)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()


cv2.imshow("Img OpenCV",img_OpenCV)
cv2.imshow("Img Matplotlib",img_matplotlib)

img_concatenate = np.concatenate((img_OpenCV,img_matplotlib),axis=1)
cv2.imshow('Merged Image',img_concatenate)


cv2.waitKey(0)
cv2.destroyAllWindows()

#get the channels with a different aproach
#B = img_OpenCV[:,:,0]
#G = img_OpenCV[:,:,1]
#R = img_OpenCV[:,:,2]

#Transform BGR to RGB using Numpy
#img_matplotlib = img_OpenCV[:,:,::-1]
