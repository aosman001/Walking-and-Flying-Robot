from pymavlink import mavutil


# mavlink_monitor edits these global variables that are consumed by the other threads, like state.
walking_lock = True
walking_direction = "middle" # "forward" | "middle" | "back"
walking_speed = 0.0 # 0.0 to 1.0

# Reads controls from the Flysky
def mavlink_monitor():
  global walking_speed, walking_direction, walking_lock
  master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57_600)
  running = True
  while running:
    try:
      msg = master.recv_match(type="RC_CHANNELS", blocking=True)
      if not msg:
        print("ERROR: msg was NONE somehow")
        return
      # print(f"Channel 1: {msg.chan1_raw}")
      # print(f"Channel 2: {msg.chan2_raw}")
      # print(f"Channel 3: {msg.chan3_raw}")
      # print(f"Channel 4: {msg.chan4_raw}")
      # print(f"Channel 5: {msg.chan5_raw}")
      # print(f"Channel 6: {msg.chan6_raw}")
      # print(f"Channel 7: {msg.chan7_raw}")
      # print(f"Channel 8: {msg.chan8_raw}")

      # Values are empirical
      walking_speed_channel = msg.chan6_raw
      walking_dir_channel = msg.chan7_raw
      walking_lock_channel = msg.chan8_raw

      walking_speed = max(0.0, min(1.0, (walking_speed_channel - 1000) / 1000))

      if walking_dir_channel < 1100:
        walking_direction = "forward"
      elif walking_dir_channel >= 1100 and walking_dir_channel < 1600:
        walking_direction = "middle"
      else:
        walking_direction = "back"

      if walking_lock_channel < 1500:
        walking_lock = False
      else:
        walking_lock = True

    except KeyboardInterrupt:
      print("Exiting...")
      running = False
    except Exception as e:
      print("------EXCEPTION--------")
  
  master.close()