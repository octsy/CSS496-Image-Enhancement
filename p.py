import cv2
import random
import imutils
import numpy as np

# Each pixel value of a color image is [x,y,z], Each pixel value of gray image is one np.uint8
image = cv2.imread('lumbar.jpg')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Turn a color image into a grayscale image （RGB The color turns grey ）


# Image resizing
ori_h, ori_w = image.shape[:2] # Get the length and width of the original image
height, width = gray_img.shape[:2] # Get the length and width of the gray image
image = cv2.resize(image, (int(ori_w / ori_h * 400), 400), interpolation=cv2.INTER_CUBIC) # Transform the image size and interpolate it three times
gray_img = cv2.resize(gray_img, (int(width / height * 400), 400), interpolation=cv2.INTER_CUBIC) # Transform the image size and interpolate it three times


# a<0 and b=0: The bright areas of the image darken , Dark areas brighten
a, b = -0.5, 0
new_img1 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8) # Initialize a new image for transformation , And the size is the same as the gray image size
for i in range(new_img1.shape[0]):
    for j in range(new_img1.shape[1]):
        new_img1[i][j] = gray_img[i][j] * a + b # original image *a+b


# a>1: Enhance the contrast of the image , The image looks clearer
a, b = 1.5, 20
new_img2 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img2.shape[0]):
    for j in range(new_img2.shape[1]):
        if gray_img[i][j] * a + b > 255:
            new_img2[i][j] = 255
        else:
            new_img2[i][j] = gray_img[i][j] * a + b


# a<1: Reduces the contrast of the image , The image looks dark
a, b = 0.5, 0
new_img3 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img3.shape[0]):
    for j in range(new_img3.shape[1]):
        new_img3[i][j] = gray_img[i][j] * a + b


# a=1 And b≠0, The gray value of the whole image moves up or down , That is to say, the whole image becomes bright or dark , Does not change the contrast of the image
a, b = 1, -50
new_img4 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img4.shape[0]):
    for j in range(new_img4.shape[1]):
        pix = gray_img[i][j] * a + b
        if pix > 255:
            new_img4[i][j] = 255
        elif pix < 0:
            new_img4[i][j] = 0
        else:
            new_img4[i][j] = pix


# a=-1, b=255, Image reversal
new_img5 = 255 - gray_img
cv2.imshow('origin', imutils.resize(image, 800))
cv2.imshow('gray', imutils.resize(gray_img, 800))
cv2.imshow('a<0 and b=0', imutils.resize(new_img1, 800))
cv2.imshow('a>1 and b>=0', imutils.resize(new_img2, 800))
cv2.imshow('a<1 and b>=0', imutils.resize(new_img3, 800))
cv2.imshow('a=1 and b><0', imutils.resize(new_img4, 800))
cv2.imshow('a=-1 and b=255', imutils.resize(new_img5, 800))
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()