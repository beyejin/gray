import cv2
import time

# Start webcam
cap = cv2.VideoCapture(0)  # Change 0 to the appropriate index if multiple webcams are connected

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Wait for 5 seconds before capturing
start_time = time.time()
while time.time() - start_time < 5:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the captured frame
    cv2.imshow('Webcam Capture', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Load the pre-trained Haar Cascade classifier for frontal faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the image from the webcam capture
img = cv2.imread('Webcam Capture.jpg')

# Detect faces in the image using the detectMultiScale method
# Parameters: scaleFactor, minNeighbors, minSize
faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Iterate over detected faces and print their positions
for (x, y, w, h) in faces:
    print(f"Detected face position: x={x}, y={y}, width={w}, height={h}")

# Display the original image with rectangles around detected faces
cv2.imshow('detected face', img)

# Wait for a key press and then close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()