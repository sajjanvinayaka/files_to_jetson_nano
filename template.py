import os, sys
from pathlib import Path 
import logging 


while True:
    # project_name = input("Enter your project name: ")
    project_name = "src"
    if project_name != "":
        break

#src/__init__.py
#src/components/__init__.py

list_of_files = [
    f"{project_name}/__init__.py",
    
    # Core Inference Components
    f"{project_name}/inference/__init__.py",
    f"{project_name}/inference/model_loader.py",  # Load YOLO model for inference
    f"{project_name}/inference/predictor.py",  # Run inference on images
    f"{project_name}/inference/preprocessor.py",  # Image preprocessing (resize, normalize)
    f"{project_name}/inference/postprocessor.py",  # Convert model output to bounding boxes, masks

    # Constants 
    f"{project_name}/constants/__init__.py"
    
    # 
    
    # Utility Functions (Image Processing, I/O, etc.)
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/image_utils.py",  # Resize, normalize, augment images
    f"{project_name}/utils/yolo_utils.py",  # YOLO-specific inference functions

    # API for Serving Inference
    "app.py",  # FastAPI or Flask-based REST API for inference
    "main.py",  # Entry point to run the inference pipeline

    # Configuration Files
    "config/config.yaml",  # Stores model paths, input image size, confidence threshold
    "models/best_model.pt",  # YOLO trained model weights

    # Sample Data & Testing
    "sample_images/",  # Folder with test images for inference
    "outputs/",  # Folder to store inference results (bounding boxes, masks)
    "notebooks/inference_test.ipynb",  # Jupyter Notebook for testing model inference
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
    
    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) ): 
        with open(filepath, "w") as f:
            pass
        
    else:
        logging.info(f"file is already present at :{filepath}")