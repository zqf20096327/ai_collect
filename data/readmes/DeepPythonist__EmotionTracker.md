<div align="center">
  <img src="logo.png" alt="Emotion Tracker Logo" width="200">
</div>

# Emotion Tracker

A professional Python desktop application for real-time facial emotion detection using DeepFace. The application analyzes user emotions via webcam and stores data as time-series CSV files with comprehensive analytics.

## 🎥 Demo Video

![Emotion Tracker Demo](demo.gif)

*Watch the demo GIF above*

## Features

- **Real-time Emotion Detection**: Uses DeepFace for accurate emotion recognition
- **Interactive GUI**: Three-tab interface (Control, Monitor, Analytics)
- **Performance Optimized**: Processes every 3rd frame to reduce CPU load
- **Data Storage**: Automatically saves daily CSV files with timestamps
- **Visual Analytics**: Pie charts and statistics for emotion analysis
- **Privacy-Focused**: All data stored locally, no internet transmission

## Requirements

- Python 3.11+ (tested with Python 3.11.1)
- Webcam access
- Internet connection (for initial DeepFace model download)
- macOS 11.0+ / Windows 10+ / Ubuntu 18.04+

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/DeepPythonist/EmotionTracker.git
   cd EmotionTracker
   ```

2. Create virtual environment:
   ```bash
   conda create -n emotiontracker python=3.10
   conda activate emotiontracker
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Control Tab
- Click **START** to begin emotion detection
- Click **STOP** to stop recording
- Monitor status and frame count

### Monitor Tab
- View current detected emotion in large text
- See confidence level with progress bar
- Track session statistics and top emotions

### Analytics Tab
- Select date from dropdown to view historical data
- View emotion distribution pie chart (if matplotlib available)
- Review summary statistics
- Monitor current session emotions

## Data Storage

- CSV files are automatically created in the `data/` directory
- File naming format: `emotions_YYYY-MM-DD.csv`
- Columns: `timestamp,emotion,confidence`
- Data is appended continuously during recording sessions

## Performance Optimization

The application implements several optimization techniques:

- Processes every 3rd frame (not every frame)
- Uses `enforce_detection=False` for better edge case handling
- Implements frame skipping when processing takes >100ms
- Resizes frames to 640x480 before processing
- Caches DeepFace model on first load
- Uses threading to separate UI from processing

## Error Handling

- Camera not found: Shows error dialog, disables START button
- DeepFace import error: Shows installation instructions
- No face detected: Skips frame silently
- Low confidence (<0.5): Marks as "uncertain"

## Project Structure

```
EmoNet/
├── main.py                    # Main application
├── requirements.txt           # Dependencies
├── README.txt                # Installation guide
├── PRIVACY.txt               # Privacy policy
├── LICENSE.txt               # MIT License
├── core/                     # Core modules
│   ├── camera_handler.py
│   ├── emotion_detector.py
│   └── data_manager.py
├── ui/                       # UI components
│   ├── main_window.py
│   ├── monitor_tab.py
│   └── analytics_tab.py
├── utils/                    # Utility modules
│   └── config.py
└── data/                     # Data storage folder
```

## Technical Details

- **CPU Usage**: <15% on modern i5 processors
- **RAM Usage**: <500MB
- **Detection Latency**: <2 seconds per processed frame
- **UI Responsiveness**: No freezing during processing

## Dependencies

- deepface==0.0.79
- opencv-python==4.8.1.78
- pandas>=2.0.0,<2.2.0
- matplotlib>=3.7.0,<3.9.0
- seaborn>=0.12.0,<0.14.0
- pillow>=9.0.0,<11.0.0
- tensorflow>=2.13.0,<2.16.0
- numpy>=1.21.0,<2.0.0

## Support

If you have any issues:
- Email: mrasolesfandiari@gmail.com
- GitHub: https://github.com/DeepPythonist/EmotionTracker

## License

MIT License - See LICENSE.txt for details.

This project is provided for educational and research purposes.
