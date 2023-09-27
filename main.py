import cv2
import mediapipe as mp
import time

# Load Face Detector 
face_detection = mp.solutions.face_detection.FaceDetection()
# Take from camera
cap = cv2.VideoCapture(0)

# Track Time
starting_time = time.time()

while True:
    #Take frame from camera
    ret, frame = cap.read()
    height, width, channels = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Draw Rectangle
    cv2.rectangle(frame, (0,0), (width, 70), (10, 10, 10), -1)

    #Face Detection
    results = face_detection.process(rgb_frame)
    #print(results.detections)
    
    
    #Is the face DETECTED?
    if results.detections:
        elapsed_time = int(time.time() - starting_time)
        #position on the screen, font, size, color, tickness

        if elapsed_time > 15: 
            # Reached Maximum Time
            cv2.rectangle(frame, (0,0), (width, height), (0, 0, 225), 10)
            # Window will pop up after 15 seconds
            cv2.setWindowProperty("Frame", cv2.WND_PROP_TOPMOST, 1)


        cv2.putText(frame, f"{elapsed_time}", (10, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 225, 0), 2)
        #print(f"Elapsed Time: {elapsed_time}") 
        print("Face looking at the screen")
    else:
        print("No Face")
        # Reset the Counter
        starting_time = time.time()
    
    #Display frame
    cv2.imshow("Frame", frame)
    # The frame stops after the code run, so the code bellow make the window stay longer
    #key 0: freeze until press key
    #key 1: change after 1 second
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()