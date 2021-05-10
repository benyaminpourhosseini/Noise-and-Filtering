import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255 #map digits between (0, 1)

# creating a box filter
m1, m2, m3 = 5, 9, 15 # choose filter size

# create an m by m box filter
F1 = np.ones((m1,m1), np.float64)/(m1*m1)
F2 = np.ones((m2,m2), np.float64)/(m2*m2)
F3 = np.ones((m3,m3), np.float64)/(m3*m3)

# Now, filter the image
J1 = cv2.filter2D(I,-1, F1)#when we choose depth = -1, the depth of 				   #output chosen automatically
J2 = cv2.filter2D(I,-1, F2)
J3 = cv2.filter2D(I,-1, F3)

cv2.imwrite('Filter size is 5.jpg',J1*255)
cv2.imwrite('Filter size is 9.jpg',J2*255)
cv2.imwrite('Filter size is 15.jpg',J3*255)

cv2.imshow('Filter size is 5',J1)
cv2.waitKey()
cv2.imshow('Filter size is 9',J2)
cv2.waitKey()
cv2.imshow('Filter size is 15',J3)
cv2.waitKey()

m = 5
J4 = cv2.blur(I, (m, m))
cv2.imshow('we use cv2.blur instead of cv2.filter2D', J4)
cv2.waitKey()


cv2.destroyAllWindows()
