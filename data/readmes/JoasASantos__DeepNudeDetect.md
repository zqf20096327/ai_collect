# DeepNudeDetect - Comprehensive NSFW/Deepfake Detection & Protection System

A robust tool for detecting deepnudes, deepfakes, NSFW, and NSFL content with image protection capabilities.

## Features

### 🔍 Detection Capabilities
- **Deepnude Detection**: Identifies AI-generated nude imagery
- **Deepfake Detection**: Detects face manipulation and synthetic media
- **NSFW/NSFL Detection**: Classifies inappropriate content
- **Multi-Model Analysis**: Combines multiple AI models for robust detection

### 🛡️ Protection Features
- **Image Perturbation**: Add adversarial noise to protect against deepfake generation
- **Privacy Protection**: Fawkes-style cloaking to prevent facial recognition abuse

### 📊 Input Methods
- File upload
- Image URL analysis
- Folder scanning
- Removable drive scanning

### 🔌 Integrations
- AIorNot API
- OpenAI Vision API
- Google Gemini Vision
- Custom trained models

## Architecture

```
DeepNudeDetect/
├── backend/          # FastAPI backend with ML models
├── frontend/         # React web interface
├── chrome-extension/ # Browser extension
├── models/          # Pre-trained ML models
└── data/            # Upload and processing directories
```

## Components

### Backend (Python + FastAPI)
- REST API for image analysis
- Multiple detection models
- Image perturbation algorithms
- API integrations

### Web Interface (React)
- Upload interface
- Folder/drive scanning
- Real-time analysis results
- Image protection tools

### Chrome Extension
- Automatic image detection
- Real-time alerts
- Privacy protection warnings

## Installation

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python download_models.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Chrome Extension
1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the `chrome-extension` directory

## Usage

### Starting the Backend
```bash
cd backend
python main.py
```
Backend runs on `http://localhost:8000`

### Starting the Web Interface
```bash
cd frontend
npm run dev
```
Frontend runs on `http://localhost:3000`

### API Endpoints

- `POST /api/analyze` - Analyze single image
- `POST /api/analyze-url` - Analyze image from URL
- `POST /api/analyze-folder` - Scan entire folder
- `POST /api/protect-image` - Add adversarial perturbation
- `GET /api/health` - Health check

## Configuration

Create `.env` file in backend directory:
```env
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
AIORNOT_API_KEY=your_key_here
```

## Models Used

1. **NudeNet** - NSFW detection
2. **DeepFake Detection Model** - Face manipulation detection
3. **CLIP** - Content understanding
4. **Custom CNN** - Deepnude specific detection
5. **Adversarial Perturbation** - Fawkes-style protection

## Security & Privacy

- All processing happens locally by default
- API keys are optional for enhanced detection
- Images are not stored unless explicitly saved
- Privacy-first approach

## License

MIT License - Use responsibly for legitimate safety and security purposes only.

## Disclaimer

This tool is designed for legitimate security research, content moderation, and personal protection.
Misuse for harassment or malicious purposes is strictly prohibited.
