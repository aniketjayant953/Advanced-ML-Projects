import matplotlib.pyplot as plt
import cv2

# create an object to read from camera
video = cv2.VideoCapture(0)

# we need to check if camera is opened previously or not
if (video.isOpened()==False):
    print("Error reading video file")

# we need to set the resolution. So, convert them from float to interger
frame_width  = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width,frame_height)

# Below VideoWriter object will create a frame of above defined resolution
# The output is stored in 'filename.avi' file
result = cv2.VideoWriter('saved_video.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while(True):
    ret, frame = video.read()

    if ret == True:

        # Write the frame into the file 'qfilename.avi'
        result.write(frame)

        # Display the frame saved in the file
        cv2.imshow('Frame', frame)

        # Press S on the keyboard to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    # break the loop
    else:
        break

# When everything done, release the video capture and video write objects
video.release()
result.release()

#Closes all the frames
cv2.destroyAllWindows()

print("The Video was successfully saved")









