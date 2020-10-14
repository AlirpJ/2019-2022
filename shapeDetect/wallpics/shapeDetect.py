import cv2
import numpy as np
img = cv2.imread("wallPic.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("wallPic",img)
cv2.waitKey(0)
cv2.destroyAllWindows
print("Hello World")