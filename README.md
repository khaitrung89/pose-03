# Pose-03: 18-Pose Character Sheet Generator

Automated character sheet generation system using Qwen-Image-Edit models for ComfyUI.

## 🎯 Features

- **18 unique poses** in 2 optimized grids
- **Batch A**: 10 body shots (full & half body) → 3840×2048
- **Batch B**: 8 close-ups (face & angles) → 3072×2048
- **LoRA-enhanced** for pose control & character consistency
- **Optimized sampling** with AuraFlow & CFG normalization

## 📁 Project Files

| File | Description |
|------|-------------|
| `pose-03-18poses-workflow.json` | **Main workflow** - Import to ComfyUI |
| `18-POSES-GUIDE.md` | **Complete documentation** - Poses, prompts, settings |
| `Qwen Image Edit 2509.json` | Original Qwen workflow reference |
| `README.md` | This file |

## 🚀 Quick Start

### 1. Install Requirements

**Models needed:**
```
✅ Qwen-Image-Edit-Rapid-AIO (or Qwen-Image-Edit-2509)
✅ qwen_2.5_vl_7b_fp8_scaled.safetensors
✅ qwen_image_vae.safetensors
```

**LoRAs recommended:**
```
✅ qwen_pose_control_lora.safetensors
✅ qwen_character_consistency_lora.safetensors
✅ qwen_multi_angle_lora.safetensors
```

### 2. Import Workflow

1. Open ComfyUI
2. Drag & drop `pose-03-18poses-workflow.json`
3. Workflow will auto-load all nodes

### 3. Configure Input

1. Load your character reference image (768×1024)
2. Update **Node 10** (LoadImage) with your file
3. Adjust prompts if needed (optional)

### 4. Run Generation

1. Click **Queue Prompt**
2. Wait ~5-8 minutes (depends on hardware)
3. Find outputs in ComfyUI output folder:
   - `BatchA_BodyShots_Grid_XXXXXX.png`
   - `BatchB_CloseUps_Grid_XXXXXX.png`

## 📊 Output Examples

### Batch A - Body Shots Grid (3840×2048)
```
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ Full    │ Full    │ Full    │ Full    │ Half    │
│ Front   │ Right   │ Left    │ Back    │ Front   │
├─────────┼─────────┼─────────┼─────────┼─────────┤
│ Half    │ Half    │ Half    │ Half    │ Half    │
│ Back    │ R45°    │ L45°    │ Right   │ Left    │
└─────────┴─────────┴─────────┴─────────┴─────────┘
```

### Batch B - Close-ups Grid (3072×2048)
```
┌─────────┬─────────┬─────────┬─────────┐
│ Face    │ Face    │ Face    │ Over-   │
│ Front   │ Right   │ Left    │ Shldr R │
├─────────┼─────────┼─────────┼─────────┤
│ Over-   │ Top-    │ Bottom- │ Wide    │
│ Shldr L │ Down    │ Up      │ Angle   │
└─────────┴─────────┴─────────┴─────────┘
```

## 🔧 Configuration

### Sampling Parameters (Optimized)

**Batch A (Body Shots):**
- Steps: 30
- CFG: 6.5
- Denoise: 0.70
- Sampler: euler_ancestral

**Batch B (Close-ups):**
- Steps: 30
- CFG: 6.5
- Denoise: 0.65 (lower for facial detail preservation)
- Sampler: euler_ancestral

### LoRA Strengths

```
Pose Control:           0.85
Character Consistency:  0.95
Multi-Angle:           0.80
```

## 📖 Documentation

See **[18-POSES-GUIDE.md](./18-POSES-GUIDE.md)** for:
- Complete pose definitions
- Detailed prompt templates
- Troubleshooting guide
- Advanced customization
- Quality checklist

## 🎨 Workflow Architecture

```
Input Image (768×1024)
    ↓
Base Models (Qwen-Image-Edit-Rapid-AIO + CLIP + VAE)
    ↓
LoRA Stack (Pose + Consistency + Multi-Angle)
    ↓
Optimization (AuraFlow + CFG Norm)
    ↓
    ├─→ Batch A Pipeline → Grid A (3840×2048)
    └─→ Batch B Pipeline → Grid B (3072×2048)
```

## 🎯 18 Poses Breakdown

### Batch A (10 poses):
1. Full Front
2. Full Right (90°)
3. Full Left (90°)
4. Full Back
5. Half Front
6. Half Back
7. Half R45°
8. Half L45°
9. Half Right (90°)
10. Half Left (90°)

### Batch B (8 poses):
1. Face Front
2. Face Right
3. Face Left
4. Over-Shoulder Right
5. Over-Shoulder Left
6. Top-Down
7. Bottom-Up
8. Wide-Angle

## 💡 Tips

**For best results:**
- Use clean, high-quality reference image (768×1024 minimum)
- Keep character description detailed in prompts
- Don't modify LoRA loading order
- Monitor VRAM usage (reduce steps if needed)
- Use fixed seed for reproducible results

**Common adjustments:**
- **More consistency**: Increase character_consistency_lora to 1.0
- **Better poses**: Increase pose_control_lora to 0.90
- **Clearer angles**: Increase multi_angle_lora to 0.85
- **Faster generation**: Reduce steps to 20-25

## 🛠️ System Requirements

**Minimum:**
- GPU: 8GB VRAM
- RAM: 16GB
- Storage: 20GB free (for models)

**Recommended:**
- GPU: 12GB+ VRAM (RTX 3060 12GB or better)
- RAM: 32GB
- Storage: SSD with 50GB+ free

## 📊 Performance

| Hardware | Batch A | Batch B | Total Time |
|----------|---------|---------|------------|
| RTX 3060 12GB | ~3 min | ~2 min | ~5 min |
| RTX 4090 24GB | ~90 sec | ~60 sec | ~2.5 min |
| RTX 4070 Ti 12GB | ~2 min | ~90 sec | ~3.5 min |

*Times are approximate and vary based on settings*

## 🔄 Comparison with Original

| Feature | Original (Qwen Image Edit 2509.json) | This Workflow (pose-03-18poses) |
|---------|--------------------------------------|----------------------------------|
| **Poses** | 1 single output | 18 poses in 2 grids |
| **LoRA** | ❌ None | ✅ 3 LoRAs (pose/consistency/angle) |
| **Batch** | Single image | Dual batch (10+8) |
| **Denoise** | 1.0 (full generation) | 0.70/0.65 (editing mode) |
| **CFG** | 2.5 (very low) | 6.5 (balanced) |
| **Steps** | 20 | 30 |
| **Output** | 1 image | 2 grids (optimized layouts) |
| **Purpose** | General image editing | Character sheet creation |

## 🚨 Troubleshooting

**Problem: Character looks different across poses**
→ Increase `character_consistency_lora` strength to 1.0

**Problem: Poses are not accurate**
→ Increase `pose_control_lora` strength to 0.90+

**Problem: VRAM out of memory**
→ Reduce steps to 20, or disable one batch and run separately

**Problem: Generation too slow**
→ Use "euler" sampler instead of "euler_ancestral"

**Problem: Blurry faces in Batch B**
→ Reduce Batch B denoise to 0.60, increase CFG to 7.0

See **18-POSES-GUIDE.md** for complete troubleshooting guide.

## 📝 Notes

- **LoRA files must be compatible** with Qwen models
- If LoRAs unavailable, workflow can run with base model only (lower quality)
- Input image quality directly affects output quality
- Background should be clean/simple for best results

## 🤝 Credits

- **Models**: Qwen-Image-Edit series (Alibaba/SeaArt)
- **Framework**: ComfyUI
- **Workflow Design**: pose-03 project
- **Version**: 1.0.0

## 📜 License

This workflow is provided as-is for personal and commercial use.
Model licenses follow their respective terms (Qwen models, LoRAs, etc.)

---

**For detailed documentation, see [18-POSES-GUIDE.md](./18-POSES-GUIDE.md)**

**Questions or issues?** Check the troubleshooting section in the guide or review your node connections.

*Last updated: 2025-11-15*
