import sys
import os
import cv2

desc = '''Script to gather data images with a particular label.

Usage: python gather_images.py <label_name> <num_samples>

The script will collect <num_samples> number of images and store them
in its own directory.

Only the portion of the image within the box displayed
will be captured and stored.

Press 'a' to start/pause the image collecting process.
Press 'q' to quit.

'''

try:
    labels = sys.argv[1]
    number = int(sys.argv[2])
except:
    print('Argument missing')
    print(desc)
    print(exit(-1))

IMAGE_PATH = 'image_data'
IMAGE_CLASS_PATH = os.path.join(IMAGE_PATH, labels)

try:
    os.mkdir(IMAGE_PATH)
except FileExistsError:
    pass

try:
    os.mkdir(IMAGE_CLASS_PATH)
except FileExistsError:
    print('{} directory exist already')
    print('The images will be saved in the directory')

start = False
count = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    if count == number:
        break

    cv2.rectangle(frame, (0, 70), (250, 300), (255, 255, 255), 2)

    if start:
        roi = frame[70:300, 0:250]
        path = os.path.join(IMAGE_CLASS_PATH, "{}.jpg".format(count + 1))
        img = cv2.imwrite(path, roi)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),
                (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(1)
    if k == ord('a'):
        start = not start

    if k == ord('q'):
        break

print("{} images have be saved to {}".format(count, labels))

cap.release()
cv2.destroyAllWindows()
