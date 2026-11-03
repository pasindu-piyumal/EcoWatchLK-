# 🌿 EcoWatchLK – Vehicle Exhaust Smoke Detection System

**An AI-powered vehicle exhaust smoke detection system designed to identify visible vehicle emissions using computer vision and deep learning.**

EcoWatch LK aims to support environmental monitoring in Sri Lanka by detecting visible exhaust smoke from vehicles and identifying nearby vehicles through real-time camera input.

---

## 📌 Project Overview

Vehicle exhaust emissions contribute to air pollution and environmental degradation. EcoWatch LK explores how computer vision and deep learning can be used to automatically detect visible smoke emissions from vehicles.

The system combines two YOLO-based object detection models:

- **Vehicle Detection:** Identifies vehicles using a pretrained YOLO model.
- **Smoke Detection:** Detects visible exhaust smoke using a custom-trained YOLO model.

The detected smoke regions are compared with vehicle locations using a spatial association method to identify smoke that appears near detected vehicles.

## ✨ Key Features

- Real-time vehicle detection.
- Vehicle exhaust smoke detection.
- Detection of multiple vehicles in a single frame.
- Spatial association between detected vehicles and nearby smoke.
- Support for different vehicle categories.
- Live camera input using OpenCV.
- iPhone camera integration through Camo Studio.
- Annotated video output showing detection results.
- GPU acceleration using NVIDIA CUDA when available.

## 🧠 Detection Architecture

EcoWatch LK uses a dual-model detection architecture.

### 1. Vehicle Detection

A pretrained YOLO11s model is used to detect vehicles.

The system focuses on the following COCO classes:

| Class ID | Vehicle Type |
|---|---|
| 2 | Car |
| 3 | Motorcycle |
| 5 | Bus |
| 7 | Truck |

### 2. Smoke Detection

A custom-trained YOLO11s model is used to detect visible smoke emissions.

The custom smoke model was trained using a prepared dataset containing positive smoke examples and negative background images.

### 3. Vehicle–Smoke Association

After detecting vehicles and smoke regions, the system uses spatial proximity to associate smoke detections with nearby vehicles.

**Important:** Spatial association indicates that smoke is near a detected vehicle. It does not independently prove that the smoke originated from that particular vehicle.

## 📊 Smoke Detection Model

The following results were obtained from the custom smoke detection model's test evaluation:

| Evaluation Metric | Result |
|---|---:|
| Precision | 0.7667 |
| Recall | 0.7101 |
| mAP@50 | 0.7296 |
| mAP@50–95 | 0.3353 |

These results represent the smoke detection model evaluation, not the complete vehicle–smoke association system.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Ultralytics YOLO | Object detection |
| YOLO11s | Vehicle and smoke detection |
| PyTorch | Deep learning framework |
| OpenCV | Image and video processing |
| NumPy | Numerical operations |
| CUDA | GPU acceleration |
| Flask | Planned web dashboard backend |
| HTML, CSS, JavaScript | Planned dashboard frontend |
| Camo Studio | iPhone camera integration |

## 📁 Project Structure

```text
smoke_vehicle_detection/
│
├── pretrained_vehicle_detection_models/
│   ├── yolo11n.pt
│   └── yolo11s.pt
│
├── runs/
│   └── ecowatch/
│       └── model_comparison/
│           └── YOLO11s/
│               └── weights/
│                   └── best.pt
│
├── EcoWatch-Final-YOLO/
│
├── EcoWatch-Negative-Candidates/
│
├── EcoWatch-Negative-Review/
│
├── EcoWatch-Smoke-Converted/
│
├── annotation_audit/
│
├── notebooks/
│
├── outputs/
│
├── test_images/
│
├── test_video/
│
├── download_dataset.py
├── dual_detection.py
├── live_ecowatch.py
├── test_camo_camera.py
├── .gitignore
└── README.md
```

*Note: Large datasets, trained model weights, generated outputs, and virtual environments are excluded from Git using `.gitignore`.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/EcoWatch-LK.git
```

Navigate into the project directory:

```bash
cd EcoWatch-LK
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install ultralytics opencv-python numpy flask
```

Install a compatible PyTorch build with CUDA support separately if GPU acceleration is required.

### 4. Download Required Model Weights

The system requires two model weights:

- Pretrained vehicle detection model: `yolo11s.pt`
- Custom smoke detection model: `best.pt`

Place them in the paths expected by `dual_detection.py`.

The model weights and datasets are not included in this repository.

## 🚀 Running the Detection System

### Real-Time Camera Detection

Connect your iPhone to your Windows laptop using Camo Studio and make sure the Camo virtual camera is available.

Run:

```bash
python live_ecowatch.py
```

The application will:

1. Load the vehicle and smoke detection models.
2. Initialize the selected camera.
3. Capture live video frames.
4. Detect vehicles and visible smoke.
5. Associate nearby smoke detections with vehicles.
6. Display annotated detection results.

Press **Q** or **ESC** to close the live detection window.

### Video Detection

The dual detection module also supports video processing.

Example:

```bash
python dual_detection.py --source test_video/sample.mp4
```

*Use the appropriate command-line options supported by the current implementation.*

## 📷 Camera Integration

EcoWatch LK supports camera input through OpenCV.

For the current development setup:

- Laptop camera: Camera index `0`
- Camo iPhone camera: Camera index `1`

The camera index may vary depending on the connected devices and system configuration.

## 📈 Future Improvements

- Develop a web-based monitoring dashboard.
- Add real-time detection statistics and event history.
- Store detection records with timestamps.
- Integrate location information where available.
- Improve smoke detection accuracy using additional real-world data.
- Evaluate performance under different lighting and weather conditions.
- Explore automated reporting for environmental monitoring.

## ⚠️ Limitations

- The system detects visible smoke, not invisible exhaust gases.
- Smoke detection performance depends on image quality, lighting, distance, and environmental conditions.
- Nearby smoke association is based on spatial proximity and may produce incorrect associations.
- Detection results should be reviewed before making any enforcement or regulatory decisions.

## 🌍 Project Goal

EcoWatch LK explores the application of artificial intelligence and computer vision to environmental monitoring in Sri Lanka.

The long-term goal is to develop a practical monitoring platform that can assist in identifying vehicles associated with visible exhaust smoke and support further environmental research.

---

## 👨‍💻 Author

**Pasindu Piyumal Amarasinghe**

BSc (Hons) in Data Science  
Sabaragamuwa University of Sri Lanka

**Project:** EcoWatch LK – Vehicle Exhaust Smoke Detection System

---

## 📄 License

This project is developed for educational and research purposes. A license can be added when the repository's distribution terms are finalized.