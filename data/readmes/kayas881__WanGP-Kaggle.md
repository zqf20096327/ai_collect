# WanGP on Kaggle - Universal Video Generation

Run powerful video generation models on Kaggle's free Tesla T4 GPU (15GB VRAM) using WanGP's optimized interface!

## 📸 Screenshots

### WanGP Interface
![WanGP Interface](images/wan.jpeg)

![Models](images/wan_models.jpeg)

![Models](images/wan2.jpeg)

### Kaggle
![kaggle](images/kaggle.jpeg)

![kaggle](images/kaggle2.jpeg)

## 🚀 Quick Start

1. Upload the notebook to Kaggle
2. Enable GPU: **Settings → Accelerator → GPU T4 x2**
3. Enable Internet: **Settings → Internet → On**
4. Run cells 1-5 to install dependencies
5. **Important**: After installation completes, restart the kernel:
   - Click the **▶ Run** button at the top
   - Select **"Restart and Clear Cell Outputs"**
6. Run the final cell to start WanGP
7. Access the Gradio URL (printed in output)

## ⚠️ Important: Kernel Restart Required

After running cells 1-5 (dependency installation), you **must** restart the kernel before running the WanGP interface. This prevents import errors and ensures all packages load correctly.

**How to restart:**
1. Click **▶ Run** button in the top toolbar
2. Select **"Restart and Clear Cell Outputs"**
3. Run the final cell again to launch WanGP

## 🎬 Supported Video Models

WanGP supports multiple state-of-the-art video generation models:

### Available Models
- **Wan 2.2** - Latest Wan model with improved quality
- **Wan 2.1** - Previous generation Wan model
- **LTX Video** - Fast and efficient video generation
- **Hunyuan Video** - High-quality video model
- **Hunyuan Video 1.5** - Enhanced version
- **Flux 1** - Image-to-video capabilities
- **Flux 2** - Improved Flux model
- **Qwen** - Multilingual video generation
- **Z-Image** - Specialized image processing
- **Kandinsky 5** - Artistic style video
- **TTS** - Text-to-speech integration
- **CogVideoX** - Advanced video understanding
- **Ovi 10B** - Lightweight video model

And many more! Check the model dropdown in the WanGP interface for the complete list.

## 🎯 Using Different Models

### Switching Models
1. Open WanGP in your browser using the Gradio link
2. Click the model dropdown (top-left, default is "Wan2.2")
3. Select any model from the list
4. Choose the task type (Text2video, Image2video, Animate, etc.)
5. Configure settings and generate!

### Model Features
- **Text2Video**: Generate videos from text prompts
- **Image2Video**: Animate static images
- **Text+Image2Video**: Combine text and image inputs
- **Lucy Edit**: Video editing capabilities
- **Vace**: Video acceleration

## 📦 What's Included

This notebook provides:
- ✅ Full WanGP installation with all dependencies
- ✅ Optimized for Tesla T4 GPU (SageAttention v1.0.6)
- ✅ Memory management system (mmgp) for large models
- ✅ Lightning LoRAs pre-configured for 4-step generation
- ✅ Automatic Gradio public URL
- ✅ Storage optimization using `/tmp`

## 💾 Storage & Memory

### Storage Management
- The notebook automatically symlinks the `ckpts` folder to `/kaggle/tmp/`
- This provides access to ~73GB of temp storage
- Models are downloaded automatically when selected
- Generated videos are saved to the `outputs` folder

### Memory Optimization
WanGP includes **mmgp** (Memory Management for GPU Poor):
- Automatic model offloading when VRAM is low
- Partial model pinning to RAM
- Async loading for faster inference
- Works seamlessly on T4's 15GB VRAM

## ⚙️ Configuration

### Profile Settings
The notebook uses `--profile 4` which is optimized for:
- Tesla T4 / RTX 20XX series GPUs
- 15GB VRAM
- Balanced speed/quality

### Attention Mode
Uses `--attention sage` (SageAttention):
- Optimized for T4 architecture
- Faster than standard attention
- Maintains quality

### Lightning LoRAs
Pre-configured with 4-step lightning LoRAs:
- Significantly faster generation
- Minimal quality loss
- Automatically loaded for supported models

## 🔧 Troubleshooting

### Import Errors After Installation
**Solution**: Restart the kernel (see "Important: Kernel Restart Required" section above)

### "Out of VRAM" Errors
- T4 has 15GB VRAM - some models may require offloading
- mmgp handles this automatically
- Generation will be slower but will complete

### Gradio Link Expired
- Gradio free tier provides temporary links (expire in ~1 week)
- Restart the final cell to get a new URL

### Models Not Loading
- Models download automatically on first use
- Check your internet connection
- Ensure enough storage space in `/tmp`

### Plugin Errors
Some optional plugins may show errors (like `wan2gp-video-mask-creator`):
- These are non-critical and won't affect core functionality
- Main video generation features work normally

## 📝 Generation Tips

### Text Prompts
- Be specific and detailed
- Include style, lighting, camera movement
- Example: *"Cinematic close-up shot of a sunset over ocean, warm golden hour lighting, slow camera pan right"*

### Settings
- **Steps**: 4 (with Lightning LoRA) or 20-50 (standard)
- **Resolution**: 480p recommended for T4, 720p+ may be slower
- **Seed**: Use same seed for consistent results

### Performance
- First generation takes longer (model loading)
- Subsequent generations are faster (model cached)
- Expect ~9-15 minutes per video on T4

## 📤 Downloading Results

Generated videos are saved in the `outputs` folder:
1. Click the generated video in the WanGP interface
2. Use the download button in the video player
3. Or access files directly from Kaggle's file browser

## 🆘 Need Help?

1. Check the WanGP console output for detailed logs
2. Verify kernel was restarted after installation
3. Ensure GPU and Internet are enabled in Kaggle settings
4. Try a different model if one fails to load

## ⏱️ Session Limits

- Kaggle sessions last up to 9 hours
- The Gradio link expires in 1 week
- Download your videos before the session ends
- You can restart the notebook anytime for a new session

---

**Note**: This notebook uses the WanGP project by DeepBeepMeep, which provides an optimized interface for running multiple video generation models with efficient memory management.
