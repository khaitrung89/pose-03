# Pose-03: Character Pose Generation with Qwen Models

Optimized workflows for character pose generation using Qwen-Image-Edit models in ComfyUI.

## ⚠️ Important Notice

**The automated 18-pose workflow (`pose-03-18poses-workflow.json`) uses custom nodes that are NOT available in standard ComfyUI and will not work.**

**✅ Recommended approach:** Use `qwen-optimized-single-pose.json` and generate 18 poses individually.

See **[WORKFLOW-COMPARISON.md](./WORKFLOW-COMPARISON.md)** for full explanation.

---

## 🚀 Quick Start (Recommended)

### **Use:** `qwen-optimized-single-pose.json`

1. **Download workflow:**
   - `qwen-optimized-single-pose.json`

2. **Import to ComfyUI:**
   - Drag & drop into ComfyUI interface

3. **Install required models:**
   ```
   ✅ Qwen-Image-Edit-2509-GGUF-Q8_0 (or Rapid-AIO)
   ✅ qwen_2.5_vl_7b_fp8_scaled.safetensors
   ✅ qwen_image_vae.safetensors
   ✅ qwen_character_consistency_lora.safetensors (optional)
   ```

4. **Load character reference image**
   - Node #38: Load your character (768×1024 recommended)

5. **Generate poses:**
   - Follow prompts from **[18-POSES-PROMPTS.md](./18-POSES-PROMPTS.md)**
   - Run 18 times for 18 different poses

6. **Create grids:**
   - Use Photoshop/GIMP/ImageMagick to assemble into grids
   - See guide in [WORKFLOW-COMPARISON.md](./WORKFLOW-COMPARISON.md)

---

## 📁 Files Overview

| File | Status | Description |
|------|--------|-------------|
| **qwen-optimized-single-pose.json** | ✅ **RECOMMENDED** | Optimized workflow for single pose generation |
| **18-POSES-PROMPTS.md** | ✅ **ESSENTIAL** | Prompt templates for all 18 poses |
| **WORKFLOW-COMPARISON.md** | ✅ **READ THIS** | Explains why 18-pose workflow doesn't work + solutions |
| **Qwen Image Edit 2509.json** | ✅ Works | Original SeaArt workflow |
| **pose-03-18poses-workflow.json** | ❌ Broken | Uses non-existent custom nodes |
| **CONFIGURATION.md** | 📖 Reference | Advanced configuration guide |
| **18-POSES-GUIDE.md** | 📖 Reference | Original concept documentation |
| **README.md** | 📖 You are here | This file |

---

## 🎯 What Changed from Original Workflow?

### ✅ **Optimized Workflow Improvements:**

| Parameter | Original | Optimized | Impact |
|-----------|----------|-----------|--------|
| **Denoise** | 1.0 | **0.70** | Better editing, preserves character |
| **CFG** | 2.5 | **6.5** | Stronger prompt adherence |
| **Steps** | 20 | **30** | Higher quality output |
| **Negative** | Chinese | **English** | Easier to customize |
| **LoRA** | None | **Optional** | Better character consistency |
| **AuraFlow** | 3.0 | **3.5** | Improved sampling |

**Result:** Significantly better quality and character consistency.

---

## 🎨 18 Poses Breakdown

### Batch A (10 poses) - Body Shots
1. Full Front
2. Full Right (90°)
3. Full Left (90°)
4. Full Back
5. Half Front (waist up)
6. Half Back (waist up)
7. Half Right 45°
8. Half Left 45°
9. Half Right (90°)
10. Half Left (90°)

### Batch B (8 poses) - Close-ups
1. Face Front
2. Face Right Profile
3. Face Left Profile
4. Over-Shoulder Right
5. Over-Shoulder Left
6. Top-Down Angle
7. Bottom-Up Angle
8. Wide-Angle Portrait

**See [18-POSES-PROMPTS.md](./18-POSES-PROMPTS.md) for exact prompts.**

---

## ⚙️ Workflow Parameters

### Optimized Settings (Node #72 - KSampler):
```yaml
Seed: randomize (or fixed for consistency)
Steps: 30
CFG: 6.5
Sampler: euler_ancestral
Scheduler: karras
Denoise: 0.70
```

### LoRA Settings (Node #82 - Optional):
```yaml
LoRA: qwen_character_consistency_lora.safetensors
Model Strength: 0.85
CLIP Strength: 0.85
```

**Note:** If LoRA file not available, you can disable Node #82 by:
- Right-click → Bypass
- Or delete the node and reconnect Model/CLIP links

---

## 📊 Performance Estimates

| Hardware | Time per Pose | 18 Poses | Grid Creation | Total |
|----------|---------------|----------|---------------|-------|
| RTX 3060 12GB | ~20s | ~6 min | 1-2 min | ~8 min |
| RTX 4090 24GB | ~10s | ~3 min | 1-2 min | ~5 min |
| RTX 4070 Ti 12GB | ~15s | ~4.5 min | 1-2 min | ~7 min |

---

## 🔧 Creating Final Grids

### Option 1: ImageMagick (Command Line)
```bash
# Install ImageMagick first
# Then run:

# Batch A Grid (5×2)
montage A{1..10}.png -tile 5x2 -geometry 768x1024+0+0 -background white BatchA_Grid.png

# Batch B Grid (4×2)
montage B{1..8}.png -tile 4x2 -geometry 768x1024+0+0 -background white BatchB_Grid.png
```

### Option 2: Photoshop/GIMP
1. Create canvas: 3840×2048 (Batch A) or 3072×2048 (Batch B)
2. Place images in grid: each cell 768×1024
3. Export as PNG

### Option 3: Python Script
See [WORKFLOW-COMPARISON.md](./WORKFLOW-COMPARISON.md) for Python code.

---

## 💡 Tips for Best Results

### For Character Consistency:
1. **Use fixed seed** (e.g., 123456) in KSampler
2. **Enable LoRA** with strength 0.85-0.95
3. **Add detailed character description** to all prompts
4. **Use same input image** for all 18 poses

### For Quality:
1. **High-res input** (768×1024 minimum)
2. **Clean background** in reference image
3. **Increase steps** to 35-40 if needed
4. **Adjust denoise** (0.65 for more detail preservation)

### For Speed:
1. **Reduce steps** to 20-25
2. **Use sampler** `euler` instead of `euler_ancestral`
3. **Lower denoise** to 0.65

---

## 🛠️ System Requirements

**Minimum:**
- GPU: 8GB VRAM
- RAM: 16GB
- Storage: 20GB (for models)
- ComfyUI with SeaArt nodes

**Recommended:**
- GPU: 12GB+ VRAM
- RAM: 32GB
- Storage: SSD with 50GB+ free
- Latest ComfyUI version

---

## 📖 Documentation Guide

**Start here:**
1. **README.md** (this file) - Overview
2. **WORKFLOW-COMPARISON.md** - Why 18-pose workflow doesn't work + solutions
3. **18-POSES-PROMPTS.md** - Copy-paste prompts for all 18 poses

**Advanced:**
4. **CONFIGURATION.md** - Detailed parameter tuning
5. **18-POSES-GUIDE.md** - Original concept documentation

---

## ❓ FAQ

**Q: Why doesn't the 18-pose workflow work?**
A: It uses custom nodes (`VAEDecodeBatch`, `LatentBatchSeedBehavior`, `ImageGridComposite`) that don't exist in ComfyUI. See [WORKFLOW-COMPARISON.md](./WORKFLOW-COMPARISON.md).

**Q: How do I generate 18 poses then?**
A: Use `qwen-optimized-single-pose.json` and run it 18 times with different prompts from [18-POSES-PROMPTS.md](./18-POSES-PROMPTS.md).

**Q: Do I need LoRA files?**
A: No, they're optional. The workflow works without them, but LoRAs improve character consistency.

**Q: Can I use this with standard Qwen models (not SeaArt)?**
A: The workflow uses SeaArt's `TextEncodeQwenImageEditPlus` node. For standard ComfyUI, you'd need to replace with `CLIPTextEncode`.

**Q: How do I ensure character consistency?**
A: Use fixed seed + LoRA + detailed character description in ALL prompts.

**Q: Can I automate the 18 poses?**
A: Not directly in ComfyUI without custom nodes. But you can script it externally (e.g., Python API to ComfyUI).

---

## 🤝 Credits

- **Models**: Qwen-Image-Edit series (Alibaba/SeaArt)
- **Framework**: ComfyUI
- **Original Workflow**: SeaArt
- **Optimization**: pose-03 project

---

## 📝 Quick Reference

**Recommended Workflow:**
```
qwen-optimized-single-pose.json
```

**Prompt Guide:**
```
18-POSES-PROMPTS.md
```

**Troubleshooting:**
```
WORKFLOW-COMPARISON.md
```

**Download Links:**
- Workflow: `https://github.com/khaitrung89/pose-03/blob/main/qwen-optimized-single-pose.json`
- Prompts: `https://github.com/khaitrung89/pose-03/blob/main/18-POSES-PROMPTS.md`

---

## 🚨 Common Issues

**"Node is missing class_type property"**
→ You're trying to load `pose-03-18poses-workflow.json`. Use `qwen-optimized-single-pose.json` instead.

**"Character looks different in each pose"**
→ Use **fixed seed** and **LoRA**. Add detailed character description to prompts.

**"Background is messy"**
→ Add to negative prompt: `complex background, detailed background, scenery`

**"Generation too slow"**
→ Reduce steps to 20-25, use `euler` sampler.

---

**Last updated: 2025-11-15**
**Version: 2.0 (Fixed)**
