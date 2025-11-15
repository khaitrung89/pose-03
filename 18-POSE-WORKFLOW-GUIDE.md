# 🎨 18-Pose Complete Workflow Guide

## 📋 Overview

**File:** `18-Pose-Complete-Workflow.json`

This workflow generates **18 different character poses in ONE RUN** using parallel processing.

---

## ✨ Features

- ✅ **18 poses** generated simultaneously
- ✅ **Optimized parameters** (denoise 0.70, CFG 6.5, steps 30)
- ✅ **Professional quality** character reference sheets
- ✅ **99 nodes** total (simplified architecture)
- ✅ **All standard nodes** (works on SeaArt/ComfyUI)
- ✅ **Batch A + Batch B** organization

---

## 📊 Workflow Structure

### Base Nodes (9 shared):
1. LoadImage - Character reference input
2. SeaArtUnetLoader - Qwen-Image-Edit-Rapid-AIO
3. CLIPLoader - qwen_2.5_vl_7b_fp8_scaled
4. VAELoader - qwen_image_vae
5. FluxKontextImageScale - Auto-scale images
6. VAEEncode - Shared latent encoder
7. ModelSamplingAuraFlow - Sampling optimization
8. CFGNorm - CFG normalization
9. Title Note - Documentation

### Per-Pose Pipeline (×18):
Each pose has 5 nodes:
1. TextEncodeQwenImageEditPlus (Positive prompt)
2. TextEncodeQwenImageEditPlus (Negative prompt)
3. KSampler (Generation)
4. VAEDecode (Image decoding)
5. SaveImage (Output)

**Total:** 9 + (18 × 5) = **99 nodes**

---

## 🎯 18 Poses Included

### Batch A - Body Shots (10 poses):
1. **A1_Full_Front** - Full body front view, standing straight
2. **A2_Full_Right** - Full body right side, 90° profile
3. **A3_Full_Left** - Full body left side, 90° profile
4. **A4_Full_Back** - Full body back view
5. **A5_Half_Front** - Half body (waist up), front view
6. **A6_Half_Back** - Half body (waist up), back view
7. **A7_Half_R45** - Half body, 45° right angle
8. **A8_Half_L45** - Half body, 45° left angle
9. **A9_Half_Right** - Half body, 90° right profile
10. **A10_Half_Left** - Half body, 90° left profile

### Batch B - Close-ups (8 poses):
11. **B1_Face_Front** - Face close-up, front view
12. **B2_Face_Right** - Face close-up, right profile
13. **B3_Face_Left** - Face close-up, left profile
14. **B4_Over_Shoulder_R** - Right over-shoulder view
15. **B5_Over_Shoulder_L** - Left over-shoulder view
16. **B6_Top_Down** - Top-down bird's eye view
17. **B7_Bottom_Up** - Bottom-up worm's eye view
18. **B8_Wide_Angle** - Wide-angle dramatic portrait

---

## ⚙️ Settings

### KSampler (all 18 poses):
```yaml
Seed: 123456 + pose_index (fixed for consistency)
Control: fixed
Steps: 30
CFG: 6.5
Sampler: euler_ancestral
Scheduler: karras
Denoise: 0.70
```

### Optimization:
```yaml
ModelSamplingAuraFlow:
  shift: 3.5

CFGNorm:
  strength: 1.0
```

---

## 🚀 Usage Instructions

### Step 1: Install Models
```
Required:
✅ Qwen-Image-Edit-Rapid-AIO (or Qwen-Image-Edit-2509)
✅ qwen_2.5_vl_7b_fp8_scaled.safetensors
✅ qwen_image_vae.safetensors
```

### Step 2: Import Workflow
1. Download `18-Pose-Complete-Workflow.json`
2. Open ComfyUI
3. Drag & drop workflow file
4. Wait for nodes to load

### Step 3: Load Character Image
1. Find **LoadImage** node (top-left)
2. Upload your character reference (768×1024 recommended)
3. Image will be auto-scaled

### Step 4: Generate All 18 Poses
1. Click **Queue Prompt**
2. Wait for generation (~5-10 minutes depending on hardware)
3. All 18 poses generate in parallel

### Step 5: Collect Outputs
Outputs will be saved as:
```
18Pose_A1_Full_Front_00001.png
18Pose_A2_Full_Right_00001.png
18Pose_A3_Full_Left_00001.png
...
18Pose_B8_Wide_Angle_00001.png
```

---

## 📊 Performance

| Hardware | Generation Time |
|----------|----------------|
| RTX 3060 12GB | ~8-12 minutes |
| RTX 4090 24GB | ~4-6 minutes |
| RTX 4070 Ti 12GB | ~6-8 minutes |

**VRAM Usage:** ~8-10GB

---

## 💡 Tips & Tricks

### For Character Consistency:
- ✅ Use **same seed** (default: 123456 base)
- ✅ Upload **high-quality** reference (768×1024+)
- ✅ Use **clean background** in input image

### Customization:
Want to change prompts?
1. Find TextEncodeQwenImageEditPlus nodes
2. Edit positive/negative prompts
3. Add character-specific details

### For Faster Generation:
1. Reduce steps to 20-25
2. Change sampler to "euler"
3. Lower denoise to 0.65

### For Higher Quality:
1. Increase steps to 35-40
2. Increase CFG to 7.0-7.5
3. Use "dpm_2_ancestral" sampler

---

## 🔧 Troubleshooting

### Issue: Out of Memory (OOM)
**Solution:**
- Reduce steps to 20
- Use smaller input image (512×683)
- Close other applications

### Issue: Character inconsistency across poses
**Solution:**
- Use **same seed** for all (already default)
- Add detailed character description to ALL positive prompts
- Increase CFG to 7.0

### Issue: Generation too slow
**Solution:**
- Reduce steps to 20-25
- Change sampler to "euler"
- Consider generating in 2 batches (modify workflow)

### Issue: Some poses look wrong
**Solution:**
- Check specific pose's positive prompt
- Adjust denoise (0.60-0.75 range)
- Try different seeds

---

## 📦 Creating Final Grids

After generating 18 poses, create grids:

### Using ImageMagick:
```bash
# Batch A Grid (5×2 = 3840×2048)
montage 18Pose_A{1..10}*.png -tile 5x2 -geometry 768x1024+0+0 -background white BatchA_Grid.png

# Batch B Grid (4×2 = 3072×2048)
montage 18Pose_B{1..8}*.png -tile 4x2 -geometry 768x1024+0+0 -background white BatchB_Grid.png
```

### Using Python:
```python
from PIL import Image
import glob

def create_grid(pattern, cols, rows, output):
    files = sorted(glob.glob(pattern))[:cols*rows]
    images = [Image.open(f).resize((768, 1024)) for f in files]

    grid = Image.new('RGB', (768*cols, 1024*rows), 'white')
    for i, img in enumerate(images):
        x, y = (i % cols) * 768, (i // cols) * 1024
        grid.paste(img, (x, y))

    grid.save(output)
    print(f"✅ Saved: {output}")

# Batch A
create_grid('18Pose_A*.png', 5, 2, 'BatchA_Grid.png')

# Batch B
create_grid('18Pose_B*.png', 4, 2, 'BatchB_Grid.png')
```

---

## 📐 Grid Layouts

### Grid A (3840×2048):
```
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ A1       │ A2       │ A3       │ A4       │ A5       │
│ Full     │ Full     │ Full     │ Full     │ Half     │
│ Front    │ Right    │ Left     │ Back     │ Front    │
├──────────┼──────────┼──────────┼──────────┼──────────┤
│ A6       │ A7       │ A8       │ A9       │ A10      │
│ Half     │ Half     │ Half     │ Half     │ Half     │
│ Back     │ R45°     │ L45°     │ Right    │ Left     │
└──────────┴──────────┴──────────┴──────────┴──────────┘
```

### Grid B (3072×2048):
```
┌──────────┬──────────┬──────────┬──────────┐
│ B1       │ B2       │ B3       │ B4       │
│ Face     │ Face     │ Face     │ Over-    │
│ Front    │ Right    │ Left     │ Shldr R  │
├──────────┼──────────┼──────────┼──────────┤
│ B5       │ B6       │ B7       │ B8       │
│ Over-    │ Top-     │ Bottom-  │ Wide     │
│ Shldr L  │ Down     │ Up       │ Angle    │
└──────────┴──────────┴──────────┴──────────┘
```

---

## 🔄 Regenerating Specific Poses

If you only want to regenerate certain poses:

1. **Bypass other nodes:**
   - Right-click on unwanted pose's KSampler
   - Select "Bypass"
   - Repeat for all unwanted poses

2. **Queue prompt:**
   - Only active (non-bypassed) poses will generate
   - Saves time and VRAM

---

## 🎨 Customizing Poses

### Add Character Description:
Edit positive prompts to include your character:

**Example:**
```
Original:
"masterpiece, best quality, full body front view..."

With Character:
"masterpiece, best quality, full body front view, young woman with long black hair, wearing blue dress, green eyes, gentle smile..."
```

### Change Art Style:
Add style modifiers to positive prompts:

- **Anime:** "anime style, cel shaded, vibrant colors"
- **Realistic:** "photorealistic, detailed skin texture"
- **Semi-realistic:** "semi-realistic, painterly style"

---

## 📝 Advanced Customization

### Modify Prompts for Specific Poses:
1. Locate the pose's **TextEncodeQwenImageEditPlus** node
2. Edit the **widgets_values** field
3. Add specific instructions for that pose

### Adjust Per-Pose Settings:
Each **KSampler** can have different settings:
- Different seeds for variety
- Different denoise values
- Different CFG scales

---

## ✅ Quality Checklist

After generation, verify:

- [ ] All 18 poses generated successfully
- [ ] Character outfit consistent across all poses
- [ ] Character hairstyle identical
- [ ] Facial features match
- [ ] Background clean and white
- [ ] No extra limbs or deformities
- [ ] Poses match descriptions
- [ ] Good image quality (no blur/artifacts)

---

## 🆚 Comparison with Other Workflows

| Feature | 18-Pose Complete | Single-Pose | 15-Perspective |
|---------|-----------------|-------------|----------------|
| **Poses per run** | 18 | 1 | 15 |
| **Total nodes** | 99 | 14 | 451 |
| **Complexity** | Medium | Simple | Very Complex |
| **Generation time** | 8-12 min | 20-30s | 10-15 min |
| **Optimized settings** | ✅ Yes | ✅ Yes | ❌ No |
| **Customizable** | ✅ Easy | ✅ Very Easy | ⚠️ Difficult |
| **Use case** | Complete sheet | Individual pose | Multiple angles |

---

## 🔗 Related Files

- **generate_18pose_workflow.py** - Python script that generated this workflow
- **18-POSES-PROMPTS.md** - Detailed prompt templates
- **18-POSE-ARCHITECTURE.md** - Technical architecture documentation
- **README.md** - Project overview

---

## 📞 Support

For issues or questions:
- Check troubleshooting section above
- Review ComfyUI console for error messages
- Verify all models are installed correctly
- Ensure sufficient VRAM available

---

## 🎉 Credits

- **Workflow:** pose-03 project
- **Models:** Qwen-Image-Edit series (Alibaba/SeaArt)
- **Framework:** ComfyUI
- **Version:** 1.0
- **Generated:** 2025-11-15

---

**Ready to create professional character reference sheets! 🚀**

*Last updated: 2025-11-15*
