import os

# Activate Conda environment and run detection inside yolov5 directory
command = "conda activate your_env_name && cd yolov5 && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0"

# Execute the command in a new terminal
os.system(f'start cmd /k "{command}"')
