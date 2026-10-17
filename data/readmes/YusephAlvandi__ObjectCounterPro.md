Object Counter Pro

An AI-powered object detection tool. Uses YOLOv3 (a deep neural network model trained on 80 object classes). Appropriate for offline operation.

Built with Python, OpenCV, and CustomTkinter.

WHAT IT DOES

In single image mode, the items in an image are detected, labelled and counted, all shown in a live preview. A confidence slider allows you to control detection sensitivity.

Batch mode processes an entire folder of images at once. In either mode results can be saved.


HOW IT WORKS 

A pre-trained model (YOLOv3) is loaded via OpenCV DNN. The model divides the whole image into a grid and predicts bounding boxes and class probabilities for each cell. Non-Maximum Suppression prevents overlapping boxes. All the procedure runs locally on your CPU; no cloud, no API calls, no privacy risk.


COMPETITIVE ADVANTAGE

Majority of object detection tools need to upload your image to a remote server or require expensive GPU hardware. Object Counter Pro works entirely offline on a standard CPU, utilizing an 80-class deep learning model.

- 80 object classes; much more than basic tools
- Confidence slider for sensitivity control
- Batch folder processing
- Live preview with bounding boxes, labels and item counts
- Works offline; your images never leave your local storage
- Built by a precise physicist with an insight into both the optics and the algorithms


HOW TO USE

In single mode
1. Click Open Image and select the image to be processed
2. Adjust the Confidence slider for a desired trade-off:
   - Lower (0.2–0.4): Find more objects, may include false detections.
   - Higher (0.6–0.8): Only confident detections, fewer false positives.
3. View results in the live preview.
4. Save the output.

For batch processing, click Batch Folder, select input and output folders, and process all images at once.


DEPENDENCIES

Python libraries (install once):
pip install opencv-python customtkinter pillow numpy

Model files (place in the same folder as object_counter.py):
- yolov3.weights (236 MB)
- yolov3.cfg (8 KB)
- coco.names (625 B)

AUTHOR

Yuseph Alvandi
PhD in Optics and Laser Physics
Python Developer and Image Processing Specialist

GitHub: https://github.com/YusephAlvandi


LICENSE

MIT License
