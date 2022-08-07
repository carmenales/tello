from djitellopy import Tello
import cv2

# Connect
tello = Tello()
tello.connect()

# Take picture
tello.streamon()
frame_read = tello.get_frame_read()
tello.takeoff()

# Save picture
cv2.imwrite("picture.png", frame_read.frame)

# Land
tello.land()
