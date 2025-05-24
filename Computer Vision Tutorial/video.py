# import cv2
# import matplotlib.pyplot as plt
#
# cap = cv2.VideoCapture('C:/Users/Aniket/Downloads/vid.mp4')
# while True:
#     flag,frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0XFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()




























import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('C:/Users/Aniket/Downloads/vid.mp4')

frame_width = int(cap.get(3))
frame_height= int(cap.get(4))

size = (frame_width,frame_height)

results = cv2.VideoWriter('saved.avi',
                          cv2.VideoWriter_fourcc(*'MJPG'),
                          50,size)



while True:
    ret, frame = cap.read()

    if ret == True:

        results.write(frame)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break
cap.release()
results.release()
cv2.destroyAllWindows()
