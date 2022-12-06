# Write python code to read camera data via picamera2 and detect faces with opencv.
import picamera2
import cv2

# Create a Picamera object
camera = picamera2.PiCamera()

# Start the camera and capture video
camera.start_preview()

# Set up OpenCV to capture video from the camera
capture = cv2.VideoCapture(0)

# Load the cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Read a frame from the camera
    ret, frame = capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the frame with the detected faces
    cv2.imshow('Camera', frame)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy the window
capture.release()
cv2.destroyAllWindows()