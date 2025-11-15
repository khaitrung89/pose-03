# 18-Pose Workflow Architecture

## Design Pattern (Based on 15-perspective analysis)

### Input Layer:
- 1 × LoadImage (character reference)
- 1 × SeaArtUnetLoader (model)
- 1 × CLIPLoader
- 1 × VAELoader

### Pose Generation (×18):
Each pose has:
- 1 × TextEncodeQwenImageEditPlus (positive prompt)
- 1 × TextEncodeQwenImageEditPlus (negative prompt)
- 1 × VAEEncode (shared input)
- 1 × KSampler (with specific pose prompt)
- 1 × VAEDecode
- 1 × SaveImage

Total per pose: 6 nodes × 18 = 108 nodes
Plus shared: ~15 nodes
Total: ~120-130 nodes (vs 451 in original)

### 18 Poses:

**Batch A - Body Shots (10):**
1. Full Front
2. Full Right 90°
3. Full Left 90°
4. Full Back
5. Half Front
6. Half Back
7. Half Right 45°
8. Half Left 45°
9. Half Right 90°
10. Half Left 90°

**Batch B - Close-ups (8):**
11. Face Front
12. Face Right
13. Face Left
14. Over-Shoulder Right
15. Over-Shoulder Left
16. Top-Down
17. Bottom-Up
18. Wide-Angle

### Optimized Settings:
- Steps: 30 (vs 8 in original)
- CFG: 6.5 (vs 1 in original)
- Denoise: 0.70 (vs 1.0 in original)
- Sampler: euler_ancestral (vs lcm in original)
- Scheduler: karras (vs normal in original)
