import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("output_power.jpg",cv2.IMREAD_GRAYSCALE)
row ,col = img.shape
def binaryconvt(img) :
    list = []
    for i in range(row):
        for j in range(col):
             list.append (np.binary_repr( img[i][j] ,width=8  ) )
    return list 
im1 = binaryconvt(img)
def bitplane(bitimgval , img1D ):
    bitList = [int(i[bitimgval])for i in img1D]
    return bitList

bit8 = np.array( bitplane(0,im1 ) ) * 256
bit7 = np.array( bitplane(1,im1) ) * 128

bit6 = np.array( bitplane(2,im1 ) ) * 64
bit5 = np.array( bitplane(3,im1) ) * 32

bit4 = np.array( bitplane(4,im1) ) * 16
bit3 = np.array( bitplane(5,im1) ) * 8
bit2 = np.array( bitplane(6,im1) ) * 4
bit1 = np.array( bitplane(7,im1) ) * 2
#bit0 = np.array( bitplane(8,im1) ) * 1


combine2 = bit8 + bit7 + bit6 + bit5
comb2 = np.reshape(combine2,(row,col))
cv2.imwrite("comb(all).jpeg",comb2)

bit8 = np.reshape(bit8,(row,col))
cv2.imwrite("./bit-pland-img/8bit.jpg" , bit8 )


bit7 = np.reshape(bit7,(row,col))
cv2.imwrite("./bit-pland-img/7bit.jpg",bit7)


bit6 = np.reshape(bit6,(row,col))
cv2.imwrite("./bit-pland-img/6bit.jpg",bit6)


bit5 = np.reshape(bit5,(row,col))
cv2.imwrite("./bit-pland-img/5bit.jpg",bit5)


bit4 = np.reshape(bit4,(row,col))
cv2.imwrite("./bit-pland-img/4bit.jpg",bit4)

bit3 = np.reshape(bit3,(row,col))
cv2.imwrite("./bit-pland-img/3bit.jpg",bit3)

bit2 = np.reshape(bit2,(row,col))
cv2.imwrite("./bit-pland-img/2bit.jpg",bit2)

bit1 = np.reshape(bit1,(row,col))
cv2.imwrite("./bit-pland-img/1bit.jpg",bit1)


cv2.destroyAllWindows()