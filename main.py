import threading
import time
import mavlink_monitor 
from Walking.Walking_RP_Code import walking_main



if __name__ == "__main__":
  # Thread the functions to run both at the same time independent of one another
  mavlink_thread = threading.Thread(target=mavlink_monitor.mavlink_monitor)
  mavlink_thread.daemon = True
  mavlink_thread.start()

  walking_thread = threading.Thread(target=walking_main)
  walking_thread.daemon = True
  walking_thread.start()

  mavlink_thread.join()  # Add this line to make the main thread wait for this thread to finish
  walking_thread.join()  # Add this line to make the main thread wait for this thread to finish
