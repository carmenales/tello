from djitellopy import Tello
import time, cv2
from threading import Thread

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# Connect
tello = Tello()
tello.connect()

# Keep record video
keepRecording = True

# Turn on video streaming.
tello.streamon()

# Get the BackgroundFrameRead object from the camera drone
frame_read = tello.get_frame_read()

# Run the recorder in a seperate thread, otherwise blocking options
# would prevent frames from getting added to the video
recorder = Thread(target=videoRecorder)
recorder.start()

# Move
tello.takeoff()
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()

# Stop record
keepRecording = False
recorder.join()
