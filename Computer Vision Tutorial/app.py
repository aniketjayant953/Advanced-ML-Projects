import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/Aniket/Downloads/car.png')
# image2=image.copy()
# image3=image.copy()
#
# rectangle = cv2.rectangle(image2,(620,60),(300,300),(0,255,0),2)
# text= cv2.putText(image3,"This is Tiger",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


# cv2.imshow('frame',text)
# cv2.imshow('frame2',rectangle)
cv2.imshow('frame2',image)


cv2.waitKey(0) # for showing image for long time
cv2.destroyAllWindows()

