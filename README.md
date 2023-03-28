# m7012e

We have created a system that monitors the user's current emotional state, along with the time of day and adjusts the ambient lighting to reduce/control stress and anxiety.

We aim to do this by monitoring the user's eye movements using Tobii Pro Glasses 2 and modifying ambient light via Philips Hue.
 
- This code connects to our Tobii Pro Glasses 2 eye tracker and captures the user's gaze data along with a live video stream from the glasses. It uses the captured gaze data to determine the user's stress level based on the number of gaze points that are detected in a certain time period. The code then sends a notification to a web hook called IFTTT (If This Then That) using the detected stress level as the trigger. The IFTTT can be used to control other devices or services, such as smart lights or email notifications, based on the trigger received.

- The code imports necessary libraries for Tobii Pro Glasses 2 (tobii_research and controller), for capturing video (cv2), for working with arrays (numpy), and for capturing current time (datetime). It then sets up a connection to the eye tracker, creates a project and a participant, and starts a calibration process.

- Next, the code opens a video capture object to read the live video stream from the glasses. It then starts streaming gaze data from the glasses and captures frames from the video stream. The captured frames are processed to display the gaze point on the video frame as a red circle.

- The code then calculates the stress level of the user based on the number of detected gaze points in a certain time period. The stress level is categorized into four levels: SleepingTime, LowLevelStress, MediumLevelStress, and HighLevelStress. The stress level is printed to the console along with the current time and the corresponding IFTTT web service URL is generated and sent.

- The code uses a while loop to continuously read video frames and gaze data until the user quits the program. The video capture object is then released and the Tobii Pro Glasses 2 connection is closed. Finally, the code includes sections for processing gaze data and controlling lights, but these sections are currently commented out and not used in the code.

- Extra functionality: In future we could look to explore using a system of lights as opposed to just one light. Then we wouldn’t always need to have the sleep functionality in place if we were to control the bedroom lights separately.


