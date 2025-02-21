import cv2
from djitellopy import Tello

# Function to process and display video stream from Tello
def process_tello_video(drone):
    while True:
        # Capture a frame from the drone's camera
        frame = drone.get_frame_read().frame
        
        # Convert the frame from BGR to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the video feed
        cv2.imshow("CAMERA", frame_rgb)
        
        # Exit the video stream if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Close all OpenCV windows and end the drone connection
    cv2.destroyAllWindows()
    drone.end()

# Main function to initialize the drone and start video streaming
def main():
    # Create a Tello drone instance
    drone = Tello()
    
    # Connect to the drone
    drone.connect()
    
    # Set the video direction to forward-facing camera
    drone.set_video_direction(drone.CAMERA_FORWARD)
    
    # Start the video stream
    drone.streamon()
    
    # Process the video stream
    process_tello_video(drone)

# Entry point of the script
if __name__ == '__main__':
    main()