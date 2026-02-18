import cv2
import numpy as np
import cvzone
import pickle
import os

# Verify file path
video_path = r'C:\Users\Admin\Downloads\yolov8-advance-parkingspace-detection-main\yolov8-advance-parkingspace-detection-main\easy1.mp4'
if not os.path.isfile(video_path):
    print("File not found!")
else:
    print("File found!")

cap = cv2.VideoCapture(video_path)

drawing = False
area_names = []
try:
    with open("freedomtech", "rb") as f:  # Use 'rb' mode for reading binary files
        data = pickle.load(f)
        polylines, area_names = data['polylines'], data['area_names']
        print("Loaded polylines and area names from file.")
except FileNotFoundError:
    polylines = []
    print("File not found, starting with empty polylines.")
except Exception as e:
    polylines = []
    print(f"An error occurred: {e}")

points = []
current_name = ""

def draw(event, x, y, flags, param):
    global points, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        current_name = input('areaname:-')
        if current_name:
            area_names.append(current_name)
            polylines.append(np.array(points, np.int32))
            points = []  # Clear points after saving

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    frame = cv2.resize(frame, (1020, 500))
    for i, polyline in enumerate(polylines):
        cv2.polylines(frame, [polyline], True, (0, 0, 225), 2)
        cvzone.putTextRect(frame, f'{area_names[i]}', tuple(polyline[0]), 1, 1)
    cv2.imshow('FRAME', frame)
    cv2.setMouseCallback('FRAME', draw)
    key = cv2.waitKey(100) & 0xFF
    if key == ord('s'):
        with open("freedomtech", "wb") as f:  # Use 'wb' mode for writing binary files
            data = {'polylines': polylines, 'area_names': area_names}
            pickle.dump(data, f)
        print("Saved polylines and area names to file.")
    elif key == ord('q'):  # Press 'q' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()
