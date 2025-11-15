#!/usr/bin/env python3
"""
Automated 18-Pose Character Sheet Generator
Tự động tạo 18 poses bằng ComfyUI API
"""

import json
import urllib.request
import urllib.parse
import time
import os
from pathlib import Path

# ============= CONFIGURATION =============
COMFYUI_URL = "http://127.0.0.1:8188"  # ComfyUI server URL
WORKFLOW_FILE = "qwen-optimized-single-pose.json"
OUTPUT_DIR = "outputs/18poses"
CHARACTER_IMAGE = "character_reference.png"  # Đặt ảnh character vào folder ComfyUI/input/

# Tạo output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============= 18 POSE PROMPTS =============
POSES = {
    # Batch A - Body Shots
    "A1_Full_Front": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, standing straight, front view, facing camera directly, arms at sides, neutral stance, T-pose variation, character turnaround reference",

    "A2_Full_Right": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, right side view, 90 degree angle, profile shot, arms visible, complete side silhouette, character turnaround reference",

    "A3_Full_Left": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, left side view, 90 degree angle, profile shot, arms visible, complete side silhouette, character turnaround reference",

    "A4_Full_Back": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, full body shot, back view, rear angle, showing back details, hair from behind, complete backside, character turnaround reference",

    "A5_Half_Front": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, front view, upper body focus, detailed torso, chest and head visible, character reference",

    "A6_Half_Back": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, back view, upper body from behind, shoulder and back details, character reference",

    "A7_Half_R45": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, 45 degree right angle, three-quarter view, slight rotation right, character reference",

    "A8_Half_L45": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, 45 degree left angle, three-quarter view, slight rotation left, character reference",

    "A9_Half_Right": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, right side view, 90 degree profile, upper body side angle, character reference",

    "A10_Half_Left": "masterpiece, best quality, ultra detailed, 8k, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, half body shot, waist up, left side view, 90 degree profile, upper body side angle, character reference",

    # Batch B - Close-ups
    "B1_Face_Front": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face front view, head and shoulders, facial features detailed, direct eye contact, character reference",

    "B2_Face_Right": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face right profile, 90 degree side view, jawline visible, ear details, character reference",

    "B3_Face_Left": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, close-up portrait, face left profile, 90 degree side view, jawline visible, ear details, character reference",

    "B4_Over_Shoulder_R": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, over right shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head, character reference",

    "B5_Over_Shoulder_L": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, over left shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head, character reference",

    "B6_Top_Down": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, top-down angle, bird's eye view, looking down at character, overhead perspective, crown of head visible, character reference",

    "B7_Bottom_Up": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, bottom-up angle, worm's eye view, looking up at character, low angle shot, chin and face from below, character reference",

    "B8_Wide_Angle": "masterpiece, best quality, ultra detailed, 8k, professional character portrait, consistent character design, same hairstyle, same facial features, clean white background, studio lighting, wide angle portrait, slight fish-eye effect, dynamic perspective, head and upper torso, dramatic angle, character reference",
}

NEGATIVE_PROMPT = "blurry, low quality, worst quality, jpeg artifacts, ugly, deformed, distorted, duplicate, watermark, text, signature, oversaturated, overexposed, static, unclear details, messy background, complex background, detailed background, three legs, extra fingers, poorly drawn hands, poorly drawn face, malformed limbs, fused fingers, different outfit, different hairstyle, inconsistent character, cropped, out of frame"

# ============= FUNCTIONS =============

def load_workflow(workflow_path):
    """Load workflow JSON"""
    with open(workflow_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def queue_prompt(prompt_data):
    """Queue prompt to ComfyUI"""
    data = json.dumps({"prompt": prompt_data}).encode('utf-8')
    req = urllib.request.Request(f"{COMFYUI_URL}/prompt", data=data)
    req.add_header('Content-Type', 'application/json')

    try:
        response = urllib.request.urlopen(req)
        return json.loads(response.read())
    except Exception as e:
        print(f"❌ Error queuing prompt: {e}")
        return None

def get_history(prompt_id):
    """Get generation history"""
    try:
        with urllib.request.urlopen(f"{COMFYUI_URL}/history/{prompt_id}") as response:
            return json.loads(response.read())
    except:
        return {}

def wait_for_completion(prompt_id, timeout=300):
    """Wait for generation to complete"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        history = get_history(prompt_id)
        if prompt_id in history:
            return history[prompt_id]
        time.sleep(2)
    return None

def update_workflow_prompt(workflow, positive_prompt, seed=None):
    """Update workflow with new prompt"""
    workflow_copy = json.loads(json.dumps(workflow))  # Deep copy

    # Find TextEncodeQwenImageEditPlus node (usually node 80)
    for node_id, node_data in workflow_copy.items():
        if isinstance(node_data, dict) and node_data.get("class_type") == "TextEncodeQwenImageEditPlus":
            # Update positive prompt
            if "inputs" in node_data and "text" in node_data["inputs"]:
                node_data["inputs"]["text"] = positive_prompt

        # Update seed if provided
        if seed is not None and isinstance(node_data, dict) and node_data.get("class_type") == "KSampler":
            if "inputs" in node_data:
                node_data["inputs"]["seed"] = seed

    return workflow_copy

def generate_pose(workflow, pose_name, prompt, seed=None):
    """Generate single pose"""
    print(f"\n{'='*60}")
    print(f"🎨 Generating: {pose_name}")
    print(f"{'='*60}")

    # Update workflow with prompt
    updated_workflow = update_workflow_prompt(workflow, prompt, seed)

    # Queue prompt
    result = queue_prompt(updated_workflow)
    if not result or "prompt_id" not in result:
        print(f"❌ Failed to queue {pose_name}")
        return False

    prompt_id = result["prompt_id"]
    print(f"📋 Prompt ID: {prompt_id}")
    print(f"⏳ Waiting for generation...")

    # Wait for completion
    history = wait_for_completion(prompt_id)
    if not history:
        print(f"⏰ Timeout waiting for {pose_name}")
        return False

    print(f"✅ {pose_name} completed!")
    return True

def main():
    """Main function"""
    print("\n" + "="*60)
    print("🎯 18-POSE CHARACTER SHEET GENERATOR")
    print("="*60)

    # Load workflow
    print(f"\n📂 Loading workflow: {WORKFLOW_FILE}")
    if not os.path.exists(WORKFLOW_FILE):
        print(f"❌ Workflow file not found: {WORKFLOW_FILE}")
        print("💡 Download from: https://raw.githubusercontent.com/khaitrung89/pose-03/claude/nahn65-file-review-019z697KL5iVLMKfRBzJ1LeB/qwen-optimized-single-pose.json")
        return

    workflow = load_workflow(WORKFLOW_FILE)
    print("✅ Workflow loaded")

    # Check ComfyUI connection
    print(f"\n🔌 Connecting to ComfyUI at {COMFYUI_URL}")
    try:
        urllib.request.urlopen(f"{COMFYUI_URL}/system_stats", timeout=5)
        print("✅ ComfyUI connected")
    except:
        print(f"❌ Cannot connect to ComfyUI")
        print("💡 Make sure ComfyUI is running at {COMFYUI_URL}")
        return

    # Optional: Use fixed seed for consistency
    use_fixed_seed = input("\n🎲 Use fixed seed for consistency? (y/n): ").lower() == 'y'
    fixed_seed = 123456 if use_fixed_seed else None

    if use_fixed_seed:
        print(f"🔒 Using fixed seed: {fixed_seed}")
    else:
        print("🎲 Using random seed")

    # Add custom character description
    print("\n💡 Optional: Add character description to all prompts")
    print("   Example: young woman with long black hair, blue dress, green eyes")
    char_desc = input("   Description (press Enter to skip): ").strip()

    # Generate all poses
    print(f"\n{'='*60}")
    print(f"🚀 STARTING GENERATION (18 poses)")
    print(f"{'='*60}")

    success_count = 0
    failed_poses = []

    for i, (pose_name, base_prompt) in enumerate(POSES.items(), 1):
        # Add character description if provided
        if char_desc:
            full_prompt = f"{base_prompt}, {char_desc}"
        else:
            full_prompt = base_prompt

        print(f"\n📊 Progress: {i}/18 ({int(i/18*100)}%)")

        success = generate_pose(workflow, pose_name, full_prompt, fixed_seed)

        if success:
            success_count += 1
        else:
            failed_poses.append(pose_name)

        # Small delay between generations
        if i < 18:
            time.sleep(1)

    # Summary
    print("\n" + "="*60)
    print("📊 GENERATION SUMMARY")
    print("="*60)
    print(f"✅ Successful: {success_count}/18")
    print(f"❌ Failed: {len(failed_poses)}/18")

    if failed_poses:
        print("\nFailed poses:")
        for pose in failed_poses:
            print(f"  - {pose}")

    print("\n💾 Outputs saved in ComfyUI output folder")
    print("📝 Next step: Create grids using ImageMagick or Photoshop")
    print("\n✨ Done!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Generation cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
