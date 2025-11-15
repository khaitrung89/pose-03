# ⚙️ Configuration Guide - 18-Pose Character Sheet

Chi tiết cấu hình cho từng thành phần trong workflow.

---

## 📦 Model Files Location

### Required Files:
```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── Qwen-Image-Edit-Rapid-AIO.safetensors  (hoặc .gguf)
│   ├── clip/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── vae/
│   │   └── qwen_image_vae.safetensors
│   └── loras/
│       ├── qwen_pose_control_lora.safetensors
│       ├── qwen_character_consistency_lora.safetensors
│       └── qwen_multi_angle_lora.safetensors
```

### Download Links (Example):
```
# Note: Điền links thực tế của models bạn đang dùng

Qwen-Image-Edit-Rapid-AIO:
  - SeaArt Model Hub
  - Hugging Face: alibaba/qwen-image-edit

CLIP & VAE:
  - Thường đi kèm với Qwen model package

LoRAs:
  - Civitai (search "Qwen pose control")
  - Custom trained (nếu bạn train riêng)
```

---

## 🎨 Node Configuration Details

### Node 10: LoadImage
```json
{
  "node_id": 10,
  "type": "LoadImage",
  "settings": {
    "image_path": "character_reference.png",
    "upload_mode": "image"
  },
  "recommendations": {
    "resolution": "768×1024 hoặc cao hơn",
    "format": "PNG (không nén)",
    "background": "Trắng hoặc đơn sắc",
    "quality": "High-res, sharp details"
  }
}
```

### Node 20: SeaArtUnetLoader
```json
{
  "node_id": 20,
  "type": "SeaArtUnetLoader",
  "settings": {
    "model_name": "Qwen-Image-Edit-Rapid-AIO",
    "mode": "default"
  },
  "alternatives": [
    "Qwen-Image-Edit-2509-GGUF-Q8_0",
    "Qwen-Image-Edit-2509-FP16"
  ],
  "notes": "Rapid-AIO nhanh hơn, 2509-FP16 chất lượng cao hơn"
}
```

### Node 21: CLIPLoader
```json
{
  "node_id": 21,
  "type": "CLIPLoader",
  "settings": {
    "clip_name": "qwen_2.5_vl_7b_fp8_scaled.safetensors",
    "type": "qwen_image",
    "mode": "default"
  },
  "notes": "7B parameters, FP8 precision cho balance speed/quality"
}
```

### Node 22: VAELoader
```json
{
  "node_id": 22,
  "type": "VAELoader",
  "settings": {
    "vae_name": "qwen_image_vae.safetensors"
  },
  "notes": "Official Qwen VAE, tối ưu cho Qwen models"
}
```

---

## 🎯 LoRA Configuration

### Node 30: Pose Control LoRA
```json
{
  "node_id": 30,
  "type": "LoraLoader",
  "settings": {
    "lora_name": "qwen_pose_control_lora.safetensors",
    "strength_model": 0.85,
    "strength_clip": 0.85
  },
  "tuning_guide": {
    "too_stiff": "Giảm xuống 0.70-0.75",
    "not_accurate": "Tăng lên 0.90-0.95",
    "default_safe": 0.85
  }
}
```

### Node 31: Character Consistency LoRA
```json
{
  "node_id": 31,
  "type": "LoraLoader",
  "settings": {
    "lora_name": "qwen_character_consistency_lora.safetensors",
    "strength_model": 0.95,
    "strength_clip": 0.95
  },
  "tuning_guide": {
    "character_changes": "Tăng lên 1.0",
    "too_rigid": "Giảm xuống 0.85-0.90",
    "default_safe": 0.95
  },
  "priority": "HIGH - Quan trọng nhất cho consistency"
}
```

### Node 32: Multi-Angle LoRA
```json
{
  "node_id": 32,
  "type": "LoraLoader",
  "settings": {
    "lora_name": "qwen_multi_angle_lora.safetensors",
    "strength_model": 0.80,
    "strength_clip": 0.80
  },
  "tuning_guide": {
    "angles_unclear": "Tăng lên 0.85-0.90",
    "too_dramatic": "Giảm xuống 0.70-0.75",
    "default_safe": 0.80
  }
}
```

---

## 🎲 Sampling Configuration

### Node 110: KSampler (Batch A - Body Shots)
```json
{
  "node_id": 110,
  "type": "KSampler",
  "settings": {
    "seed": "randomize",
    "steps": 30,
    "cfg": 6.5,
    "sampler_name": "euler_ancestral",
    "scheduler": "karras",
    "denoise": 0.70
  },
  "performance_tuning": {
    "fast_preview": {
      "steps": 15,
      "cfg": 5.0,
      "sampler": "euler"
    },
    "balanced": {
      "steps": 30,
      "cfg": 6.5,
      "sampler": "euler_ancestral"
    },
    "high_quality": {
      "steps": 40,
      "cfg": 7.5,
      "sampler": "dpm_2_ancestral"
    }
  },
  "denoise_guide": {
    "0.60-0.65": "Light edit, giữ nguyên nhiều chi tiết gốc",
    "0.70-0.75": "Balanced, edit vừa phải (RECOMMENDED)",
    "0.80-0.90": "Heavy edit, thay đổi nhiều",
    "1.00": "Full generation, tạo mới hoàn toàn"
  }
}
```

### Node 210: KSampler (Batch B - Close-ups)
```json
{
  "node_id": 210,
  "type": "KSampler",
  "settings": {
    "seed": "randomize",
    "steps": 30,
    "cfg": 6.5,
    "sampler_name": "euler_ancestral",
    "scheduler": "karras",
    "denoise": 0.65
  },
  "notes": "Denoise thấp hơn Batch A (0.65 vs 0.70) để preserve facial details",
  "facial_detail_optimization": {
    "denoise": 0.65,
    "cfg": 6.5,
    "steps": 30,
    "reason": "Close-ups cần giữ chi tiết khuôn mặt gốc"
  }
}
```

### Available Samplers:
```yaml
Fast (speed priority):
  - euler: Fastest, good quality
  - heun: Slightly better than euler

Balanced:
  - euler_ancestral: Good balance (DEFAULT)
  - dpm_2: Smooth results

Quality (quality priority):
  - dpm_2_ancestral: High quality, slower
  - dpm_adaptive: Adaptive steps
  - ddim: Classic, reliable
```

### Available Schedulers:
```yaml
- normal: Linear schedule
- karras: Improved noise schedule (DEFAULT)
- exponential: Exponential decay
- sgm_uniform: Uniform sampling
- simple: Simple schedule
```

---

## 🔧 Optimization Nodes

### Node 300: ModelSamplingAuraFlow
```json
{
  "node_id": 300,
  "type": "ModelSamplingAuraFlow",
  "settings": {
    "shift": 3.5
  },
  "tuning_guide": {
    "shift_range": "1.0 - 5.0",
    "low_shift_1_2": "More detail, slower convergence",
    "mid_shift_3_4": "Balanced (RECOMMENDED)",
    "high_shift_5": "Faster convergence, may lose details"
  }
}
```

### Node 301: CFGNorm
```json
{
  "node_id": 301,
  "type": "CFGNorm",
  "settings": {
    "strength": 1.0
  },
  "tuning_guide": {
    "strength_range": "0.5 - 1.5",
    "0_5_0_8": "Subtle normalization",
    "1_0": "Standard (RECOMMENDED)",
    "1_2_1_5": "Strong normalization, use if CFG artifacts appear"
  }
}
```

---

## 📐 Grid Assembly Configuration

### Node 113: ImageGridComposite (Batch A)
```json
{
  "node_id": 113,
  "type": "ImageGridComposite",
  "settings": {
    "columns": 5,
    "rows": 2,
    "width": 3840,
    "height": 2048
  },
  "calculation": {
    "cell_width": "3840 / 5 = 768",
    "cell_height": "2048 / 2 = 1024",
    "total_cells": "5 × 2 = 10 poses"
  },
  "alternative_layouts": {
    "square_layout": {
      "columns": 4,
      "rows": 3,
      "width": 3072,
      "height": 3072,
      "note": "Cần thêm 2 poses (total 12)"
    },
    "vertical_layout": {
      "columns": 2,
      "rows": 5,
      "width": 1536,
      "height": 5120,
      "note": "Long vertical sheet"
    }
  }
}
```

### Node 213: ImageGridComposite (Batch B)
```json
{
  "node_id": 213,
  "type": "ImageGridComposite",
  "settings": {
    "columns": 4,
    "rows": 2,
    "width": 3072,
    "height": 2048
  },
  "calculation": {
    "cell_width": "3072 / 4 = 768",
    "cell_height": "2048 / 2 = 1024",
    "total_cells": "4 × 2 = 8 poses"
  }
}
```

---

## 📝 Prompt Configuration

### Node 50: Positive Conditioning
```json
{
  "node_id": 50,
  "type": "TextEncodeQwenImageEditPlus",
  "base_prompt": "masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, multiple poses, turnaround reference, clean white background, studio lighting, character reference sheet",

  "customization": {
    "character_description": "ADD HERE: young woman, long black hair, blue dress, green eyes, etc.",
    "art_style": "ADD IF NEEDED: anime style, realistic, semi-realistic, etc.",
    "additional_details": "ADD IF NEEDED: accessories, specific features, etc."
  },

  "example_full_prompt": "masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, multiple poses, turnaround reference, clean white background, studio lighting, character reference sheet, young woman with long flowing black hair, wearing elegant blue dress with golden trim, emerald green eyes, gentle smile, fantasy character, anime style"
}
```

### Node 51: Negative Conditioning
```json
{
  "node_id": 51,
  "type": "TextEncodeQwenImageEditPlus",
  "base_prompt": "blurry, low quality, worst quality, jpeg artifacts, ugly, deformed, distorted, duplicate, watermark, text, signature, oversaturated, overexposed, static, unclear details, messy background, three legs, extra fingers, poorly drawn hands, poorly drawn face, malformed limbs, fused fingers, different outfit, different hairstyle, inconsistent character",

  "additional_negatives": {
    "for_anime": "realistic, photorealistic, 3d render",
    "for_realistic": "cartoon, anime, illustrated, drawing",
    "for_clean_bg": "complex background, detailed background, outdoor scene, indoor scene, scenery, landscape",
    "for_face_quality": "asymmetric eyes, cropped face, partial face, face out of frame"
  },

  "example_full_negative": "blurry, low quality, worst quality, jpeg artifacts, ugly, deformed, distorted, duplicate, watermark, text, signature, oversaturated, overexposed, static, unclear details, messy background, three legs, extra fingers, poorly drawn hands, poorly drawn face, malformed limbs, fused fingers, different outfit, different hairstyle, inconsistent character, complex background, detailed background, asymmetric eyes, cropped face"
}
```

---

## 💾 Output Configuration

### Node 114: SaveImage (Batch A)
```json
{
  "node_id": 114,
  "type": "SaveImage",
  "settings": {
    "filename_prefix": "BatchA_BodyShots_Grid"
  },
  "customization": {
    "add_date": "BatchA_BodyShots_Grid_%date%",
    "add_character_name": "BatchA_BodyShots_CharName_Grid",
    "add_version": "BatchA_BodyShots_Grid_v1"
  },
  "output_location": "ComfyUI/output/BatchA_BodyShots_Grid_XXXXXX.png"
}
```

### Node 214: SaveImage (Batch B)
```json
{
  "node_id": 214,
  "type": "SaveImage",
  "settings": {
    "filename_prefix": "BatchB_CloseUps_Grid"
  },
  "customization": {
    "add_date": "BatchB_CloseUps_Grid_%date%",
    "add_character_name": "BatchB_CloseUps_CharName_Grid",
    "add_version": "BatchB_CloseUps_Grid_v1"
  },
  "output_location": "ComfyUI/output/BatchB_CloseUps_Grid_XXXXXX.png"
}
```

---

## 🎚️ Quick Tuning Presets

### Preset 1: Speed (Fast Preview)
```yaml
Batch A KSampler (Node 110):
  steps: 15
  cfg: 5.0
  sampler: euler
  denoise: 0.65

Batch B KSampler (Node 210):
  steps: 15
  cfg: 5.0
  sampler: euler
  denoise: 0.60

LoRAs:
  pose_control: 0.75
  character_consistency: 0.85
  multi_angle: 0.70

Time: ~2-3 minutes
Quality: Preview level
```

### Preset 2: Balanced (Recommended)
```yaml
Batch A KSampler (Node 110):
  steps: 30
  cfg: 6.5
  sampler: euler_ancestral
  denoise: 0.70

Batch B KSampler (Node 210):
  steps: 30
  cfg: 6.5
  sampler: euler_ancestral
  denoise: 0.65

LoRAs:
  pose_control: 0.85
  character_consistency: 0.95
  multi_angle: 0.80

Time: ~5-8 minutes
Quality: High production level
```

### Preset 3: Maximum Quality
```yaml
Batch A KSampler (Node 110):
  steps: 40
  cfg: 7.5
  sampler: dpm_2_ancestral
  denoise: 0.75

Batch B KSampler (Node 210):
  steps: 40
  cfg: 7.5
  sampler: dpm_2_ancestral
  denoise: 0.70

LoRAs:
  pose_control: 0.90
  character_consistency: 1.00
  multi_angle: 0.85

ModelSamplingAuraFlow:
  shift: 4.0

Time: ~10-15 minutes
Quality: Maximum detail
```

---

## 🔍 Troubleshooting Configuration

### Issue: Character inconsistency
```yaml
Solution Config:
  character_consistency_lora: 1.00 (tăng từ 0.95)
  positive_prompt: thêm "same face, identical features"
  cfg: 7.0 (tăng từ 6.5)
  denoise: 0.65 (giảm từ 0.70)
```

### Issue: Pose inaccuracy
```yaml
Solution Config:
  pose_control_lora: 0.95 (tăng từ 0.85)
  multi_angle_lora: 0.90 (tăng từ 0.80)
  steps: 35 (tăng từ 30)
  cfg: 7.0 (tăng từ 6.5)
```

### Issue: Background not clean
```yaml
Solution Config:
  positive_prompt: thêm "pure white background, studio shot, isolated"
  negative_prompt: thêm "complex background, detailed background, outdoor, indoor, scenery"
  denoise: 0.75 (tăng để tạo background mới)
```

### Issue: Blurry details
```yaml
Solution Config:
  steps: 40 (tăng từ 30)
  cfg: 7.0 (tăng từ 6.5)
  denoise: 0.60 (giảm để giữ chi tiết)
  sampler: dpm_2_ancestral (thay vì euler_ancestral)
  negative_prompt: thêm "blurry, soft focus, out of focus"
```

### Issue: VRAM out of memory
```yaml
Solution Config:
  steps: 20 (giảm từ 30)
  sampler: euler (thay vì euler_ancestral)
  hoặc: disable một batch, chạy riêng Batch A rồi Batch B
  hoặc: giảm input resolution xuống 512×683
```

---

## 📊 Performance Optimization

### For RTX 3060 12GB:
```yaml
steps: 25
sampler: euler
cfg: 6.0
denoise: 0.70
lora_strengths: giảm 0.05 so với default
```

### For RTX 4090 24GB:
```yaml
steps: 40
sampler: dpm_2_ancestral
cfg: 7.5
denoise: 0.75
lora_strengths: có thể tăng 0.05
enable_xformers: true
```

### For RTX 4070 Ti 12GB:
```yaml
steps: 30
sampler: euler_ancestral
cfg: 6.5
denoise: 0.70
lora_strengths: default
```

---

## 🔐 Advanced Settings

### Batch Size Multiplier (Custom Nodes)
```json
{
  "node_111": {
    "type": "LatentBatchSeedBehavior",
    "batch_count": 10,
    "seed_behavior": "randomize",
    "note": "Generates 10 variations for Batch A"
  },
  "node_211": {
    "type": "LatentBatchSeedBehavior",
    "batch_count": 8,
    "seed_behavior": "randomize",
    "note": "Generates 8 variations for Batch B"
  }
}
```

### Fixed Seed for Reproducibility
```yaml
To make reproducible:
  1. Node 110: Set seed to fixed number (e.g., 123456)
  2. Node 210: Set seed to different fixed number (e.g., 789012)
  3. Node 111 & 211: Set seed_behavior to "fixed" or "increment"

Result: Same character, same poses every run
Use case: Iterating on prompts while keeping poses consistent
```

---

## 📝 Configuration Checklist

Before running workflow:
- [ ] All model files downloaded and placed correctly
- [ ] LoRA files compatible with Qwen models
- [ ] Input image loaded (768×1024 minimum)
- [ ] Prompts customized with character description
- [ ] LoRA strengths adjusted if needed
- [ ] Sampling parameters set (start with Balanced preset)
- [ ] Output filename prefixes set
- [ ] VRAM sufficient for current settings
- [ ] ComfyUI updated to latest version

---

*This configuration guide covers all tunable parameters in the 18-pose workflow.*
*For workflow usage, see README.md and 18-POSES-GUIDE.md*

**Last updated: 2025-11-15**
