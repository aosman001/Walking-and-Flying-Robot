import threading
import time
import mavlink_monitor 
from Walking.Walking_RP_Code import walking_main


def control_walking():
  global walking_speed, walking_direction, walking_lock
  while True:
    print(walking_speed, walking_direction, walking_lock)
    time.sleep(0.1)
  

if __name__ == "__main__":
  # Thread the functions to run both at the same time independent of one another
  mavlink_thread = threading.Thread(target=mavlink_monitor.mavlink_monitor)
  mavlink_thread.daemon = True
  mavlink_thread.start()

  control_thread = threading.Thread(target=control_walking)
  control_thread.daemon = True
  control_thread.start()

  mavlink_thread.join()  # Add this line to make the main thread wait for this thread to finish
  control_thread.join()  # Add this line to make the main thread wait for this thread to finish
