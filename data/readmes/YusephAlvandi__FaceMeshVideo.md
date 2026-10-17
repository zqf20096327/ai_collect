FaceMeshVideo

This application is used for detecting faces in a video and meshing them with facial landmarks. This can be used as a preliminary step for developing face recognition software.
This software has been developed with Python, OpenCV, Pillow, NumPy, Ultralytics, MediaPipe Tasks API, and CustomTkinter.
Two deep learning models were used: YOLOv8n-face (a CNN for face detection) and MediaPipe Face Landmarker (a DNN for meshing the face with 478 points), loaded from the pre-trained file face_landmarker.task.
Taking advantage of “ffmpeg” the original sound of the video will be preserved.
The user-friendly and straightforward to use GUI has been developed by “CustomTkinter” .
It works completely offline, without any need to upload data to any external server and cloud system, which guarantees your privacy.

HOW TO RUN

python video_facial_landmarks.py

1. Click Open Video and select a video file.
2. Adjust landmark size and YOLO confidence.
3. Click Start Processing.
4. Choose where to save the output video.


DEPENDENCIES

Python libraries (install once):
pip install ultralytics opencv-python pillow customtkinter mediapipe numpy

System tools:
sudo apt install ffmpeg

Model files (place in the same folder as the script):
- yolov8n-face.pt (6 MB); auto-downloaded on first run, or download manually
- face_landmarker.task (3.6 MB); download from MediaPipe


AUTHOR

Yuseph Alvandi
PhD in Optics and Laser Physics
Python Developer and Image Processing Specialist

GitHub: https://github.com/YusephAlvandi


LICENSE

MIT License


