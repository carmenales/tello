from djitellopy import Tello

# Connect
tello = Tello()
tello.connect()

# Take off
tello.takeoff()

# tello.go_xyz_speed(x,y,z, speed)
# x - (+)foward/(-)backwards
# y - (+)left/(-)right
# z - (+)up/(-)down

# Forward, Right, Up
tello.go_xyz_speed(30,-30,30, 20)

# Backwards, Left, Down
tello.go_xyz_speed(-60,60,-60, 20)

# Forward, Right, Up
tello.go_xyz_speed(30,-30,30, 20)

# Land
tello.land()
