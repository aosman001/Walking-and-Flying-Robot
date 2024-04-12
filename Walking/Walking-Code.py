from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/cu.usbserial-1420", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
    servo8 = LX16A(8)

    servo1.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo2.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo3.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo4.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo5.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo6.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo7.set_angle_limits(0, 240)
    time.sleep(0.5)
    servo8.set_angle_limits(0, 240)
    time.sleep(0.5)
    

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

print("SERVO INITIAL ANGLES:")
print(servo1.get_physical_angle())
print(servo2.get_physical_angle())
print(servo3.get_physical_angle())
print(servo4.get_physical_angle())
print(servo5.get_physical_angle())
print(servo6.get_physical_angle())
print(servo7.get_physical_angle())
print(servo8.get_physical_angle())
print("\n")
      
print("HOMING SERVOS:")
print("\n")

### Landing mode.
### Lower motors.
##servo2.move(95.04, 3000)
##servo4.move(119.28, 3000)
##servo6.move(66.72, 3000)
##servo8.move(90, 3000)
##time.sleep(3.5)
##
### Upper motors.
##servo1.move(118.08, 3000)
##servo3.move(175.92, 3000)
##servo5.move(133.68, 3000)
##servo7.move(108.72, 3000)
##time.sleep(5)


# Standing mode.
# Lower motors.
servo2.move(173.76, 3000)
servo4.move(181.44, 3000)
servo6.move(137.52, 3000)
servo8.move(159.6, 3000)
time.sleep(3.5)

# Upper motors.
servo1.move(116, 3000)
servo3.move(176.4, 3000)
servo5.move(150.72, 3000)
servo7.move(118.08, 3000)
time.sleep(3.5)


time.sleep(0.5)
      
print("SERVO HOME ANGLES:")
# Lower motors
print(servo1.get_physical_angle())
print(servo2.get_physical_angle())
# Leg 2
print(servo3.get_physical_angle())
print(servo4.get_physical_angle())
# Leg 3
print(servo5.get_physical_angle())
print(servo6.get_physical_angle())
# Leg 4
print(servo7.get_physical_angle())
print(servo8.get_physical_angle())

time.sleep(1)

# Trying to Walk.

t = 0

while True:
    servo1.move(10*sin(0.5*t)+100)
    servo2.move(15*sin(0.5*t)+145)
    

    time.sleep(0.05)
    t += 0.1






