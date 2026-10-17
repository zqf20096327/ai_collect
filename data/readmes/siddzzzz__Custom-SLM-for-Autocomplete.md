# Velocitext: SLM Autocomplete

Velocitext is a Small Language Model (SLM) designed for text autocomplete tasks, built from scratch using PyTorch. It is optimized to run on consumer hardware (e.g., NVIDIA RTX 3050 4GB).

## Features
- **Custom Transformer Decoder**: Implemented from scratch (GPT-style).
- **Efficient Training**: Uses mixed precision (AMP) and gradient accumulation to fit in 4GB VRAM.
- **Data Pipeline**: Scrapes Wikipedia and tokenizes using BPE (GPT-2 tokenizer).
- **Interactive UI**: Fast web interface for real-time autocomplete suggestions.

## Project Structure
```text
Velocitext/
├── data/               # Dataset storage
├── src/
│   ├── data/           # Scraper and Preprocessor
│   ├── model/          # Transformer implementation
│   ├── train/          # Training and generation scripts
│   └── ui/             # Web application
├── checkpoints/        # Model checkpoints
└── requirements.txt
```

## Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Collect Data**:
   ```bash
   python src/data/scraper.py
   ```

3. **Preprocess Data**:
   ```bash
   python src/data/preprocessor.py
   ```

## Training
To train the model:
```bash
python src/train/train.py
```
- Checkpoints are saved to `checkpoints/ckpt.pt`.
- You can stop and resume training anytime; the script automatically loads the last checkpoint.

## Usage
### Web UI
Start the web interface using the provided script (ensures correct environment):
```bash
python run_ui.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

### CLI Generation
Generate text from the command line:
```bash
python src/train/generate.py --prompt "Artificial Intelligence is"
```

## Model Configuration
- **Context Length**: 256 tokens
- **Embedding Dim**: 512
- **Layers**: 8
- **Heads**: 8
- **Parameters**: ~25M