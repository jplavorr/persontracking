import cv2
import time


# Take from camera
cap = cv2.VideoCapture(0)

# Track Time
starting_time = time.time()

while True:
     #Display frame
     ret, frame = cap.read()
     height, width, channels = frame.shape
     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     cv2.imshow("Frame", frame)
    # The frame stops after the code run, so the code bellow make the window stay longer
    #key 0: freeze until press key
    #key 1: change after 1 second
     key = cv2.waitKey(1)
     if key == 27:
         break

cap.release()
cv2.destroyAllWindows()