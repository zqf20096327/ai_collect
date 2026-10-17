# 🎭 Qwen3-TTS Emotional Voice Clone (Ultimate Edition)

Advanced voice cloning with **80+ emotion presets** and **multi-emotion mixing** for ComfyUI.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![ComfyUI](https://img.shields.io/badge/ComfyUI-compatible-green)
![License](https://img.shields.io/badge/license-GPL--3.0-orange)

## 🌟 Features

### 80+ Emotion Presets
Transform your voice clones with comprehensive emotional range:
- **Core Emotions**: neutral, angry, sad, happy, fearful, disgusted, surprised
- **Intensity Variations**: annoyed → angry → furious → enraged
- **Social/Interpersonal**: sarcastic, mocking, condescending, dismissive, sympathetic, apologetic, pleading
- **Confidence Spectrum**: confident, arrogant, smug, insecure, hesitant, timid, defeated, hopeless
- **Energy Levels**: excited, enthusiastic, energetic, bored, tired, exhausted, lethargic, calm
- **Stress/Tension**: nervous, panicked, frantic, stressed, overwhelmed, relaxed, serene
- **Attitude/Mood**: playful, teasing, flirtatious, seductive, mysterious, ominous, menacing, threatening
- **Physical States**: drunk, breathless, whispering, shouting, in_pain, sick
- **Complex Emotions**: bitter, manic, reluctant, desperate, jealous, frustrated, relieved, guilty, ashamed, proud
- **Character Presets**: rick_like, jerry_like, morty_like (Rick & Morty inspired)

### Multi-Emotion Mixing
- **Primary Emotion**: Main emotional tone (required)
- **Secondary Emotion**: Blend with primary for nuanced delivery (optional)
- **Tertiary Emotion**: Add third layer of complexity (optional)
- **Intensity Control**: 0.0x to 2.0x multiplier for emotion strength

### Voice Cloning Modes
- **Fast Mode** (`x_vector_only=True`): Quick generation, speaker embedding only
- **Accurate Mode** (`x_vector_only=False`): High-quality cloning with reference transcript

## 📋 Requirements

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [ComfyUI-Qwen-TTS](https://github.com/flybirdxx/ComfyUI-Qwen-TTS) (base package)
- Python 3.10+
- CUDA-capable GPU (recommended) or CPU

**Hardware Compatibility**: Works on any system that can run Qwen3-TTS (NVIDIA GPUs, AMD GPUs with ROCm, Mac M1/M2, CPU)

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended - Coming Soon)
1. Open ComfyUI Manager
2. Search for "Qwen3-TTS Emotional"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

**Step 1**: Install the base Qwen3-TTS package first
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/flybirdxx/ComfyUI-Qwen-TTS.git
cd ComfyUI-Qwen-TTS
pip install -r requirements.txt
```

**Step 2**: Add the Emotional Voice Clone node
```bash
# Download qwen3_emotional_clone.py from this repo
# Place it in: ComfyUI/custom_nodes/ComfyUI-Qwen-TTS/
```

**Step 3**: Update `__init__.py`

Add these lines to `ComfyUI/custom_nodes/ComfyUI-Qwen-TTS/__init__.py`:

```python
# Import emotional clone nodes
try:
    from .qwen3_emotional_clone import (
        NODE_CLASS_MAPPINGS as EMOTIONAL_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as EMOTIONAL_DISPLAY
    )
    EMOTIONAL_LOADED = True
except Exception as e:
    print(f"⚠️ Failed to load emotional clone nodes: {e}")
    EMOTIONAL_LOADED = False

# Add to the existing NODE_CLASS_MAPPINGS section
if EMOTIONAL_LOADED:
    NODE_CLASS_MAPPINGS.update(EMOTIONAL_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(EMOTIONAL_DISPLAY)
    print("✅ Emotional Voice Clone node loaded!")
```

**Step 4**: Restart ComfyUI

## 💡 Usage

### Basic Usage

1. **Add the node**: Right-click → `Qwen3-TTS` → `🎭 Qwen3-TTS Emotional Voice Clone (Ultimate)`
2. **Connect reference audio**: Load your voice sample (5-30 seconds recommended)
3. **Enter text**: What you want the voice to say
4. **Select emotion**: Choose from 80+ presets
5. **Generate**: Queue the prompt

### Single Emotion Example
```
Primary Emotion: sad
Secondary Emotion: none
Tertiary Emotion: none
Intensity: 1.0x
Result: Pure sad delivery
```

### Multi-Emotion Mixing Examples

**Bitter (Pre-mixed)**
```
Primary: sad
Secondary: angry
Intensity: 1.0x
= Bitter, resentful tone
```

**Manic Energy**
```
Primary: excited
Secondary: nervous  
Tertiary: breathless
Intensity: 1.5x
= Frantic, overwhelming energy
```

**Maximum Confidence**
```
Primary: confident
Secondary: arrogant
Tertiary: dismissive
Intensity: 2.0x
= Peak smugness and authority
```

**Defeated Character**
```
Primary: defeated
Secondary: apologetic
Tertiary: whispering
Intensity: 1.2x
= Complete emotional breakdown
```

### Advanced Settings

**Fast Generation** (3-5 seconds):
- `x_vector_only`: True (enabled)
- `ref_audio_transcript`: Leave empty
- Good for testing, quick iterations

**High Quality** (15-20 seconds):
- `x_vector_only`: False (disabled)
- `ref_audio_transcript`: Fill in what the reference audio says
- Better voice matching, complete sentences

**Controlling Length**:
- Use **randomize seed** to try different generation lengths
- When you get a good long generation, note the seed
- Use that **fixed seed** for consistent results

## 🎨 Emotion Mixing Tips

### Energy Combinations
- `calm + confident = assured`
- `excited + happy = ecstatic`
- `tired + defeated = hopeless`

### Social Dynamics
- `confident + mocking = smug`
- `nervous + apologetic = submissive`
- `angry + contemptuous = hateful`

### Physical + Emotional
- `breathless + excited = exhilarated`
- `drunk + happy = jolly`
- `whispering + fearful = terrified`

### Character Voices
- **Confident Scientist**: `confident + condescending + dismissive`
- **Nervous Assistant**: `nervous + insecure + apologetic`
- **Anxious Student**: `anxious + overwhelmed + stressed`

## 📊 Parameter Guide

### Emotion Intensity
- **0.0x**: Neutral (no emotion)
- **0.5x**: Subtle hint
- **1.0x**: Normal strength (default)
- **1.5x**: Strong emotion
- **2.0x**: Extreme/exaggerated

### How It Works
The node adjusts three generation parameters based on emotion:
- **Temperature**: Controls randomness/variation
- **Repetition Penalty**: Affects word repetition and flow  
- **Top-p**: Nucleus sampling probability

Emotions are mixed by averaging their parameter adjustments, then multiplied by intensity.

## 🔧 Troubleshooting

### Audio cuts off abruptly
- This is seed-dependent behavior
- Try randomizing seed multiple times
- Use longer input text
- Consider using `x_vector_only=False` with transcript

### Generation too fast (3 seconds)
- This is normal for `x_vector_only=True` mode
- For longer, more accurate generation:
  - Set `x_vector_only=False`
  - Fill in `ref_audio_transcript`
  - Should take 15-20 seconds

### Voice doesn't match reference
- Make sure reference audio is clear (5-30 seconds)
- Try `x_vector_only=False` with accurate transcript
- Use higher quality reference audio (24kHz recommended)

### Node doesn't appear
- Verify base ComfyUI-Qwen-TTS is installed
- Check `__init__.py` was updated correctly
- Look for errors in ComfyUI console
- Try restarting ComfyUI

## 📝 Examples & Workflows

### Sarcastic Scientist
```yaml
Reference Audio: scientist_voice.mp3
Text: "Oh wonderful, another one who thinks they understand quantum mechanics."
Primary: sarcastic
Secondary: condescending
Tertiary: dismissive
Intensity: 1.5x
```

### Defeated Character
```yaml
Reference Audio: character_voice.mp3
Text: "I tried my best, but I guess it wasn't enough."
Primary: defeated
Secondary: sad
Tertiary: whispering
Intensity: 1.8x
```

### Panicked Character
```yaml
Reference Audio: anxious_voice.mp3
Text: "We need to move NOW, there's no time!"
Primary: panicked
Secondary: breathless
Tertiary: stressed
Intensity: 2.0x
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional emotion presets
- Better parameter tuning for specific emotions
- Character-specific preset packs
- Multi-language emotion mapping

## 📜 Credits

- **Emotional Voice Clone Node**: Developed with assistance from Claude (Anthropic)
- **Base Qwen3-TTS**: [Alibaba Qwen Team](https://github.com/QwenLM/Qwen3-TTS)
- **ComfyUI Integration**: [flybirdxx](https://github.com/flybirdxx/ComfyUI-Qwen-TTS)
- **ComfyUI**: [comfyanonymous](https://github.com/comfyanonymous/ComfyUI)

## 📄 License

GPL-3.0 License (matching base Qwen3-TTS package)

## 🔗 Links

- [Qwen3-TTS Official Repo](https://github.com/QwenLM/Qwen3-TTS)
- [ComfyUI-Qwen-TTS Base Package](https://github.com/flybirdxx/ComfyUI-Qwen-TTS)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 💬 Support

- Issues: [GitHub Issues](#)
- Discussions: [GitHub Discussions](#)
- Discord: ComfyUI Community Server

---

**Made with 🎭 for the ComfyUI community**
