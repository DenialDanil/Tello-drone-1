import os
import cv2
import time
from djitellopy import Tello
import numpy as np

# Function to take a picture and save it to the 'pictures' directory
def take_picture(frame: np.ndarray) -> None:
    try:
        if not os.path.exists("pictures"):
            os.mkdir("pictures")
        file_name = f"pictures/{time.time()}.png"
        cv2.imwrite(file_name, frame)
        print("Image saved:", file_name)
        time.sleep(0.3)
    except Exception as pic_exception:
        print("Error saving image:", pic_exception)

# Function to process and display the Tello video stream
def run_tello_video(drone: Tello) -> None:
    try:
        while True:
            # Capture a frame from the drone's camera
            frame = drone.get_frame_read().frame
            
            # Display the video feed
            cv2.imshow("Frame", frame)
            
            # Handle key events
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('p'):
                take_picture(frame)
    except Exception as stream_exception:
        print("Error in video stream:", stream_exception)
    finally:
        cv2.destroyAllWindows()

# Main function to initialize the drone and start video streaming
def main():
    drone = Tello()
    try:
        # Connect to the drone
        drone.connect()
        
        # Start the video stream
        drone.streamon()
        
        # Process the video stream
        run_tello_video(drone)
    except Exception as main_exception:
        print("Error in main function:", main_exception)
    finally:
        # Reboot the drone to ensure a clean shutdown
        drone.reboot()

# Entry point of the script
if __name__ == '__main__':
    main()
