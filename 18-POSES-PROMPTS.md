# 🎯 18 Poses Prompts Guide

Hướng dẫn tạo 18 poses bằng workflow **qwen-optimized-single-pose.json**

## 📋 Cách sử dụng:

1. **Load workflow**: `qwen-optimized-single-pose.json` vào ComfyUI
2. **Load character reference**: Node #38 (LoadImage)
3. **Copy prompt tương ứng** từ bảng dưới vào Node #80 (Positive Prompt)
4. **Queue & Generate** mỗi pose
5. **Repeat 18 lần** cho 18 poses

---

## 📦 BATCH A - 10 Body Shots

### A1. Full Front View
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, standing straight, front view, facing camera directly, arms at sides, neutral stance, T-pose variation, character turnaround reference
```

### A2. Full Right Side (90°)
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, right side view, 90 degree angle, profile shot, arms visible, complete side silhouette, character turnaround reference
```

### A3. Full Left Side (90°)
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, left side view, 90 degree angle, profile shot, arms visible, complete side silhouette, character turnaround reference
```

### A4. Full Back View
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, back view, rear angle, showing back details, hair from behind, complete backside, character turnaround reference
```

### A5. Half Front (Waist Up)
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, front view, upper body focus, detailed torso, chest and head visible, character reference
```

### A6. Half Back (Waist Up)
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, back view, upper body from behind, shoulder and back details, character reference
```

### A7. Half Right 45° Angle
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, 45 degree right angle, three-quarter view, slight rotation right, character reference
```

### A8. Half Left 45° Angle
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, 45 degree left angle, three-quarter view, slight rotation left, character reference
```

### A9. Half Right Side (90°)
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, right side view, 90 degree profile, upper body side angle, character reference
```

### A10. Half Left Side (90°)
```
masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, left side view, 90 degree profile, upper body side angle, character reference
```

---

## 👤 BATCH B - 8 Close-ups

### B1. Face Front
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face front view, head and shoulders, facial features detailed, direct eye contact, character reference
```

### B2. Face Right Profile
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face right profile, 90 degree side view, jawline visible, ear details, character reference
```

### B3. Face Left Profile
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face left profile, 90 degree side view, jawline visible, ear details, character reference
```

### B4. Over-Shoulder Right
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, over right shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head, character reference
```

### B5. Over-Shoulder Left
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, over left shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head, character reference
```

### B6. Top-Down Angle
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, top-down angle, bird's eye view, looking down at character, overhead perspective, crown of head visible, character reference
```

### B7. Bottom-Up Angle
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, bottom-up angle, worm's eye view, looking up at character, low angle shot, chin and face from below, character reference
```

### B8. Wide-Angle Portrait
```
masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, wide angle portrait, slight fish-eye effect, dynamic perspective, head and upper torso, dramatic angle, character reference
```

---

## 🎨 Customization Tips

### Thêm Character Description
Thêm vào cuối mỗi prompt:

**Ví dụ:**
```
, young woman with long flowing black hair, wearing elegant blue dress with golden trim, emerald green eyes, gentle smile, fantasy character, anime style
```

### Adjust Style
Thêm style modifiers:
- **Anime**: `anime style, cel shaded, vibrant colors`
- **Realistic**: `photorealistic, realistic skin texture, detailed lighting`
- **Semi-realistic**: `semi-realistic, painterly style, stylized rendering`

### Background Variations
Nếu muốn background khác:
- **Gradient**: Replace `clean white background` → `gradient background, soft colors`
- **Solid color**: Replace `clean white background` → `solid blue background`
- **Transparent**: Add to negative: `background, any background`

---

## ⚙️ Workflow Parameters (Node #72)

**Current Optimized Settings:**
```
Seed: randomize (or fixed for consistency)
Steps: 30
CFG: 6.5
Sampler: euler_ancestral
Scheduler: karras
Denoise: 0.70
```

**For even MORE consistency across 18 poses:**
1. Use **FIXED SEED** (e.g., 123456)
2. Increase **character_consistency_lora** to 0.95 (Node #82)
3. Keep **same input image** for all 18 runs

**For FASTER generation:**
1. Reduce **steps** to 20-25
2. Change **sampler** to `euler`
3. Reduce **denoise** to 0.65

---

## 📊 Creating Grid Layouts

After generating all 18 images, use external tools to create grids:

### Option 1: Photoshop / GIMP
- Canvas Batch A: 3840×2048 (5 columns × 2 rows)
- Canvas Batch B: 3072×2048 (4 columns × 2 rows)
- Each cell: 768×1024

### Option 2: ImageMagick (Command Line)
```bash
# Batch A - 10 images in 5×2 grid
montage A*.png -tile 5x2 -geometry 768x1024+0+0 -background white BatchA_Grid.png

# Batch B - 8 images in 4×2 grid
montage B*.png -tile 4x2 -geometry 768x1024+0+0 -background white BatchB_Grid.png
```

### Option 3: Python (PIL)
```python
from PIL import Image

# Batch A Grid
images = [Image.open(f'A{i}.png') for i in range(1, 11)]
grid = Image.new('RGB', (3840, 2048), 'white')
for i, img in enumerate(images):
    x = (i % 5) * 768
    y = (i // 5) * 1024
    grid.paste(img.resize((768, 1024)), (x, y))
grid.save('BatchA_Grid.png')
```

---

## ✅ Quality Checklist

Before creating final grids, check:
- [ ] All 18 poses generated successfully
- [ ] Character outfit consistent across all poses
- [ ] Character hairstyle identical in all images
- [ ] Facial features match in all close-ups
- [ ] Background clean and consistent
- [ ] No extra limbs or fingers
- [ ] Poses match descriptions accurately

---

## 🔧 Troubleshooting

**Problem: Character changes between poses**
- Use **fixed seed** in KSampler
- Increase **LoRA strength** to 0.95
- Add more character details to positive prompt

**Problem: Background not clean**
- Add to negative: `complex background, detailed background, scenery, outdoor, indoor`
- Increase **CFG** to 7.0

**Problem: Poses not accurate**
- Be more specific in pose descriptions
- Increase **steps** to 35-40
- Try different **seed** values

**Problem: Blurry faces in close-ups**
- Reduce **denoise** to 0.65 for Batch B
- Increase **CFG** to 7.0
- Add to positive: `sharp focus, detailed face, high resolution facial features`

---

## 📝 Batch Processing Workflow

**Recommended order:**
1. Generate all Batch A (A1-A10) first
2. Verify consistency before Batch B
3. Generate all Batch B (B1-B8)
4. Compile into grids using external tools

**Time estimate (RTX 3060 12GB):**
- Single pose: ~20 seconds
- Total 18 poses: ~6 minutes
- Grid creation: 1-2 minutes
- **Total: ~8 minutes**

---

## 🎯 Pro Tips

1. **Save prompts**: Copy all prompts to a text file for easy access
2. **Batch rename**: Rename outputs as A1, A2, ... B8 for easy grid assembly
3. **Test first**: Generate 2-3 poses first to verify settings before full run
4. **Fixed seed**: Use same seed for ultimate consistency
5. **Character description**: Add detailed character description to ALL prompts
6. **Monitor outputs**: Check each pose before continuing

---

**Files:**
- Workflow: `qwen-optimized-single-pose.json`
- This guide: `18-POSES-PROMPTS.md`
- Original workflow: `Qwen Image Edit 2509.json`

**Next steps:**
1. Import workflow to ComfyUI
2. Load character reference image
3. Run 18 times with different prompts
4. Create grids using external tools

---

*Version 1.0 - Optimized for Qwen-Image-Edit-2509*
*Last updated: 2025-11-15*
