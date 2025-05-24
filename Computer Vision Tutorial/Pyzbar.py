import cv2
import numpy as np
from pyzbar.pyzbar import decode
img=cv2.imread(r'C:\Users\Aniket\Downloads\barcode.jpg')
cv2.imshow('frame',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
code= decode(img)
print(code)
