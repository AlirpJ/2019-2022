import cv2
import numpy as np
count = 0

#img = cv2.imread("E:\CodeVS\wallpics\chessboardTest.jpg")           # img is set to the picture
img = cv2.imread("E:\CodeVS\wallpics\wallPic.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                       # imgRGB is img set to RGB simplistic
imgGrey = cv2.cvtColor(imgRGB,cv2.COLOR_RGB2GRAY)                   # imgGrey is imgRGB converted to grey

# Set threshhold for drawing contours and then draw them on imgGrey:
_, thrash = cv2.threshold(imgGrey, 220, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# Detect contours to find sticky notes
for contour in contours:
    print("!!!")
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img,[approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        print("Triangle detected!")
    elif len(approx) == 4:
        x ,y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        print("Rectangle detected!")
        count = count + 1
    else:
        
        cv2.putText(img, "unknown", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
print("Count = ",count)
cv2.imshow("wallPic",img)
cv2.waitKey(0)
cv2.destroyAllWindows