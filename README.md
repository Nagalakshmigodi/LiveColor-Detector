# Color Detector using Webcam and OpenCV

This project captures live video from your webcam and detects the color at the center of the frame. It compares the pixel color to a list of known colors (from the XKCD color dataset) and displays the closest color name on the video feed in real-time.

## Features

- Captures webcam feed using OpenCV
- Detects color at the center pixel of the video frame
- Finds the closest matching color name using XKCD colors CSV
- Displays the detected color name on the video stream
- Press 'q' to quit the application

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- pandas
- numpy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NagaLakshmigodi/color-detector.git
   cd color-detector
2.Install dependencies:

pip install opencv-python pandas numpy

3.Make sure you have the xkcd_colors.csv file in the project folder.
(This CSV contains color names and their RGB values used for matching.)

Run the script:
python color_detector.py
A window will open showing your webcam feed with the detected color name displayed at the center. Press q to quit.

Notes
You may need to change the webcam device index in the script (cv2.VideoCapture(1)) to 0 or another number depending on your setup.

The color detection is based on Euclidean distance in RGB color space to the colors in the XKCD dataset.
License
This project is licensed under the MIT License.
