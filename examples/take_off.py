from djitellopy import Tello

# Connect
tello = Tello()
tello.connect()

# Take off
tello.takeoff()

# Move
tello.move_left(20)
tello.rotate_counter_clockwise(90)
tello.move_forward(20)

# Land
tello.land()
