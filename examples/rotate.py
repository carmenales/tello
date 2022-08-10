from djitellopy import Tello

# Connect
tello = Tello()
tello.connect()

# Take off
tello.takeoff()

# Rotate
tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(90)

# Land
tello.land()
