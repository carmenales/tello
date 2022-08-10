from djitellopy import Tello
import time

# Connect
tello = Tello()
tello.connect()

# Take off
tello.takeoff()

# Flip 
time.sleep(1)
tello.flip_right()
time.sleep(1)
tello.flip_left()
time.sleep(1)

# Land
tello.land()
