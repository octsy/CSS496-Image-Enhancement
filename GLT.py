import numpy as np
import matplotlib.pyplot as plt
import cv2

def GLT(image, transform, coeff = 1.0 , gamma = 1.0):
    #built
    if transform == "negative":
        table = np.array([256-1-i for i in np.arange(0,256)]).astype("uint8")

    elif transform == "identity":
        table = np.array([i for i in np.arange(0,256)]).astype("uint8")

    elif transform == "log":
        table = np.array([10*coeff*(np.log10(1+i)) for i in np.arange(0,256)]).astype("uint8")

    elif transform == 'invlog':
        table = np.array([10*coeff/(np.log10(i+1)+1) for i in np.arange(0,256)]).astype("uint8")

    elif transform == "root":
        invGamma = 1.0/gamma
        table = np.array([coeff*((i/255.0) **invGamma)*255 for i in np.arange(0,256)]).astype("uint8")

    elif transform == "power" :
        table = np.array([coeff*((i/255.0)**gamma)*255 for i in np.arange(0,256)]).astype("uint8")



    return cv2.LUT(image, table)
