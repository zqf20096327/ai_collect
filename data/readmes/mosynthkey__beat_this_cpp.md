# Beat This! C++ Implementation

A C++ port of the "Beat This!" AI-powered beat tracking system from Johannes Kepler University Linz. 

## Overview

This is a C++ implementation of the Beat This! model, originally published at ISMIR 2024. The system uses a transformer-based neural network to detect musical beats and downbeats in audio files with high accuracy.

**Original Paper**: "Beat This! Accurate and Generalizable Beat Tracking"  
**Original Repository**: https://github.com/CPJKU/beat_this

## Features

- **Cross-Platform**: Support for macOS and Windows
- **Multiple Output Formats**: Export beats to `.beats` files, generate audio click tracks, or create mixed audio with original music
- **C++ API**: Clean, type-safe interface with RAII and move semantics
- **ONNX Runtime**: Uses optimized neural network inference
- **Flexible CLI**: Support for individual output formats (beats-only or audio-only)
- **DBN Post-processing**: Optional madmom-compatible Hidden Markov Model (Viterbi) beat tracker (`--dbn` flag) for tempo-constrained output
- **High-Quality Resampling**: r8brain-free-src polyphase FIR resampler (>144 dB SNR) for accurate Mel spectrogram computation

## Architecture

The system consists of five main components:

1. **Audio I/O**: Decode audio files (miniaudio) and convert to mono
2. **Resampling**: Downsample to 22050 Hz using r8brain polyphase FIR filter (>144 dB SNR)
3. **Mel Spectrogram**: Compute 128-band Mel spectrograms via PocketFFT (n_fft=1024, hop=441, Slaney scale)
4. **AI Inference**: Run the transformer model in chunks (1500 frames, 6-frame border) via ONNX Runtime
5. **Post-processing**: Two modes:
   - **Minimal** (default): Peak detection on beat/downbeat logits
   - **DBN** (`--dbn`): madmom-compatible Hidden Markov Model + Viterbi for tempo-constrained tracking

## Dependencies

| Library | Purpose | License |
|---|---|---|
| **ONNX Runtime** | Neural network inference engine | MIT |
| **PocketFFT** | Fast Fourier Transform (Mel spectrogram) | BSD 3-Clause |
| **r8brain-free-src** | High-quality audio resampling (44100 → 22050 Hz) | MIT |
| **miniaudio** | Audio file I/O (decode MP3/WAV/FLAC/OGG) | MIT / Public Domain |

## Building

### Prerequisites

The pre-converted ONNX model is already included in the repository (`onnx/beat_this.onnx`). You can start building and using the application immediately.

If you need to convert a custom model, see [onnx/README.md](onnx/README.md) for detailed instructions on converting PyTorch checkpoints to ONNX format.

```bash
git clone https://github.com/mosynthkey/beat_this_cpp.git
cd beat_this_cpp
git submodule update --init --recursive
mkdir build && cd build
cmake -S . -B build
cmake --build build
```

### Build Options

- **Use system ONNX Runtime**: `cmake -DUSE_SYSTEM_ONNXRUNTIME=ON ..`
- **Specify ONNX Runtime version**: Edit `cmake/FetchONNXRuntime.cmake`

### Manual ONNX Runtime Installation

If you prefer to install ONNX Runtime manually:

1. Download the appropriate ONNX Runtime release for your platform
2. Extract to `ThirdParty/onnxruntime-[platform]/`
3. The build system will automatically detect and use it

## Usage

### Command Line Interface

The application supports flexible output options:

**Beat information only**:
```bash
./beat_this_cpp onnx/beat_this.onnx input.wav --output-beats output.beats
```

**Audio click track only**:
```bash
./beat_this_cpp onnx/beat_this.onnx input.wav --output-audio click_track.wav
```

**Mixed audio (original music + click track)**:
```bash
./beat_this_cpp onnx/beat_this.onnx input.wav --output-mixed mixed.wav
```

**Multiple outputs**:
```bash
./beat_this_cpp onnx/beat_this.onnx input.wav --output-beats output.beats --output-audio clicks.wav --output-mixed mixed.wav
```

**DBN post-processing** (madmom-compatible, higher accuracy):
```bash
./beat_this_cpp onnx/beat_this.onnx input.wav --output-beats output.beats --dbn
```

### C++ API Usage

```cpp
#include "beat_this_api.h"

// Initialize with minimal post-processing (default)
BeatThis::BeatThis analyzer("beat_this.onnx");

// Or enable DBN post-processing
BeatThis::BeatThis analyzer_dbn("beat_this.onnx", /*use_dbn=*/true);

// Load and process audio
std::vector<float> audio_data = /* load your audio */;
auto result = analyzer.process_audio(audio_data, 44100, 2);

// Access results directly
std::cout << "Found " << result.beats.size() << " beats\n";
for (size_t i = 0; i < result.beats.size(); ++i) {
    std::cout << "Beat " << i << ": time=" << result.beats[i] 
              << "s, count=" << result.beat_counts[i] << "\n";
}
```

## File Formats

### Input Audio
- **Supported formats**: WAV, FLAC, OGG, MP3 (decoded via miniaudio)
- **Automatic processing**: Stereo → mono conversion, resampling

### Output Beats File
The `.beats` file format contains tab-separated values:
```
0.340    4
0.681    1
1.023    2
1.364    3
1.705    4
2.047    1
```
- **Column 1**: Beat time in seconds
- **Column 2**: Beat number (1 = downbeat, 2-4 = other beats)

### Audio Click Track (`--output-audio`)
Generated WAV files contain:
- **Downbeats**: 880 Hz sine wave
- **Other beats**: 440 Hz sine wave
- **Duration**: 0.1 seconds per beat with ADSR envelope

### Mixed Audio (`--output-mixed`)
Mixed audio files combine original music with click track:
- **Original music**: 70% volume, preserved exactly as input
- **Click track**: 30% volume, synchronized with detected beats
- **Format preservation**: Maintains original sample rate and channel configuration
- **Stereo/mono support**: Stereo inputs remain stereo, mono inputs remain mono
- **High fidelity**: No resampling or format conversion to preserve audio quality
- **Duration**: Uses the longer of original audio or beat track duration

## Project Structure

```
beat_this_cpp/
├── Source/
│   ├── beat_this_api.h/cpp       # C++ API interface
│   ├── MelSpectrogram.h/cpp      # Mel spectrogram computation (PocketFFT)
│   ├── InferenceProcessor.h/cpp  # Neural network inference (ONNX Runtime)
│   ├── Postprocessor.h/cpp       # Minimal beat extraction (peak detection)
│   ├── DBNPostprocessor.h/cpp    # DBN beat extraction (HMM + Viterbi)
│   └── main.cpp                  # Command line interface with audio generation
├── Submodule/
│   ├── pocketfft/               # FFT library (BSD 3-Clause)
│   ├── miniaudio/               # Audio I/O (MIT / Public Domain)
│   └── r8brain/                 # High-quality resampler (MIT)
├── onnx/
│   ├── beat_this.onnx           # Pre-converted ONNX model (ready to use)
│   ├── convert_to_onnx.py       # PyTorch to ONNX conversion script
│   ├── beat_this/               # Local beat_this submodule for conversion
│   └── README.md                # ONNX model setup and conversion guide
├── cmake/                        # CMake modules
└── CMakeLists.txt               # Build configuration
```

## API Reference

### BeatResult Structure
```cpp
namespace BeatThis {
    struct BeatResult {
        std::vector<float> beats;        // Beat timestamps in seconds
        std::vector<float> downbeats;    // Downbeat timestamps in seconds  
        std::vector<int> beat_counts;    // Beat numbers (1=downbeat, 2,3,4...=other beats)
    };
}
```

### BeatThis Class
```cpp
namespace BeatThis {
    class BeatThis {
    public:
        // use_dbn: false = minimal peak detection (default), true = DBN Viterbi
        explicit BeatThis(const std::string& onnx_model_path, bool use_dbn = false);
        
        // Process audio from vector
        BeatResult process_audio(
            const std::vector<float>& audio_data,
            int samplerate,
            int channels = 1
        );
        
        // Process audio from raw pointer
        BeatResult process_audio(
            const float* audio_data,
            size_t num_samples,
            int samplerate,
            int channels = 1
        );
    };
}
```

## Windows-Specific Notes

### Running the Application

After a successful build, the executables will be in:
- `build\Release\beat_this_cpp.exe` - Main application
- `build\Release\beat_this_api.dll` - API library

## Model Details

- **Architecture**: Transformer-based neural network
- **Input**: 128-dimensional Mel spectrograms (batch, time, freq)
- **Output**: Beat and downbeat probability logits
- **Training**: Trained on large-scale music datasets from the original Beat This! research
- **Inference**: Chunked processing for long audio files
- **ONNX Compatibility**: Fully compatible with ONNX Runtime, opset version 14

### ONNX Model Information

The included ONNX model (`onnx/beat_this.onnx`) is converted from the official Beat This! PyTorch checkpoint:

- **Source**: https://cloud.cp.jku.at/public.php/dav/files/7ik4RrBKTS273gp/final0.ckpt
- **Input format**: `input_spectrogram` with shape `[1, time_frames, 128]`
- **Output format**: `beat` and `downbeat` logits with shape `[1, time_frames]`
- **Dynamic axes**: Variable time dimension for processing audio of any length
- **Model size**: ~97 MB (includes full transformer architecture)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Note: This C++ implementation is separate from the original Beat This! repository. Please refer to the original project for their licensing terms.

## Acknowledgments

- **Original Beat This! Implementation**: This C++ port is based on the Beat This! model from Johannes Kepler University Linz. Please refer to the [original repository](https://github.com/CPJKU/beat_this) for the original implementation, research paper, and licensing terms.
- **ONNX Runtime**: Microsoft's high-performance inference engine (MIT)
- **PocketFFT**: Martin Reinecke's header-only FFT library (BSD 3-Clause)
- **r8brain-free-src**: Aleksey Vaneev's high-quality sample rate converter (MIT) — [github.com/avaneev/r8brain-free-src](https://github.com/avaneev/r8brain-free-src)
- **miniaudio**: David Reid's single-header audio library for file I/O (MIT / Public Domain)
- **madmom** (algorithm reference): The DBN post-processing is a C++ reimplementation of madmom's `DBNDownBeatTrackingProcessor` (Sebastian Böck et al., BSD 2-Clause)