from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    #servo3 = LX16A(3)
    #servo4 = LX16A(4)
    #servo5 = LX16A(5)
    #servo6 = LX16A(6)
    #servo7 = LX16A(7)
    #servo8 = LX16A(8)
    
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    #servo3.set_angle_limits(0, 240)
    #servo4.set_angle_limits(0, 240)
    #servo5.set_angle_limits(0, 240)
    #servo6.set_angle_limits(0, 240)
    #servo7.set_angle_limits(0, 240)
    #servo8.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    
    servo1.move(sin(t) * 60 + 60)
    servo2.move(cos(t) * 60 + 60)

    #servo3.move(sin(t) * 60 + 60)
    #servo4.move(cos(t) * 60 + 60)

    #servo5.move(sin(t) * 60 + 60)
    #servo6.move(cos(t) * 60 + 60)

    #servo7.move(sin(t) * 60 + 60)
    #servo8.move(cos(t) * 60 + 60)

    

    time.sleep(0.05)
    t += 0.1
