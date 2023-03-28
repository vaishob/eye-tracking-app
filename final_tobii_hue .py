import tobii_research as tr
import controller
import time
import urllib.request
import cv2
import numpy as np
from datetime import datetime

"""
Connecting to eye tracker
"""


"""
Gaze Data Here Need to Create Loop
"""


if hasattr(__builtins__, 'raw_input'):

      input=raw_input



now = datetime.now()

current_time = now.strftime("%H")

ipv4_address = "192.168.71.50"

tobiiglasses = controller.TobiiGlassesController(ipv4_address, video_scene=True)

project_id = tobiiglasses.create_project("Test live_scene_and_gaze.py")

participant_id = tobiiglasses.create_participant(project_id, "participant_test")

calibration_id = tobiiglasses.create_calibration(project_id, participant_id)

input("Put the calibration marker in front of the user, then press enter to calibrate")
tobiiglasses.start_calibration(calibration_id)

res = tobiiglasses.wait_until_calibration_is_done(calibration_id)


if res is False:
	print("Calibration failed!")
	exit(1)


cap = cv2.VideoCapture("rtsp://%s:8554/live/scene" % ipv4_address)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
tobiiglasses.start_streaming()
gpqueue = []
counter = 0
threshold = 0.4
while(cap.isOpened()):
  # Capture frame-by-frame
  tobiiglasses.get_data()
  ret, frame = cap.read()
  if ret == True:
    height, width = frame.shape[:2]
    data_gp  = tobiiglasses.get_data()['gp']
    data_gpgp = data_gp['gp']
    counter += 1
    if not gpqueue:
        gpqueue.append(data_gpgp)
    else:
        if (abs(data_gpgp[0]-gpqueue[-1][0])+abs(data_gpgp[1]-gpqueue[-1][1]))>threshold:
            gpqueue.append(data_gpgp)
            counter = 0
    if counter > 3:
        gpqueue = []
    print(gpqueue)
    if data_gp['ts'] > 0:
        cv2.circle(frame,(int(data_gp['gp'][0]*width),int(data_gp['gp'][1]*height)), 60, (0,0,255), 5)

    # # Display the resulting frame
    # cv2.imshow('Tobii Pro Glasses 2 - Live Scene',frame)
    stress_level = 'Normal'
    print(current_time)
    if int(current_time)>19 or int(current_time)<8:
        stress_level = 'SleepingTime'
    if  len(gpqueue)>5:
        stress_level = 'LowLevelStress'
    if len(gpqueue)>10 :
        stress_level = 'MediumLevelStress'
    if len(gpqueue)>15 : 
        stress_level = 'HighLevelStress'


    print("User is on {}".format(stress_level))

    url = "https://maker.ifttt.com/trigger/{}/json/with/key/dkGggE04bUpAq2pHaIFTv".format(stress_level)
    print(url)
    urllib.request.urlopen(url)

        
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

tobiiglasses.stop_streaming()
tobiiglasses.close()



"""
Processing Gaze Data
"""




"""
For controlling lights (Last step)
"""

