import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('output_piecewise.jpg',0)
plt.hist(img.ravel(),256,[0,256]) 

plt.show() 
plt.savefig('./hist-img/hist.png')

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

cv2.imshow('Equalized Image',res)
cv2.imwrite('./hist-img/Equalized Image.png',res)

plt.hist(res.ravel(),256,[0,256]) 

plt.show() 
plt.savefig('./hist-img/equal-hist.png')