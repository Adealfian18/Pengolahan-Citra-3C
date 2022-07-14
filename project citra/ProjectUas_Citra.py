import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

#* read image
image = cv2.imread('daun.jfif')

# convert to grayscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# applying gaussian blur
blurred = cv2.GaussianBlur(grey, (3, 3), 0)

# thresholdin: Otsu's Binarization method
_, thresh1 = cv2.threshold(blurred, 127, 255,
                            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# show thresholded image

image = cv2.imread("daun.jfif")

# TODO : tuple untuk warna dari garis histogram
colors = ("red", "green", "blue")
chanel_ids = (0, 1, 2)

# TODO : membuat histogram berwarna
plt.figure()
plt.xlim([0, 256])

for channel, color in zip(chanel_ids, colors):
    histogram, bins = np.histogram(image[:, :, channel], bins=256, range=(0, 256))
    plt.plot(bins[:-1], histogram, color=color)
    
plt.title("Histogram")
plt.xlabel("Color Value")
plt.ylabel("Pixel Count")

# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blurred,cv2.CV_64F)

# But this tends to localize the edge towards the brighter side.
laplacian1 = laplacian/laplacian.max()

cv2.imshow("image", image)
cv2.imshow("Greyscale", grey)
cv2.imshow('Thresholded', thresh1)
cv2.imshow('LoG',laplacian1)
plt.show()   

cv2.waitKey(0)
