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

# Leg 1
servo1.move(120, 3000)
time.sleep(1)
servo2.move(120, 3000)
time.sleep(1)
# Leg 2
servo3.move(120, 3000)
time.sleep(1)
servo4.move(120, 3000)
time.sleep(1)
# Leg 3
servo5.move(120, 3000)
time.sleep(1)
servo6.move(120, 3000)
time.sleep(1)
# Leg 4
servo7.move(120, 3000)
time.sleep(1)
servo8.move(120, 3000)
time.sleep(1)


time.sleep(0.5)
      
print("SERVO HOME ANGLES:")
# Leg 1
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
