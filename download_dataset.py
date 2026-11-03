
import os
from pathlib import Path
from roboflow import Roboflow

# Read the API key from an environment variable
api_key = os.environ.get("ROBOFLOW_API_KEY")

if not api_key:
    raise RuntimeError(
        "ROBOFLOW_API_KEY is not set. "
        "Set it in PowerShell before running this script."
    )

print("Connecting to Roboflow...")

rf = Roboflow(api_key=api_key)

project = (
    rf.workspace("student-project-wixsj")
    .project("smoke-vehicles-detection")
)

# Download dataset version 2 in YOLO format
version = project.version(2)
dataset = version.download("yolov8")

print("\nDataset downloaded successfully!")
print("Dataset location:", dataset.location)

# Check for the dataset configuration file
data_yaml = Path(dataset.location) / "data.yaml"

if data_yaml.exists():
    print("Dataset configuration found:", data_yaml)
    print("\nDataset configuration:")
    print(data_yaml.read_text(encoding="utf-8"))
else:
    print("Warning: data.yaml was not found at the expected location.")
    print("Inspect the downloaded directory:", dataset.location)
