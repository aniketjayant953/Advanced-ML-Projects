import pytesseract
import cv2
import pandas

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Aniket\Tesseract-OCR\tesseract.exe"
path = r'C:\Users\Aniket\Downloads\essay.png'
img = cv2.imread(path)
cv2.imshow('sample image',img)

text = pytesseract.image_to_string(img)
# text = pytesseract.image_to_boxes(img)
# text=pytesseract.image_to_data(img,output_type="data.frame")
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(text))


