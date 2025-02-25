import cv2
import numpy as np
name ="car_parking.jpg"
img =cv2.imread("input/" + "car_parking.jpg")
img_copy = img.copy()

while True:
    cv2.imshow('C:\Users\ThinkPad\Downloads\car_parking.jpg' , img) # type: ignore
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
