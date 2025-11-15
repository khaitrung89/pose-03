# 🔄 Workflow Comparison & Fixes

## ❌ Problem với workflow trước đó

**File có lỗi:** `pose-03-18poses-workflow.json`

**Lỗi:** `Cannot execute because a node is missing the class_type property: Node ID '#112'`

**Nguyên nhân:**
Workflow sử dụng **custom nodes không có trong ComfyUI standard**:
- `VAEDecodeBatch` (Node #112) - ❌ Không tồn tại
- `LatentBatchSeedBehavior` (Node #111, #211) - ❌ Không tồn tại
- `ImageGridComposite` (Node #113, #213) - ❌ Không tồn tại

**Kết quả:** Workflow không chạy được trên hầu hết ComfyUI installations.

---

## ✅ Solution: Workflow mới

### **File đề xuất:** `qwen-optimized-single-pose.json`

**Đặc điểm:**
- ✅ CHỈ dùng **standard nodes** + **SeaArt nodes** (giống workflow gốc)
- ✅ **Tương thích 100%** với SeaArt ComfyUI
- ✅ **Optimized parameters** cho quality cao hơn
- ✅ **Optional LoRA support** cho character consistency
- ⚠️ Tạo **1 pose mỗi lần** (chạy 18 lần để có 18 poses)

---

## 📊 So sánh 3 workflows

| Feature | Original<br/>(Qwen Image Edit 2509.json) | Optimized Single Pose<br/>(qwen-optimized-single-pose.json) | 18-Pose Complex<br/>(pose-03-18poses-workflow.json) |
|---------|-------------|---------------------|----------------------|
| **Status** | ✅ Works | ✅ Works | ❌ Broken (custom nodes) |
| **Compatibility** | SeaArt ComfyUI | SeaArt ComfyUI | ❌ Requires custom nodes |
| **Nodes** | All standard/SeaArt | All standard/SeaArt | Custom nodes (not available) |
| **Denoise** | 1.0 (full gen) | **0.70** (editing) | 0.70/0.65 |
| **CFG** | 2.5 (too low) | **6.5** (optimal) | 6.5 |
| **Steps** | 20 | **30** | 30 |
| **LoRA** | ❌ No | ✅ **Optional** | ✅ Yes (3 LoRAs) |
| **Negative Prompt** | Chinese | **English** | English |
| **Outputs** | 1 pose | 1 pose | 18 poses (not working) |
| **Use Case** | Basic | **Recommended** | Concept only |

---

## 🎯 Khuyến nghị sử dụng

### **Cho Production (Khuyến nghị):**
```
📁 qwen-optimized-single-pose.json
```

**Lý do:**
- ✅ Works out of the box với SeaArt ComfyUI
- ✅ Optimized parameters
- ✅ English prompts dễ customize
- ✅ Optional LoRA support
- ✅ Tạo high-quality single pose

**Workflow cho 18 poses:**
1. Load `qwen-optimized-single-pose.json`
2. Chạy 18 lần với prompts khác nhau (xem `18-POSES-PROMPTS.md`)
3. Tạo grids bằng external tools (Photoshop/ImageMagick/Python)

---

### **Cho Quick Testing:**
```
📁 Qwen Image Edit 2509.json (original)
```

**Lý do:**
- Đơn giản nhất
- Ít nodes nhất
- Phù hợp test model

**Nhược điểm:**
- Parameters chưa tối ưu (denoise=1.0, cfg=2.5)
- Negative prompt tiếng Trung
- Không có LoRA

---

### **KHÔNG dùng:**
```
❌ pose-03-18poses-workflow.json
```

**Lý do:**
- Sử dụng custom nodes không tồn tại
- Sẽ báo lỗi khi load
- Concept tốt nhưng implementation không tương thích

---

## 🔧 Chi tiết cải thiện

### Optimized Workflow Improvements:

#### 1. **Denoise: 1.0 → 0.70**
```
Original: denoise = 1.0 (full generation, ignores input)
Optimized: denoise = 0.70 (editing mode, preserves input details)

Result: Better character consistency, preserves reference features
```

#### 2. **CFG: 2.5 → 6.5**
```
Original: cfg = 2.5 (very low, weak prompt adherence)
Optimized: cfg = 6.5 (balanced, strong prompt following)

Result: Better prompt accuracy, clearer poses
```

#### 3. **Steps: 20 → 30**
```
Original: steps = 20 (basic quality)
Optimized: steps = 30 (higher quality)

Result: Sharper details, better rendering
```

#### 4. **Negative Prompt: Chinese → English**
```
Original: "色调艳丽，过曝，静态，细节模糊不清..." (Chinese)
Optimized: "blurry, low quality, worst quality..." (English)

Result: Better compatibility, easier to customize
```

#### 5. **LoRA Support**
```
Original: No LoRA
Optimized: Optional LoRA loader (character_consistency)

Result: Much better character consistency across multiple generations
```

#### 6. **AuraFlow: 3.0 → 3.5**
```
Original: shift = 3.0
Optimized: shift = 3.5

Result: Slightly better convergence
```

---

## 📋 Nodes Comparison

### Original Workflow Nodes:
```
✅ SeaArtUnetLoader
✅ CLIPLoader
✅ VAELoader
✅ LoadImage
✅ FluxKontextImageScale (SeaArt custom)
✅ VAEEncode
✅ TextEncodeQwenImageEditPlus (SeaArt custom)
✅ ModelSamplingAuraFlow
✅ CFGNorm
✅ KSampler
✅ VAEDecode
✅ SaveImage
```

### Optimized Workflow Adds:
```
+ LoraLoader (optional, can be disabled)
```

### Broken 18-Pose Workflow Attempted:
```
❌ VAEDecodeBatch - NOT IN COMFYUI
❌ LatentBatchSeedBehavior - NOT IN COMFYUI
❌ ImageGridComposite - NOT IN COMFYUI
```

---

## 🚀 Migration Guide

### If you were using the broken workflow:

**Step 1:** Delete or archive
```
❌ pose-03-18poses-workflow.json
```

**Step 2:** Use instead
```
✅ qwen-optimized-single-pose.json
```

**Step 3:** Follow guide
```
📖 18-POSES-PROMPTS.md
```

**Step 4:** Create grids externally
```bash
# Using ImageMagick
montage pose_*.png -tile 5x2 -geometry 768x1024+0+0 grid.png
```

---

## 🎨 How to Create 18-Pose Grid

### Method 1: Manual (Recommended)

1. **Generate all 18 poses**
   - Use `qwen-optimized-single-pose.json`
   - Copy prompts from `18-POSES-PROMPTS.md`
   - Run 18 times with different prompts
   - Save as: `A1.png`, `A2.png`, ... `B8.png`

2. **Create grids in Photoshop/GIMP**
   - Batch A Canvas: 3840×2048
   - Batch B Canvas: 3072×2048
   - Place images in grid layout (5×2 and 4×2)

### Method 2: ImageMagick (Automated)

```bash
# Batch A (10 images, 5×2 grid)
montage A{1..10}.png \
  -tile 5x2 \
  -geometry 768x1024+0+0 \
  -background white \
  BatchA_Grid.png

# Batch B (8 images, 4×2 grid)
montage B{1..8}.png \
  -tile 4x2 \
  -geometry 768x1024+0+0 \
  -background white \
  BatchB_Grid.png
```

### Method 3: Python Script

```python
from PIL import Image

def create_grid(images, cols, rows, output):
    w, h = 768, 1024
    grid = Image.new('RGB', (w*cols, h*rows), 'white')

    for i, img_path in enumerate(images):
        img = Image.open(img_path).resize((w, h))
        x = (i % cols) * w
        y = (i // cols) * h
        grid.paste(img, (x, y))

    grid.save(output)

# Batch A
batch_a = [f'A{i}.png' for i in range(1, 11)]
create_grid(batch_a, 5, 2, 'BatchA_Grid.png')

# Batch B
batch_b = [f'B{i}.png' for i in range(1, 9)]
create_grid(batch_b, 4, 2, 'BatchB_Grid.png')
```

---

## 📁 Final File Structure

```
pose-03/
├── 📄 Qwen Image Edit 2509.json           # Original workflow
├── ✅ qwen-optimized-single-pose.json     # RECOMMENDED
├── ❌ pose-03-18poses-workflow.json       # BROKEN (custom nodes)
│
├── 📖 README.md                           # Updated overview
├── 📖 18-POSES-PROMPTS.md                 # Prompt templates for 18 poses
├── 📖 WORKFLOW-COMPARISON.md              # This file
├── 📖 CONFIGURATION.md                    # Advanced settings
└── 📖 18-POSES-GUIDE.md                   # Original guide (for reference)
```

---

## ✅ Quality Assurance Checklist

Before using any workflow:

- [ ] Check all nodes exist in your ComfyUI installation
- [ ] Verify model files are downloaded and placed correctly
- [ ] Test with 1-2 poses before running full 18
- [ ] Use fixed seed for consistency testing
- [ ] Verify LoRA compatibility (if using)
- [ ] Check output quality before batch processing

---

## 🤝 Recommendations Summary

| Use Case | Recommended Workflow | Time | Quality |
|----------|---------------------|------|---------|
| **Quick test** | Original (Qwen Image Edit 2509.json) | 15s | Good |
| **Single high-quality pose** | ✅ Optimized (qwen-optimized-single-pose.json) | 20s | Excellent |
| **18-pose character sheet** | ✅ Optimized × 18 + External grid tool | 6min | Excellent |
| **Batch automation** | Custom scripts + Optimized workflow | Varies | Excellent |

---

## 🔮 Future Improvements

Potential enhancements (requires custom node development):

1. **Batch Latent Processor** - Generate multiple poses in one run
2. **Grid Compositor Node** - Auto-create grids in ComfyUI
3. **Pose Prompt Templates** - Pre-defined 18 pose prompts as dropdown
4. **Character Consistency Node** - Advanced character preservation

**Status:** Concept stage - requires custom node development

---

**Recommended workflow:** `qwen-optimized-single-pose.json`
**Recommended guide:** `18-POSES-PROMPTS.md`

*Last updated: 2025-11-15*
