# 🎯 18-Pose Character Sheet - Complete Guide

## 📋 Overview

Hệ thống tự động tạo character sheet với 18 poses được chia làm 2 batches:
- **Batch A**: 10 body shots (full/half body) → Grid 3840×2048
- **Batch B**: 8 close-ups (face/angle views) → Grid 3072×2048

---

## 🖼️ BATCH A - 10 Body Shots

### Grid Layout: 5 columns × 2 rows = 3840×2048
Mỗi pose: 768×1024 pixels

| Position | Pose Name | Prompt Addition | Description |
|----------|-----------|-----------------|-------------|
| **A1** | Full Front | `full body, standing straight, front view, facing camera directly, arms at sides, neutral stance, T-pose variation` | Toàn thân nhìn từ phía trước |
| **A2** | Full Right | `full body, right side view, 90 degree angle, profile shot, arms visible, complete side silhouette` | Toàn thân nhìn từ bên phải (90°) |
| **A3** | Full Left | `full body, left side view, 90 degree angle, profile shot, arms visible, complete side silhouette` | Toàn thân nhìn từ bên trái (90°) |
| **A4** | Full Back | `full body, back view, rear angle, showing back details, hair from behind, complete backside` | Toàn thân nhìn từ phía sau |
| **A5** | Half Front | `half body shot, waist up, front view, upper body focus, detailed torso, chest and head visible` | Nửa thân trên (eo lên) nhìn từ trước |
| **A6** | Half Back | `half body shot, waist up, back view, upper body from behind, shoulder and back details` | Nửa thân trên nhìn từ sau |
| **A7** | Half R45° | `half body shot, waist up, 45 degree right angle, three-quarter view, slight rotation right` | Nửa thân góc 45° bên phải |
| **A8** | Half L45° | `half body shot, waist up, 45 degree left angle, three-quarter view, slight rotation left` | Nửa thân góc 45° bên trái |
| **A9** | Half Right | `half body shot, waist up, right side view, 90 degree profile, upper body side angle` | Nửa thân nhìn từ bên phải (90°) |
| **A10** | Half Left | `half body shot, waist up, left side view, 90 degree profile, upper body side angle` | Nửa thân nhìn từ bên trái (90°) |

---

## 👤 BATCH B - 8 Close-ups

### Grid Layout: 4 columns × 2 rows = 3072×2048
Mỗi pose: 768×1024 pixels

| Position | Pose Name | Prompt Addition | Description |
|----------|-----------|-----------------|-------------|
| **B1** | Face Front | `close-up portrait, face front view, head and shoulders, facial features detailed, direct eye contact` | Cận mặt nhìn thẳng |
| **B2** | Face Right | `close-up portrait, face right profile, 90 degree side view, jawline visible, ear details` | Cận mặt profile bên phải |
| **B3** | Face Left | `close-up portrait, face left profile, 90 degree side view, jawline visible, ear details` | Cận mặt profile bên trái |
| **B4** | Over-Shoulder R | `over right shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head` | Nhìn qua vai phải |
| **B5** | Over-Shoulder L | `over left shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head` | Nhìn qua vai trái |
| **B6** | Top-Down | `top-down angle, bird's eye view, looking down at character, overhead perspective, crown of head visible` | Góc nhìn từ trên xuống |
| **B7** | Bottom-Up | `bottom-up angle, worm's eye view, looking up at character, low angle shot, chin and face from below` | Góc nhìn từ dưới lên |
| **B8** | Wide-Angle | `wide angle portrait, slight fish-eye effect, dynamic perspective, head and upper torso, dramatic angle` | Góc rộng dramatic |

---

## 🔧 Model Configuration

### Base Models:
```
Main Model: Qwen-Image-Edit-Rapid-AIO (hoặc Qwen-Image-Edit-2509)
CLIP: qwen_2.5_vl_7b_fp8_scaled.safetensors
VAE: qwen_image_vae.safetensors
```

### LoRA Stack (Thứ tự quan trọng):
```
1. qwen_pose_control_lora.safetensors
   - Strength: 0.85 (model & clip)
   - Purpose: Kiểm soát pose chính xác

2. qwen_character_consistency_lora.safetensors
   - Strength: 0.95 (model & clip)
   - Purpose: Giữ nhất quán character design

3. qwen_multi_angle_lora.safetensors
   - Strength: 0.80 (model & clip)
   - Purpose: Tối ưu cho multi-angle views
```

---

## ⚙️ Sampling Parameters

### Batch A (Body Shots):
```
Steps: 30
CFG Scale: 6.5
Sampler: euler_ancestral
Scheduler: karras
Denoise: 0.70
Seed: randomize
```

### Batch B (Close-ups):
```
Steps: 30
CFG Scale: 6.5
Sampler: euler_ancestral
Scheduler: karras
Denoise: 0.65 (thấp hơn để giữ chi tiết khuôn mặt)
Seed: randomize
```

### Optimization Nodes:
```
ModelSamplingAuraFlow: shift = 3.5
CFGNorm: strength = 1.0
```

---

## 📝 Prompt Templates

### Global Positive Prompt:
```
masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet,
consistent character design, same outfit, same hairstyle, same facial features,
multiple poses, turnaround reference, clean white background, studio lighting,
character reference sheet
```

### Global Negative Prompt:
```
blurry, low quality, worst quality, jpeg artifacts, ugly, deformed, distorted,
duplicate, watermark, text, signature, oversaturated, overexposed, static,
unclear details, messy background, three legs, extra fingers, poorly drawn hands,
poorly drawn face, malformed limbs, fused fingers, different outfit, different hairstyle,
inconsistent character
```

### Per-Pose Prompt Structure:
```
[Global Positive] + [Specific Pose Prompt from table above] + [Character Description]
```

**Ví dụ cho pose A1 (Full Front):**
```
masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet,
consistent character design, same outfit, same hairstyle, same facial features,
full body, standing straight, front view, facing camera directly, arms at sides,
neutral stance, T-pose variation,
[YOUR CHARACTER DESCRIPTION: e.g., "young woman with long black hair,
wearing blue dress, green eyes, friendly smile"]
```

---

## 🎨 Workflow Node Structure

```
Input (768×1024)
    ↓
┌─────────────────────┐
│ Base Models Load    │
│ - UNet (Rapid-AIO)  │
│ - CLIP (7B FP8)     │
│ - VAE (Qwen)        │
└─────────────────────┘
    ↓
┌─────────────────────┐
│ LoRA Stack          │
│ 1. Pose Control     │
│ 2. Char Consistency │
│ 3. Multi-Angle      │
└─────────────────────┘
    ↓
┌─────────────────────┐
│ Optimization        │
│ - AuraFlow Sampling │
│ - CFG Normalization │
└─────────────────────┘
    ↓
    ├─────────────────────────┬─────────────────────────┐
    │                         │                         │
┌───▼────────┐         ┌──────▼─────┐         ┌────────▼──────┐
│ Batch A    │         │ Batch B    │         │ Conditioning  │
│ Pipeline   │         │ Pipeline   │         │ (Global)      │
│            │         │            │         │               │
│ KSampler   │         │ KSampler   │         │ Positive +    │
│ ↓          │         │ ↓          │         │ Negative      │
│ Batch×10   │         │ Batch×8    │         └───────────────┘
│ ↓          │         │ ↓          │
│ VAE Decode │         │ VAE Decode │
│ ↓          │         │ ↓          │
│ Grid 5×2   │         │ Grid 4×2   │
│ 3840×2048  │         │ 3072×2048  │
└────────────┘         └────────────┘
```

---

## 📊 Output Specifications

### Grid A (Batch A):
- **Dimensions:** 3840 × 2048 pixels
- **Layout:** 5 columns × 2 rows
- **Each cell:** 768 × 1024 pixels
- **Content:** Full & Half body shots
- **Filename:** `BatchA_BodyShots_Grid_XXXXXX.png`

### Grid B (Batch B):
- **Dimensions:** 3072 × 2048 pixels
- **Layout:** 4 columns × 2 rows
- **Each cell:** 768 × 1024 pixels
- **Content:** Face close-ups & angle views
- **Filename:** `BatchB_CloseUps_Grid_XXXXXX.png`

---

## 🚀 Usage Instructions

### Step 1: Chuẩn bị Input
1. Chuẩn bị ảnh reference character (768×1024 recommended)
2. Đặt tên file: `character_reference.png`
3. Load vào node **LoadImage** (Node 10)

### Step 2: Customize Prompts (Optional)
1. Thêm character description vào **Positive Prompt** (Node 50)
2. Điều chỉnh **Negative Prompt** nếu cần (Node 51)

### Step 3: Adjust LoRA Strengths (Optional)
- **Pose Control** (Node 30): 0.85 (giảm nếu pose quá cứng)
- **Character Consistency** (Node 31): 0.95 (tăng nếu character thay đổi)
- **Multi-Angle** (Node 32): 0.80 (tăng nếu angle views không rõ)

### Step 4: Run Workflow
1. Queue workflow trong ComfyUI
2. Batch A sẽ generate trước (10 poses)
3. Batch B generate sau (8 poses)
4. Total time: ~5-8 phút (depends on hardware)

### Step 5: Collect Outputs
- Check output folder cho 2 grid images
- Verify character consistency across all 18 poses
- Re-run với adjusted params nếu cần

---

## 🎯 Quality Checklist

### Character Consistency:
- [ ] Same outfit across all 18 poses
- [ ] Same hairstyle and color
- [ ] Same facial features
- [ ] Same body proportions
- [ ] Same accessories/details

### Pose Accuracy:
- [ ] Angles match descriptions (90°, 45°, etc.)
- [ ] No twisted/deformed limbs
- [ ] Natural body posture
- [ ] Clear silhouette for each view

### Technical Quality:
- [ ] No blur or artifacts
- [ ] Clean white background
- [ ] Proper lighting (studio style)
- [ ] Sharp details on face/hands
- [ ] Correct resolution (768×1024 per pose)

---

## 🔄 Troubleshooting

### Problem: Character inconsistency
**Solution:** Tăng `character_consistency_lora` strength lên 1.0

### Problem: Poses không đúng angle
**Solution:**
1. Tăng `pose_control_lora` strength
2. Thêm chi tiết angle vào prompt
3. Kiểm tra `multi_angle_lora` đã load chưa

### Problem: Background không trắng/sạch
**Solution:** Thêm vào negative prompt: `"complex background, detailed background, outdoor, indoor, scenery"`

### Problem: Facial details bị blur
**Solution:**
1. Giảm denoise của Batch B xuống 0.60
2. Tăng CFG lên 7.0-7.5 cho Batch B
3. Tăng steps lên 35-40

### Problem: Generation quá lâu
**Solution:**
1. Giảm steps xuống 25
2. Dùng sampler "euler" thay vì "euler_ancestral"
3. Giảm resolution input xuống 512×683

---

## 📈 Advanced Tips

### Tip 1: Optimize Memory Usage
- Batch A và B có thể run riêng biệt nếu VRAM không đủ
- Disable một trong hai branch, run tuần tự

### Tip 2: Custom Pose Variations
- Fork từ KSampler nodes
- Thêm ControlNet cho pose control chính xác hơn
- Sử dụng OpenPose/DWPose preprocessor

### Tip 3: Style Variations
- Thêm style LoRAs vào stack (sau multi_angle_lora)
- Điều chỉnh global prompt cho anime/realistic/semi-realistic

### Tip 4: Batch Processing Multiple Characters
- Create loop với multiple input images
- Sử dụng ComfyUI's batch processing features
- Auto-rename outputs với character names

---

## 📦 File Structure
```
pose-03/
├── pose-03-18poses-workflow.json       # Main workflow
├── 18-POSES-GUIDE.md                   # This guide
├── Qwen Image Edit 2509.json           # Original workflow
├── outputs/
│   ├── BatchA_BodyShots_Grid_XXXXXX.png
│   └── BatchB_CloseUps_Grid_XXXXXX.png
└── inputs/
    └── character_reference.png
```

---

## 🏆 Best Practices

1. **Always use high-quality reference image** (768×1024 minimum)
2. **Keep character description detailed but concise**
3. **Don't modify LoRA order** (loading sequence affects results)
4. **Test with low steps first** (20 steps) to verify setup
5. **Save workflow snapshots** after successful generations
6. **Use fixed seed** for reproducible results when needed
7. **Monitor VRAM usage** - reduce batch size if OOM errors

---

## 📞 Support & Credits

- **Workflow Version:** 1.0.0
- **Created for:** pose-03 project
- **Models:** Qwen-Image-Edit series (SeaArt/Alibaba)
- **Framework:** ComfyUI

**Note:** LoRA files phải tương thích với Qwen models. Nếu không có LoRAs, có thể disable các LoRA nodes và chạy với base model (chất lượng sẽ thấp hơn).

---

*Last updated: 2025-11-15*
