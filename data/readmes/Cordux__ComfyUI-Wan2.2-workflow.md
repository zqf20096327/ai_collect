# Wan 2.2 14B Low-VRAM Workflow for ComfyUI

Generate high-quality text-to-video and image-to-video content using Wan 2.2 14B on budget hardware!

**🚀 Performance Highlight:** Generate a 1-second video in under 5 minutes on an RTX 3050 6GB!

## ✨ Features

- **Low VRAM Optimization** - Works on 6GB VRAM cards (RTX 3050, 3060, AMD equivalents)
- **User-Friendly Interface** - Simple FPS & Seconds input (automatic frame calculation)
- **Dual Mode Support** - Text-to-Video (t2v) and Image-to-Video (i2v) with easy switching
- **Last Frame Extraction** - Optional last frame saving for video chaining/extension
- **GGUF Quantization** - Leverages quantized models for memory efficiency
- **Smart Memory Management** - Aggressive CPU offloading for low-VRAM systems
- **Fast Generation** - 4-step sampling for rapid results

<details>
   <summary>🖼️ Screenshot</summary>
   <img width="1753" height="1020" alt="image" src="https://github.com/user-attachments/assets/7c00817f-c3c9-4d11-8130-7c59f360ef44" />
</details>

## 📋 System Requirements

### Minimum
- **VRAM:** 6GB (RTX 3050, 3060 6GB, AMD equivalents)
- **System RAM:** 16GB
- **Storage:** ~15GB for models

### Recommended
- **VRAM:** 8GB+
- **System RAM:** 32GB
- **Storage:** SSD for faster model loading

<details>
   <summary>
      <h3>🔧 Required Custom Nodes</h3>
   </summary>

   Install these ComfyUI custom nodes (via ComfyUI Manager or manual installation):
   
   1. **[rgthree-comfy](https://github.com/rgthree/rgthree-comfy)** - Context system, workflow organization, group muting
   2. **[cg-use-everywhere](https://github.com/chrisgoringe/cg-use-everywhere)** - Global parameter distribution
   3. **[ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)** - LoRA loading and model management
   4. **[ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)** - Video processing and frame selection
   5. **[ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)** - Utility nodes
   6. **[ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)** - GGUF model loading (CRITICAL for this workflow)
   7. **[comfyui_memory_cleanup](https://github.com/LAOGOU-666/Comfyui-Memory_Cleanup)** - Memory management for low-VRAM
   8. **[ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)** - Math expression nodes
   9. **[efficiency-nodes-comfyui](https://github.com/jags111/efficiency-nodes-comfyui)** - Workflow efficiency nodes

</details>

<details>
   <summary><h3>Quick Installation via ComfyUI Manager</h3></summary>

   1. Open ComfyUI Manager
   2. Click "Install Custom Nodes"
   3. Search for each node pack above
   4. Click "Install" on each
   5. Restart ComfyUI

</details>

<details>
   <summary><h3>Manual Installation</h3></summary>

```bash
cd ComfyUI/custom_nodes

git clone https://github.com/rgthree/rgthree-comfy
git clone https://github.com/chrisgoringe/cg-use-everywhere
git clone https://github.com/yolain/ComfyUI-Easy-Use
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
git clone https://github.com/kijai/ComfyUI-KJNodes
git clone https://github.com/city96/ComfyUI-GGUF
git clone https://github.com/LAOGOU-666/Comfyui-Memory_Cleanup
git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts
git clone https://github.com/jags111/efficiency-nodes-comfyui

# Restart ComfyUI
```

</details>

<details>
   <summary><h3>📥 Required Model Files</h3></summary>

This workflow uses the **wan2.2-t2v-rapid-aio-v10-nsfw GGUF** model from [Phr00t/befox rapid merge](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF).

### Important Naming Note
The "D" prefix you may see in some screenshots (e.g., `Dwan2.2-t2v-rapid-aio-v10-nsfw-Q3_K.gguf`) is just my local folder organization. **Download files with their original names** as shown below - ComfyUI will load them correctly from the standard model folders.

---

### 1. Main Model (GGUF) - Choose based on your VRAM

**Repository:** https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/tree/main/v10

**Recommended for 6-8GB VRAM:** Q3_K or Q4_K

#### Q3_K (~8 GB total memory, very low VRAM friendly)
- **Download:** [wan2.2-t2v-rapid-aio-v10-nsfw-Q3_K.gguf](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/resolve/main/v10/wan2.2-t2v-rapid-aio-v10-nsfw-Q3_K.gguf?download=true)
- **Placement:** `ComfyUI/models/unet` or `models/checkpoints`

#### Q4_K (~9-10 GB total memory, good balance) ⭐ Recommended
- **Download:** [wan2.2-t2v-rapid-aio-v10-nsfw-Q4_K.gguf](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/resolve/main/v10/wan2.2-t2v-rapid-aio-v10-nsfw-Q4_K.gguf?download=true)
- **Placement:** `ComfyUI/models/unet` or `models/checkpoints`

#### Q5_K (~11-12 GB total memory, higher quality)
- **Download:** [wan2.2-t2v-rapid-aio-v10-nsfw-Q5_K.gguf](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/resolve/main/v10/wan2.2-t2v-rapid-aio-v10-nsfw-Q5_K.gguf?download=true)
- **Placement:** `ComfyUI/models/unet` or `models/checkpoints`

---

### 2. Text Encoder / CLIP (umt5-xxl GGUF)

**Repository:** https://huggingface.co/city96/umt5-xxl-encoder-gguf/tree/main

**Recommended:** Q3_K_M (lowest VRAM usage, good performance)

#### Q3_K_M (~3 GB) ⭐ Recommended
- **Download:** [umt5-xxl-encoder-Q3_K_M.gguf](https://huggingface.co/city96/umt5-xxl-encoder-gguf/resolve/main/umt5-xxl-encoder-Q3_K_M.gguf?download=true)
- **Placement:** `ComfyUI/models/clip` or `models/text_encoders`

#### Q4_K_M (~3.7 GB, slightly higher quality)
- **Download:** [umt5-xxl-encoder-Q4_K_M.gguf](https://huggingface.co/city96/umt5-xxl-encoder-gguf/resolve/main/umt5-xxl-encoder-Q4_K_M.gguf?download=true)
- **Placement:** `ComfyUI/models/clip` or `models/text_encoders`

---

### 3. VAE

**Repository:** https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/vae

#### wan_2.1_vae.safetensors (~254 MB)
- **Download:** [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)
- **Placement:** `ComfyUI/models/vae`

</details>

---

### Quick Tips
- Verify file hashes after download (Hugging Face shows them on each file page)
- If links change, search Hugging Face for "WAN2.2-14B-Rapid-AllInOne-GGUF" (befox), "umt5-xxl-encoder-gguf" (city96), or "Wan_2.2_ComfyUI_Repackaged" (Comfy-Org)
- **For best low-VRAM performance:** Use Q3_K or Q4_K model + Q3_K_M CLIP + standard Wan VAE

### Recommended Configurations by VRAM

| VRAM | Main Model | Text Encoder | Total Memory | Performance |
|------|------------|--------------|--------------|-------------|
| 6GB  | Q3_K       | Q3_K_M       | ~11GB system | Fast, good quality |
| 8GB  | Q4_K       | Q3_K_M       | ~13GB system | Balanced ⭐ |
| 10GB+ | Q5_K      | Q4_K_M       | ~15GB system | High quality |

---

<details>
   <summary><h3>🎬 How to Use</h3></summary>

   ### Basic Workflow
   
   1. **Load the workflow** in ComfyUI
   2. **Set your parameters:**
      - Width: 512 (default)
      - Height: 512 (default)
      - Seconds: 10 (duration of video)
      - FPS: 15 (frames per second)
      - *Frames are calculated automatically!*
   3. **Choose mode:**
      - Text-to-Video (t2v): Generate from text prompt
      - Image-to-Video (i2v): Animate from input image
   4. **Enter your prompt** (positive and negative)
   5. **Queue prompt** and generate!
   
   ### Text-to-Video (t2v) Mode
   
   1. Make sure "Load Image" node is **disabled/muted**
   2. Enter your text prompt describing the video
   3. Queue prompt
   
   ### Image-to-Video (i2v) Mode
   
   1. **Enable** the "Load Image" node
   2. Load your input image
   3. Enter your prompt (can enhance/modify the image animation)
   4. Queue prompt
   
   ### Last Frame Extraction (Optional)
   
   The workflow includes automatic last frame saving for video chaining:
   
   - **Enabled by default** - Last frame is automatically saved
   - **To disable:** Mute the "Save the Last Frame" group using rgthree Group Muter
   - **Use case:** Chain multiple generations together for longer videos
</details>

---


<details>
   <summary><h3>⚙️ Workflow Features Explained</h3></summary>

   ### Automatic Frame Calculation
   - Input: FPS × Seconds
   - Calculation: `(FPS × Seconds) + 1`
   - The +1 frame is required for Wan's t2v initialization
   - Works for both t2v and i2v modes automatically
   
   ### Memory Optimization
   - GGUF quantization reduces model size
   - Aggressive CPU offloading (~9GB offloaded to system RAM)
   - Dynamic memory management between pipeline stages
   - Memory cleanup nodes for low-VRAM systems
   
   ### Mode Switching
   - Clean interface with POS/NEG/Switch nodes
   - One control point switches both two paths (Text2Image and Image2Video) simultaneously
   - No manual rewiring needed between modes
</details>

---

<details>
   <summary><h3>🐛 Troubleshooting</h3></summary>
   
   ### "Out of Memory" Errors
   - Drop to Q3_K model instead of Q4_K
   - Close other applications to free system RAM
   - Enable Windows page file (set to system managed)
   - Reduce video length (fewer seconds)
   
   ### "Missing Nodes" Error
   - Install all required custom nodes (see list above)
   - Use ComfyUI Manager's "Install Missing Nodes" feature
   - Restart ComfyUI after installing nodes
   
   ### GGUF Models Not Loading
   - Ensure ComfyUI-GGUF is installed correctly
   - Verify model files are in correct folders with exact filenames
   - Check that files downloaded completely (verify file sizes)
   
   ### Poor Quality Output
   - Try Q4_K or Q5_K model if you have more VRAM
   - Increase steps (though 4 steps works well with this model)
   - Adjust prompt strength and detail
   - Use better quality input images for i2v mode
   
   ### Slow Generation
   - This is normal for low-VRAM setups (CPU offloading takes time)
   - Expected: ~5 minutes for 1 second video on RTX 3050 6GB
   - Close background applications
   - Ensure models are on SSD for faster loading
</details>

---

<details>
   <summary><h3>🎯 Performance Benchmarks</h3></summary>

   ### RTX 3050 6GB (Tested Configuration)
   - **Model:** Q4_K + Q3_K_M CLIP
   - **Video length:** 1 second (16 frames @ 15 FPS)
   - **Total time:** ~4.6 minutes
     - Model loading: ~1 min
     - Sampling (4 steps): ~1.8 min
     - VAE decode: ~30s
   - **Quality:** Good, suitable for most use cases
   
   ### Expected Performance on Other Cards
   - **RTX 3060 12GB:** ~3 minutes (less offloading overhead)
   - **RTX 4060 8GB:** ~2.5 minutes (faster architecture)
   - **RTX 4070 12GB:** ~2 minutes (minimal offloading)
   
   *Times are approximate and depend on system configuration*
</details>

---

### Optional LoRAs
The workflow supports standard LoRA loading through the EasyUse nodes. 
You can add any compatible Wan 2.2 LoRAs to enhance or modify output.

---

## 📚 Additional Resources

- [Wan 2.2 Official Repository](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ComfyUI Documentation](https://github.com/comfyanonymous/ComfyUI)
- [GGUF Quantization Info](https://github.com/city96/ComfyUI-GGUF)
- [befox Rapid Model Info](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF)

---

## 🤝 Contributing

This workflow is released into the public domain with no restrictions. Use it however you want - personal, commercial, modified, redistributed.

Contributions, improvements, and forks are welcome! No attribution required, but appreciated! ❤️

---

## 🙏 Credits

- **befox** - GGUF quantized Wan models
- **city96** - ComfyUI-GGUF loader and umt5-xxl encoder
- **Comfy-Org** - Wan 2.2 repackaged models
- **ComfyUI community** - All the amazing custom node developers

---

## 📜 License

This workflow is released into the public domain with no restrictions.

**You are free to:**
- Use commercially
- Modify and redistribute
- Use in closed-source projects
- Not provide attribution (though it's appreciated!)

No warranty provided. Use at your own risk.

---

## 💬 Support & Feedback

If you find this workflow helpful:
- ⭐ Star this repository
- 🐛 Report issues or bugs
- 💡 Suggest improvements
- 📢 Share with the community!
