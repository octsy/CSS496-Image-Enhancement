import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread('output_piecewise.jpg',0)
x,y=image.shape
z=np.zeros((x,y))
for i in range(0,x):
    for j in range(0,y):
        if(image[i][j]>50 and image[i][j]<150):
            z[i][j]=255
        else:
            z[i][j]=0
equ=np.hstack((image,z))
plt.title('Original\Graylevel slicing w/o background')
plt.imshow(equ,'gray')
plt.show()