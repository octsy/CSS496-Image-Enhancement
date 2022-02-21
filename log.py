from GLT import GLT
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('lumbar.jpg')
transform = 'log'
coeff = 6
gamma = 2.5

out_img = GLT(img, transform, coeff = coeff , gamma = gamma)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('Input image', fontsize=12)
plt.axis("off")

plt.subplot(122)
plt.imshow(out_img, 'gray')
plt.title('Output image', fontsize=12)
plt.axis("off")
plt.show()