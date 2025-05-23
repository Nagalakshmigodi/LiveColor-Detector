import cv2
import pandas as pd
import numpy as np

print("Starting script...")

# Load the CSV file
color_data = pd.read_csv("xkcd_colors.csv")
print("CSV loaded successfully")

def get_closest_color_name(r, g, b):
    min_dist = float('inf')
    closest_name = "Unknown"
    for i in range(len(color_data)):
        cr, cg, cb = color_data.loc[i, ['R', 'G', 'B']]
        dist = np.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        if dist < min_dist:
            min_dist = dist
            closest_name = color_data.loc[i, 'Color Name']
    return closest_name

cap = cv2.VideoCapture(0)  # Use 0 if 1 doesn't work for your webcam
if not cap.isOpened():
    print("❌ Could not open webcam")
    exit()

print("✅ Webcam opened successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Resize for consistency
    frame = cv2.resize(frame, (640, 480))
    cx, cy = 320, 240  # center point

    # Get color at center pixel (note OpenCV uses BGR order)
    b, g, r = frame[cy, cx]
    color_name = get_closest_color_name(r, g, b)

    # Show color name and center dot on frame
    cv2.putText(frame, f"{color_name}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (int(b), int(g), int(r)), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)

    # Show processed frame
    cv2.imshow("Color Detector", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
