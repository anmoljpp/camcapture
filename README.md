# Countdown Video Capture with Frame Saving

This project captures live video from a connected camera, displays a countdown timer when triggered, and saves a single frame when the countdown reaches zero. The saved frame is stored as a high-resolution image in a specified directory.

## Features
- Live video streaming using OpenCV.
- Countdown timer overlay displayed on the video feed.
- Frame capture and save upon countdown completion.
- Adjustable camera resolution and countdown duration.

## Requirements
- Python 3.x
- OpenCV (`cv2`)

## Installation
1. Clone or download this repository.
2. Install the required Python libraries using pip:
   ```bash
   pip install opencv-python
   ```

## How to Use
1. Connect a camera to your computer.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. During the live video feed:
   - Press `x` to start the countdown.
   - Press `q` to quit the application.
4. The captured frame is saved in the `captured_images` folder.

## Customization

### Camera Settings
- Change the camera index if necessary (default is `2`):
  ```python
  camera = cv2.VideoCapture(2)
  ```
- Adjust the resolution for video and captured images:
  ```python
  video_width = 640
  video_height = 480
  capture_width = 1920
  capture_height = 1080
  ```

### Countdown Timer
- Modify the countdown duration (default is `14` seconds):
  ```python
  countdown_duration = 14
  ```

### Overlay Text
- Update the text displayed during the countdown by modifying the `OVERLAY_TEXT` variable:
  ```python
  OVERLAY_TEXT = "{}"
  ```
  `{}` will be replaced with the remaining seconds.

## File Structure
- **Script**: The Python file containing the main logic.
- **Captured Images**: The `captured_images` folder stores saved frames.

## Example Usage
1. Start the program to open the live video feed.
2. Press `x` to display the countdown timer on the video.
3. Once the timer reaches `0`, the current frame will be saved.

## Notes
- Ensure the connected camera is detected and properly configured.
- Make sure the `captured_images` directory has write permissions.

