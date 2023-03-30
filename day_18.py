# IMAGE BLENDING USING IMAGE PYRAMIDS

import cv2
import numpy as np
import matplotlib.pyplot as plt

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

apple = cv2.resize(apple,(512,512))
orange = cv2.resize(orange,(512,512))

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:,:256],orange[:,256:]))
plt.imshow(apple_orange[:,:,::-1])
cv2.imshow('img',apple_orange[:,:,::-1])

# generata gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6) :
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6) :
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate laplacian pyrmaid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in  range(5,0,-1) :
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    # print(gp_apple[i - 1].shape)
    # print(gaussian_expanded.shape)
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_expanded)
    lp_apple.append(laplacian)

# generate laplacian pyrmaid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in  range(5,0,-1) :
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    # print(gp_apple[i-1].shape)
    # print(gaussian_expanded.shape)
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)

# now add left and right halves of iamge in each level
apple_orange_pyramid = []
n= 0
for apple_lap,orange_lap in zip(lp_apple,lp_orange) :
    n+=1
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6) :
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)

cv2.imshow('final image',apple_orange_reconstruct)
# cv2.imwrite('blended_apple_orange.jpg',apple_orange_reconstruct)


cv2.waitKey(0)
cv2.destroyAllWindows()