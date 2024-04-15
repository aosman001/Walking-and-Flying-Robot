from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

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

""" print("SERVO INITIAL ANGLES:")
print(servo1.get_physical_angle())
print(servo2.get_physical_angle())
print(servo3.get_physical_angle())
print(servo4.get_physical_angle())
print(servo5.get_physical_angle())
print(servo6.get_physical_angle())
print(servo7.get_physical_angle())
print(servo8.get_physical_angle())
print("\n")
      
print("Standing")
print("\n")

### Standing mode.
### Upper motors.
servo1.move(37.20, 1000)
servo3.move(147.84, 1000)
servo5.move(118.32, 1000)
servo7.move(96.24, 1000)
time.sleep(1.5)
### Lower motors.
servo2.move(150.96, 1000)
servo4.move(108, 1000)
servo6.move(50.88, 1000)
servo8.move(146.4, 1000)
time.sleep(6)
##


print('Landing')
print('n')
## Flying mode (legs tucked underneath body)
## Lower motors
servo2.move(104.16, 1000)
servo4.move(49.92, 1000)
servo6.move(7.68, 1000)
servo8.move(102.96, 1000)
time.sleep(1.5)
## Upper motors
servo1.move(4.32, 1000)
servo3.move(111.6, 1000)
servo5.move(85.92, 1000)
servo7.move(52.32, 1000)
time.sleep(1.5)



time.sleep(1)
      
print("SERVO CURRENT ANGLES:")
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

t = 0 """
time.sleep(2.5)
###TRYING TO WALK

#while True:
    #Step 1
#    servo1.move(37.2, 1000)
 #   servo2.move(130, 1000)
  #  servo3.move(190, 1000)
   # servo4.move(114, 1000)
    #time.sleep(1.0)
    #

while True:
    








    servo1.move(37.2, 1000)
    servo2.move(130, 1000)
    servo3.move(190, 1000)
    servo4.move(114, 1000)
    servo5.move(81,1000)
    servo6.move(45,1000)
    servo7.move(100,1000)
    servo8.move(150,1000)
    time.sleep(1.0)

    servo1.move(37.2, 1000)
    servo2.move(130, 1000)
    servo3.move(152, 1000)
    servo4.move(116, 1000)
    servo5.move(100,1000)
    servo6.move(65,1000)
    servo7.move(100,1000)
    servo8.move(110,1000)
    time.sleep(1.0)

    servo1.move(75, 1000)
    servo2.move(81, 1000)
    servo3.move(162, 1000)
    servo4.move(74, 1000)
    servo5.move(100,1000)
    servo6.move(65,1000)
    servo7.move(84,1000)
    servo8.move(122,1000)
    time.sleep(1.0)

    servo1.move(102, 1000)
    servo2.move(175, 1000)
    servo3.move(190, 1000)
    servo4.move(26, 1000)
    servo5.move(113,1000)
    servo6.move(0,1000)
    servo7.move(84,1000)
    servo8.move(122,1000)
    time.sleep(1.0)

    servo1.move(50, 1000)
    servo2.move(150, 1000)
    servo3.move(215, 1000)
    servo4.move(25, 1000)
    servo5.move(96,1000)
    servo6.move(28,1000)
    servo7.move(100,1000)
    servo8.move(150,1000)
    time.sleep(1.0)
