import cv2
import os
import datetime
import time

# Define overlay text directly in the script
OVERLAY_TEXT = "{}"

def save_frame(frame, width, height, directory="captured_images"):
    os.makedirs(directory, exist_ok=True)
    resized_frame = cv2.resize(frame, (width, height))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(directory, f"capture_{timestamp}.jpg")
    cv2.imwrite(filename, resized_frame)
    print(f"Frame saved as {filename}")

def main():
    # Initializationn
    camera = cv2.VideoCapture(2)
    if not camera.isOpened():
        print("Error: Camera not found!")
        return

    # Set resolution of camera and captured_image 
    video_width = 640
    video_height = 480
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, video_width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, video_height)
    capture_width = 1920
    capture_height = 1080

    countdown_active = False
    countdown_start_time = None

# set the countdown timer, the timer will start from the "countdown_duration"
    countdown_duration = 14

# Read a frame from the camera
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Unable to read from camera.")
            break

# this willHandle countdown logic
        if countdown_active:
            elapsed_time = time.time() - countdown_start_time
            remaining_time = countdown_duration - int(elapsed_time)

            if remaining_time > 0:
# Display's text on the live video feed
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 4
                font_color = (12, 255, 5)  # Red text
                thickness = 4

                countdown_text = OVERLAY_TEXT.format(remaining_time)
                text_size = cv2.getTextSize(countdown_text, font, font_scale, thickness)[0]
                text_x = (frame.shape[1] - text_size[0]) // 2
                text_y = (frame.shape[0] + text_size[1]) // 2

                cv2.putText(frame, countdown_text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)
            else:
                # Save the frame once the countdown reaches 0
                save_frame(frame, capture_width, capture_height)
                countdown_active = False  # Stop the countdown

        # Display the live video feed
        cv2.imshow("Live Video Stream", frame)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('x') and not countdown_active:
            # Start the countdown on pressing 'x'
            countdown_active = True
            countdown_start_time = time.time()
        elif key == ord('q'):
            # Exit the application on pressing 'q'
            break

    # Release resources
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
