# 🚗 AICTE TASK — Parking Space Detection

A **computer vision-based system** to detect and classify *parking spaces* as occupied or free using video/image input.  
This project is part of an **AICTE-assigned task**, demonstrating practical application of image processing and vehicle detection techniques.

---

## 📌 Project Overview

Parking management is an important challenge in smart cities, campuses, and commercial areas. This project uses **OpenCV** (and optionally machine learning/AI models) to:

✔ Detect parking slots in a static image or video feed  
✔ Identify whether each slot is **occupied** or **available**  
✔ Output real-time or batch results for parking space status

---

## 📂 Project Structure

```

├── 1.py                        # First code 
├── easy1.mp4                   # Sample video feed
├── 2.py                        # Tool to mark parking spaces
├── coco.txt                   # Core detection logic                     
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation (this file)

````

---

## 🛠 Requirements

Make sure you have **Python 3.7+** installed.

Install the required libraries:

```bash
pip install -r requirements.txt
````

Common dependencies include:

* `opencv-python`
* `cvzone`
* `numpy`
---

## ⚙️ How It Works

### 1. Define Parking Spaces

Use the **ParkingSpacePicker.py** script to manually mark parking slots on an image:

```bash
python ParkingSpacePicker.py
```

**Controls:**

* Left-click to add a slot
* Right-click to remove
* Press `Space` to reset
* Press `Q` to save

Slots are saved to a file (e.g., `CarParkPos`) for later use.

---

### 2. Detect Free/Occupied Spaces

Once the slot coordinates are stored:

```bash
python main.py
```

This script:

* Opens the video feed frame by frame
* Uses saved slot positions
* Classifies each slot as *free* or *occupied*
* Displays results and counts in real time

---

## 📊 Output

After detection, you will see:

* Live visualization of occupied and free slots
* Slot status text overlay
* Summary of free vs. occupied count
  (You can extend this to save logs/CSV reports)

---

## 🧠 Techniques Used

* Image thresholding
* Contour detection
* Region-of-interest (ROI) extraction
* Vehicle detection via pixel analysis
* (Optional) Deep-learning models like YOLO / edge AI

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ✨ Future Improvements

* Add automated parking slot detection (no manual marking)
* Integrate YOLOv8 or other deep learning for better detection
* Export logs to CSV/JSON for analytics
* Build a web dashboard for live monitoring

---

## 👏 Acknowledgements

Inspired by popular parking detection tutorials and projects built using CV techniques. ([GitHub][1])


[1]: https://github.com/harshbafnaa/car-parking-detection?utm_source=chatgpt.com "Car Parking Space Detection Project - GitHub"
