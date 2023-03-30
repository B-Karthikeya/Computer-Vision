import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('parrot.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# reshape image to a 2D array pixels and 3 color code values(RGB)
pixel_values = image.reshape((-1,3))
print(pixel_values)

pixel_values = np.float32(pixel_values)
print(pixel_values.shape)

# define stop iteration
criteria  = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,100,0.2)

# number of clusters
k=6
_,labels,(centers) = cv2.kmeans(pixel_values,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# convert back to 8 bit values
cneters = np.uint8(centers)

# flatten the labels array
labels = labels.flatten()

# convert all pixels to color of the cnetroid
segmented_image = centers[labels.flatten()]

# reshape back to the original image dimensions
segmented_image = segmented_image.reshape(image.shape)

# show the image
plt.imshow(segmented_image)
plt.show()