# 📤 SeaArt Upload Guide

Hướng dẫn upload workflow lên SeaArt platform.

---

## 📁 FILE UPLOAD

**Workflow file:** `SeaArt-Character-Pose-Workflow.json`

---

## 📝 THÔNG TIN WORKFLOW CHO SEAART

### **Title / Tên workflow:**
```
Character Pose Generator - Optimized for Reference Sheets
```

### **Description / Mô tả:**
```
🎨 Professional character pose generator using Qwen-Image-Edit models

✨ FEATURES:
• Optimized parameters for high-quality character poses
• Perfect for character reference sheets and turnarounds
• Support for full body, half body, and close-up poses
• Character consistency with optional LoRA support
• Clean white background for professional results

🔧 OPTIMIZED SETTINGS:
• Denoise: 0.70 (editing mode, preserves character details)
• CFG: 6.5 (balanced prompt adherence)
• Steps: 30 (high quality output)
• English prompts (easy to customize)

📋 USE CASES:
• Character design reference sheets
• Game character turnarounds
• Animation character references
• Comic/manga character poses
• Illustration reference materials

💡 TIPS FOR BEST RESULTS:
• Use fixed seed for consistency across multiple poses
• Enable character consistency LoRA (strength 0.85-0.95)
• Add detailed character description to prompts
• Generate 18 different poses for complete reference sheet

⚙️ REQUIREMENTS:
• Qwen-Image-Edit-Rapid-AIO model (or Qwen-Image-Edit-2509)
• qwen_2.5_vl_7b_fp8_scaled.safetensors (CLIP)
• qwen_image_vae.safetensors (VAE)
• qwen_character_consistency_lora.safetensors (optional)

🎯 RECOMMENDED FOR:
Character artists, game developers, animators, illustrators, comic artists
```

### **Category / Danh mục:**
```
Character Design / Image Editing
```

### **Tags / Thẻ tag:**
```
character, pose, reference, turnaround, character-sheet, qwen, character-design, game-art, animation, illustration, multi-pose, body-reference, face-reference
```

### **Difficulty / Độ khó:**
```
Beginner to Intermediate
```

### **Estimated Time / Thời gian:**
```
~20-30 seconds per pose
```

---

## 🎨 THUMBNAIL/PREVIEW IMAGE

**Khuyến nghị tạo preview image:**

### Option 1: Grid Layout
```
Tạo 1 ảnh grid 3×3 hoặc 4×4 với:
- Different character poses
- Clean white background
- Professional layout
- Size: 1024×1024 hoặc 1200×1200
```

### Option 2: Before/After
```
Split screen showing:
- Left: Input character image
- Right: Generated pose outputs (2-3 examples)
- Size: 1200×800
```

### Option 3: Collage
```
Character poses in artistic layout:
- Multiple angles visible
- Clean presentation
- Professional quality
- Size: 1200×900
```

---

## 📋 MODELS INFORMATION

### **Required Models:**

**1. Main Model:**
```
Name: Qwen-Image-Edit-Rapid-AIO
Type: UNet Model
Size: ~8-12GB
Source: SeaArt Model Hub
Alternative: Qwen-Image-Edit-2509-GGUF-Q8_0
```

**2. CLIP Model:**
```
Name: qwen_2.5_vl_7b_fp8_scaled
Type: CLIP Vision-Language
Parameters: 7 billion
Precision: FP8
Size: ~4-6GB
```

**3. VAE Model:**
```
Name: qwen_image_vae
Type: VAE Encoder/Decoder
Size: ~300-500MB
```

**4. LoRA (Optional):**
```
Name: qwen_character_consistency_lora
Type: LoRA
Strength: 0.85 (model & clip)
Size: ~100-300MB
Purpose: Improve character consistency across poses
```

---

## 🎯 USAGE INSTRUCTIONS (For SeaArt Description)

### **Quick Start:**

**Step 1: Load Character**
```
• Click "Load Character Image" node
• Upload your character reference (768×1024 recommended)
• Any resolution works, will auto-scale
```

**Step 2: Customize Prompt**
```
• Open "Positive Prompt" node
• Add your pose description:
  - Full body front view / Half body side view / Face closeup
  - Character details: age, hair, clothing, features
  - Art style: anime / realistic / semi-realistic
```

**Example Prompts:**
```
FULL BODY FRONT:
"masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body front view, standing straight, arms at sides, neutral pose, young woman with long black hair, wearing blue dress, green eyes, anime style"

HALF BODY SIDE:
"masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, right side view, 90 degree profile, young man with short brown hair, wearing red jacket, confident expression, semi-realistic style"

FACE CLOSEUP:
"masterpiece, best quality, ultra detailed, 8k resolution, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face front view, head and shoulders, facial features detailed, teenage girl with blue hair, purple eyes, friendly smile, anime style"
```

**Step 3: Adjust Settings (Optional)**
```
• Seed: Use 'randomize' for variety OR fixed number for consistency
• Steps: 30 (balanced) | 20 (fast) | 40 (quality)
• CFG: 6.5 (default) | 5.0 (creative) | 8.0 (strict)
• Denoise: 0.70 (default) | 0.60 (preserve more) | 0.80 (change more)
```

**Step 4: Generate**
```
• Click "Queue Prompt"
• Wait ~20-30 seconds
• Download output from "Save Output" node
```

**Step 5: Multiple Poses (Optional)**
```
• Change prompt to different pose
• Use SAME seed for character consistency
• Generate 18 different poses for complete sheet
```

---

## 🎨 18-POSE CHARACTER SHEET GUIDE

### **Batch A - Body Shots (10 poses):**
1. Full Body Front View
2. Full Body Right Side (90°)
3. Full Body Left Side (90°)
4. Full Body Back View
5. Half Body Front (waist up)
6. Half Body Back (waist up)
7. Half Body Right 45°
8. Half Body Left 45°
9. Half Body Right Side (90°)
10. Half Body Left Side (90°)

### **Batch B - Close-ups (8 poses):**
1. Face Front
2. Face Right Profile
3. Face Left Profile
4. Over-Shoulder Right
5. Over-Shoulder Left
6. Top-Down Angle
7. Bottom-Up Angle
8. Wide-Angle Portrait

### **Grid Layout:**
```
Batch A Grid: 5 columns × 2 rows = 3840×2048
Batch B Grid: 4 columns × 2 rows = 3072×2048
```

---

## 💡 TIPS & TRICKS

### **For Character Consistency:**
```
✅ Use FIXED SEED across all 18 poses
✅ Enable character consistency LoRA (strength 0.85-0.95)
✅ Add detailed character description to ALL prompts
✅ Use SAME input reference image
✅ Keep CFG and denoise values consistent
```

### **For Quality:**
```
✅ High-resolution input (768×1024 minimum)
✅ Clean background in reference image
✅ Increase steps to 35-40 for maximum detail
✅ Use euler_ancestral sampler (default)
```

### **For Speed:**
```
✅ Reduce steps to 20-25
✅ Use euler sampler
✅ Lower denoise to 0.65
```

### **Common Issues:**

**Character changes between poses:**
→ Use fixed seed + LoRA + detailed character description

**Background not clean:**
→ Add to negative: "complex background, detailed background, scenery"

**Blurry details:**
→ Increase steps to 35-40, increase CFG to 7.0

**Generation too slow:**
→ Reduce steps to 20, use euler sampler

---

## 📊 PERFORMANCE

| Hardware | Time per Pose | 18 Poses Total |
|----------|---------------|----------------|
| RTX 3060 12GB | ~20s | ~6 min |
| RTX 4090 24GB | ~10s | ~3 min |
| RTX 4070 Ti 12GB | ~15s | ~4.5 min |

---

## 🔗 LINKS & RESOURCES

**GitHub Repository:**
```
https://github.com/khaitrung89/pose-03
```

**Full Documentation:**
```
https://github.com/khaitrung89/pose-03/blob/main/README.md
```

**18-Pose Prompts Guide:**
```
https://github.com/khaitrung89/pose-03/blob/main/18-POSES-PROMPTS.md
```

**Automation Script (Python):**
```
https://github.com/khaitrung89/pose-03/blob/main/generate_18_poses.py
```

---

## 📜 LICENSE & CREDITS

**Workflow License:**
```
Free to use for personal and commercial projects
```

**Models:**
```
• Qwen-Image-Edit series by Alibaba Cloud / SeaArt
• Follow individual model licenses
```

**Created by:**
```
pose-03 project
Version: 1.0
Date: 2025-11-15
```

---

## ✅ UPLOAD CHECKLIST

Before uploading to SeaArt:

- [ ] Workflow JSON file ready (`SeaArt-Character-Pose-Workflow.json`)
- [ ] Thumbnail/preview image created (1024×1024 or larger)
- [ ] Title filled in (clear and descriptive)
- [ ] Description copied (with features, usage, requirements)
- [ ] Tags added (13+ relevant tags)
- [ ] Category selected (Character Design / Image Editing)
- [ ] Models list provided
- [ ] Usage instructions clear
- [ ] Example prompts included
- [ ] Tested workflow works correctly

---

## 📤 UPLOAD STEPS ON SEAART

1. **Login to SeaArt**
   - Go to SeaArt.ai
   - Login to your account

2. **Navigate to Workflows**
   - Click "Create" or "Workflows"
   - Select "Upload Workflow"

3. **Upload JSON**
   - Upload `SeaArt-Character-Pose-Workflow.json`
   - Wait for processing

4. **Fill Information**
   - Title: Copy from above
   - Description: Copy from above
   - Tags: Add all tags
   - Category: Select appropriate

5. **Upload Preview**
   - Add thumbnail image
   - Add 2-3 example outputs

6. **Publish**
   - Review all information
   - Click "Publish"
   - Share link!

---

## 🎉 DONE!

Your workflow is ready to share on SeaArt!

**Share your workflow link here when uploaded!** 🚀

---

*Last updated: 2025-11-15*
*Version: 1.0*
