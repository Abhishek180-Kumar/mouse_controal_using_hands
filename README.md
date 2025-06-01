# Hand Gesture Virtual Mouse

A Python application that uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to control your computer mouse using hand gestures captured from your webcam.

## Features

- Control the mouse cursor by moving your index finger.
- Perform mouse clicks by bringing your thumb and index finger close together.
- Real-time hand tracking and gesture detection.
- Works with a single hand for smooth control.
- Simple, lightweight, and easy to use.

## Demo

![Demo GIF or Image Here]  
*(You can add a GIF or screenshot showing the app in action)*

## Requirements

- Python 3.7 or higher
- Webcam

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Abhishek180-Kumar/hand-gesture-virtual-mouse.git
   cd hand-gesture-virtual-mouse

## Install dependencies:
pip install opencv-python mediapipe pyautogui

## Usage
Run the Python script:
python virtual_mouse.py

## Controls
Move mouse: Move your index finger in front of the webcam.
Click: Bring your thumb and index finger tips close together.
Exit: Press ESC key to quit the program.

### How It Works
Uses MediaPipe Hands to detect hand landmarks.
Tracks the index finger tip to move the mouse cursor.
Detects proximity between thumb and index finger tips to perform mouse clicks.
Maps hand coordinates from the webcam feed to the screen resolution for accurate control.

## Troubleshooting
Make sure your webcam is enabled and not being used by other applications.
Ensure good lighting conditions for better hand detection.
Adjust the click distance threshold in the code if clicks are too sensitive or not detected properly.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
