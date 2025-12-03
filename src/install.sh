#!/bin/bash

echo "=== Installing YOLOs Real-Time Detection Dependencies ==="

#############################################
# 1. UPGRADE pip
#############################################

pip install --upgrade pip
echo "[OK] pip upgraded"


#############################################
# 2. INSTALL PYTORCH (Auto detect CUDA)
#############################################

echo "Detecting CUDA..."

CUDA_AVAILABLE=$(python3 - << 'EOF'
import subprocess
try:
    out = subprocess.getoutput("nvidia-smi")
    print("cuda" if "NVIDIA-SMI" in out else "cpu")
except:
    print("cpu")
EOF
)

if [ "$CUDA_AVAILABLE" = "cuda" ]; then
    echo "[OK] CUDA detected — installing CUDA PyTorch..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
else
    echo "[OK] No CUDA found — installing CPU PyTorch..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
fi


#############################################
# 3. INSTALL SUPER-GRADIENTS (YOLO-NAS)
#############################################

echo "Installing SuperGradients (YOLO-NAS framework)..."
pip install super-gradients


#############################################
# 4. INSTALL OPENCV
#############################################

echo "Installing OpenCV..."
pip install opencv-python


#############################################
# 5. INSTALL NUMPY
#############################################

echo "Installing numpy..."
pip install numpy


#############################################
# 6. INSTALL OPTIONAL BUT RECOMMENDED PACKAGES
#############################################

echo "Installing pycocotools (Windows-compatible version)..."
pip install pycocotools-windows


echo "Installing other recommended utilities..."
pip install matplotlib tqdm

pip install ultralytics


echo "=== INSTALLATION COMPLETE ==="
echo "You can now run: python your_yolonas_script.py"
