#!/usr/bin/env python3
"""
18-Pose Character Sheet Workflow Generator
Generates ComfyUI workflow JSON for 18 different character poses
"""

import json

# Configuration
POSITIVE_BASE = "masterpiece, best quality, ultra detailed, 8k resolution, professional character sheet, consistent character design, same outfit, same hairstyle, same facial features, clean white background, studio lighting, character reference sheet"

NEGATIVE_BASE = "blurry, low quality, worst quality, jpeg artifacts, ugly, deformed, distorted, duplicate, watermark, text, signature, oversaturated, overexposed, unclear details, messy background, complex background, three legs, extra fingers, poorly drawn hands, poorly drawn face, malformed limbs, fused fingers, different outfit, different hairstyle, inconsistent character, cropped, out of frame"

# 18 Pose definitions
POSES = [
    # Batch A - Body Shots (10)
    ("A1_Full_Front", "full body front view, standing straight, facing camera directly, arms at sides, neutral stance"),
    ("A2_Full_Right", "full body right side view, 90 degree angle, profile shot, complete side silhouette"),
    ("A3_Full_Left", "full body left side view, 90 degree angle, profile shot, complete side silhouette"),
    ("A4_Full_Back", "full body back view, rear angle, showing back details, hair from behind, complete backside"),
    ("A5_Half_Front", "half body shot, waist up, front view, upper body focus, detailed torso, chest and head visible"),
    ("A6_Half_Back", "half body shot, waist up, back view, upper body from behind, shoulder and back details"),
    ("A7_Half_R45", "half body shot, waist up, 45 degree right angle, three-quarter view, slight rotation right"),
    ("A8_Half_L45", "half body shot, waist up, 45 degree left angle, three-quarter view, slight rotation left"),
    ("A9_Half_Right", "half body shot, waist up, right side view, 90 degree profile, upper body side angle"),
    ("A10_Half_Left", "half body shot, waist up, left side view, 90 degree profile, upper body side angle"),
    # Batch B - Close-ups (8)
    ("B1_Face_Front", "close-up portrait, face front view, head and shoulders, facial features detailed, direct eye contact"),
    ("B2_Face_Right", "close-up portrait, face right profile, 90 degree side view, jawline visible, ear details"),
    ("B3_Face_Left", "close-up portrait, face left profile, 90 degree side view, jawline visible, ear details"),
    ("B4_Over_Shoulder_R", "over right shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head"),
    ("B5_Over_Shoulder_L", "over left shoulder view, looking back angle, 3/4 back view, shoulder in frame, turning head"),
    ("B6_Top_Down", "top-down angle, bird's eye view, looking down at character, overhead perspective, crown of head visible"),
    ("B7_Bottom_Up", "bottom-up angle, worm's eye view, looking up at character, low angle shot, chin and face from below"),
    ("B8_Wide_Angle", "wide angle portrait, slight fish-eye effect, dynamic perspective, head and upper torso, dramatic angle"),
]

def generate_workflow():
    """Generate complete 18-pose workflow"""

    workflow = {
        "id": "18-pose-complete-v1",
        "revision": 1,
        "last_node_id": 200,
        "last_link_id": 300,
        "nodes": [],
        "links": [],
        "groups": [],
        "config": {},
        "extra": {
            "ds": {"scale": 0.7, "offset": [400, 600]},
            "workspace_info": {
                "name": "18-Pose Character Sheet (Complete)",
                "version": "1.0",
                "author": "pose-03",
                "description": "Complete 18-pose character sheet generation in one run"
            }
        },
        "version": 0.4
    }

    node_id = 1
    link_id = 1

    print("🔨 Generating 18-Pose Workflow...")
    print("=" * 60)

    # 1. Title Note
    workflow["nodes"].append({
        "id": node_id,
        "type": "Note",
        "pos": [50, -900],
        "size": [1400, 140],
        "flags": {},
        "order": 0,
        "mode": 0,
        "title": "🎨 18-Pose Character Sheet Generator - COMPLETE",
        "properties": {},
        "widgets_values": [
            "✨ AUTOMATED 18-POSE GENERATION IN ONE RUN\\n" +
            "🔧 Optimized: Denoise 0.70 | CFG 6.5 | Steps 30\\n" +
            "📦 Output: 18 individual poses (Batch A: 10 body shots | Batch B: 8 close-ups)\\n" +
            "⚡ All poses generated in parallel - professional quality character reference sheet"
        ],
        "color": "#1a5490",
        "bgcolor": "#2d6ca8"
    })
    print(f"✅ Node {node_id}: Title Note")
    node_id += 1

    # 2. LoadImage
    load_image_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "LoadImage",
        "pos": [-700, -400],
        "size": [350, 520],
        "flags": {},
        "order": 1,
        "mode": 0,
        "inputs": [],
        "outputs": [
            {"name": "IMAGE", "type": "IMAGE", "links": [link_id]},
            {"name": "MASK", "type": "MASK", "links": None}
        ],
        "properties": {"Node name for S&R": "LoadImage"},
        "widgets_values": ["character_reference.png", "image"],
        "title": "📷 Input Character Image"
    })
    image_output_link = link_id
    print(f"✅ Node {node_id}: LoadImage")
    node_id += 1
    link_id += 1

    # 3. SeaArtUnetLoader
    model_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "SeaArtUnetLoader",
        "pos": [-300, -700],
        "size": [320, 85],
        "flags": {},
        "order": 2,
        "mode": 0,
        "inputs": [],
        "outputs": [{"name": "MODEL", "type": "MODEL", "links": [link_id]}],
        "properties": {"Node name for S&R": "SeaArtUnetLoader"},
        "widgets_values": ["Qwen-Image-Edit-Rapid-AIO", "default"],
        "serialize_values": ["d394rt5e878c738b06r0@619ba541a84453b7116e974a5ab39e1d", None],
        "title": "🧠 Qwen Model"
    })
    model_output_link = link_id
    print(f"✅ Node {node_id}: Model Loader")
    node_id += 1
    link_id += 1

    # 4. CLIPLoader
    clip_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "CLIPLoader",
        "pos": [-300, -580],
        "size": [320, 106],
        "flags": {},
        "order": 3,
        "mode": 0,
        "inputs": [],
        "outputs": [{"name": "CLIP", "type": "CLIP", "links": list(range(link_id, link_id + 36))}],  # 18*2 = 36 links
        "properties": {"Node name for S&R": "CLIPLoader"},
        "widgets_values": ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default"],
        "title": "🎨 CLIP Encoder"
    })
    clip_output_links = list(range(link_id, link_id + 36))
    print(f"✅ Node {node_id}: CLIP Loader")
    node_id += 1
    link_id += 36

    # 5. VAELoader
    vae_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "VAELoader",
        "pos": [-300, -440],
        "size": [320, 60],
        "flags": {},
        "order": 4,
        "mode": 0,
        "inputs": [],
        "outputs": [{"name": "VAE", "type": "VAE", "links": list(range(link_id, link_id + 20))}],  # 1 encode + 18 decode + 1 spare
        "properties": {"Node name for S&R": "VAELoader"},
        "widgets_values": ["qwen_image_vae.safetensors"],
        "title": "🔧 VAE"
    })
    vae_output_links = list(range(link_id, link_id + 20))
    print(f"✅ Node {node_id}: VAE Loader")
    node_id += 1
    link_id += 20

    # 6. FluxKontextImageScale
    scale_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "FluxKontextImageScale",
        "pos": [-300, -60],
        "size": [320, 30],
        "flags": {},
        "order": 5,
        "mode": 0,
        "inputs": [{"name": "image", "type": "IMAGE", "link": image_output_link}],
        "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": list(range(link_id, link_id + 37))}],  # 1 encode + 36 text encode
        "properties": {"Node name for S&R": "FluxKontextImageScale"},
        "widgets_values": [],
        "title": "📐 Auto-Scale"
    })
    scaled_image_links = list(range(link_id, link_id + 37))
    print(f"✅ Node {node_id}: Image Scaler")
    node_id += 1
    link_id += 37

    # 7. VAEEncode (shared)
    encode_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "VAEEncode",
        "pos": [-300, 20],
        "size": [220, 50],
        "flags": {},
        "order": 6,
        "mode": 0,
        "inputs": [
            {"name": "pixels", "type": "IMAGE", "link": scaled_image_links[0]},
            {"name": "vae", "type": "VAE", "link": vae_output_links[0]}
        ],
        "outputs": [{"name": "LATENT", "type": "LATENT", "links": list(range(link_id, link_id + 18))}],
        "properties": {"Node name for S&R": "VAEEncode"},
        "title": "🔄 VAE Encode (Shared)"
    })
    latent_links = list(range(link_id, link_id + 18))
    print(f"✅ Node {node_id}: VAE Encoder")
    node_id += 1
    link_id += 18

    # 8. ModelSamplingAuraFlow
    auraflow_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "ModelSamplingAuraFlow",
        "pos": [50, -700],
        "size": [290, 65],
        "flags": {},
        "order": 7,
        "mode": 0,
        "inputs": [{"name": "model", "type": "MODEL", "link": model_output_link}],
        "outputs": [{"name": "MODEL", "type": "MODEL", "links": [link_id]}],
        "properties": {"Node name for S&R": "ModelSamplingAuraFlow"},
        "widgets_values": [3.5],
        "title": "⚙️ AuraFlow"
    })
    auraflow_output = link_id
    print(f"✅ Node {node_id}: AuraFlow Sampling")
    node_id += 1
    link_id += 1

    # 9. CFGNorm
    cfgnorm_id = node_id
    workflow["nodes"].append({
        "id": node_id,
        "type": "CFGNorm",
        "pos": [50, -605],
        "size": [290, 65],
        "flags": {},
        "order": 8,
        "mode": 0,
        "inputs": [{"name": "model", "type": "MODEL", "link": auraflow_output}],
        "outputs": [{"name": "patched_model", "type": "MODEL", "links": list(range(link_id, link_id + 18))}],
        "properties": {"Node name for S&R": "CFGNorm"},
        "widgets_values": [1.0],
        "title": "🎚️ CFG Norm"
    })
    model_links = list(range(link_id, link_id + 18))
    print(f"✅ Node {node_id}: CFG Normalization")
    node_id += 1
    link_id += 18

    print(f"\n📋 Base nodes complete! Starting pose generation...")
    print(f"   Total base nodes: {node_id - 1}")

    # Generate 18 pose pipelines
    for pose_idx, (pose_name, pose_desc) in enumerate(POSES):
        print(f"\n🎨 Generating Pose {pose_idx + 1}/18: {pose_name}")

        # Calculate positions
        col = pose_idx % 6
        row = pose_idx // 6
        base_x = 400 + (col * 300)
        base_y = -400 + (row * 600)

        # Positive prompt
        pos_prompt_id = node_id
        full_positive = f"{POSITIVE_BASE}, {pose_desc}"
        workflow["nodes"].append({
            "id": node_id,
            "type": "TextEncodeQwenImageEditPlus",
            "pos": [base_x, base_y],
            "size": [280, 180],
            "flags": {},
            "order": 9 + pose_idx * 5,
            "mode": 0,
            "inputs": [
                {"name": "clip", "type": "CLIP", "link": clip_output_links[pose_idx * 2]},
                {"name": "vae", "type": "VAE", "link": vae_output_links[1 + pose_idx]},
                {"name": "image1", "type": "IMAGE", "link": scaled_image_links[1 + pose_idx * 2]}
            ],
            "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [link_id]}],
            "properties": {"Node name for S&R": "TextEncodeQwenImageEditPlus"},
            "widgets_values": [full_positive, [False, True]],
            "title": f"✅ {pose_name[:15]}",
            "color": "#232",
            "bgcolor": "#353"
        })
        pos_cond_link = link_id
        node_id += 1
        link_id += 1

        # Negative prompt
        neg_prompt_id = node_id
        workflow["nodes"].append({
            "id": node_id,
            "type": "TextEncodeQwenImageEditPlus",
            "pos": [base_x, base_y + 200],
            "size": [280, 180],
            "flags": {},
            "order": 10 + pose_idx * 5,
            "mode": 0,
            "inputs": [
                {"name": "clip", "type": "CLIP", "link": clip_output_links[pose_idx * 2 + 1]},
                {"name": "vae", "type": "VAE", "link": vae_output_links[1 + pose_idx]},
                {"name": "image1", "type": "IMAGE", "link": scaled_image_links[2 + pose_idx * 2]}
            ],
            "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [link_id]}],
            "properties": {"Node name for S&R": "TextEncodeQwenImageEditPlus"},
            "widgets_values": [NEGATIVE_BASE, [False, True]],
            "title": f"❌ Negative",
            "color": "#322",
            "bgcolor": "#533"
        })
        neg_cond_link = link_id
        node_id += 1
        link_id += 1

        # KSampler
        sampler_id = node_id
        workflow["nodes"].append({
            "id": node_id,
            "type": "KSampler",
            "pos": [base_x, base_y + 400],
            "size": [280, 270],
            "flags": {},
            "order": 11 + pose_idx * 5,
            "mode": 0,
            "inputs": [
                {"name": "model", "type": "MODEL", "link": model_links[pose_idx]},
                {"name": "positive", "type": "CONDITIONING", "link": pos_cond_link},
                {"name": "negative", "type": "CONDITIONING", "link": neg_cond_link},
                {"name": "latent_image", "type": "LATENT", "link": latent_links[pose_idx]}
            ],
            "outputs": [{"name": "LATENT", "type": "LATENT", "links": [link_id]}],
            "properties": {"Node name for S&R": "KSampler"},
            "widgets_values": [123456 + pose_idx, "fixed", 30, 6.5, "euler_ancestral", "karras", 0.70],
            "title": f"🎲 {pose_name[:15]}"
        })
        sampler_output = link_id
        node_id += 1
        link_id += 1

        # VAEDecode
        decode_id = node_id
        workflow["nodes"].append({
            "id": node_id,
            "type": "VAEDecode",
            "pos": [base_x + 300, base_y + 400],
            "size": [220, 50],
            "flags": {},
            "order": 12 + pose_idx * 5,
            "mode": 0,
            "inputs": [
                {"name": "samples", "type": "LATENT", "link": sampler_output},
                {"name": "vae", "type": "VAE", "link": vae_output_links[1 + pose_idx]}
            ],
            "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": [link_id]}],
            "properties": {"Node name for S&R": "VAEDecode"},
            "title": "🔄 Decode"
        })
        image_link = link_id
        node_id += 1
        link_id += 1

        # SaveImage
        save_id = node_id
        workflow["nodes"].append({
            "id": node_id,
            "type": "SaveImage",
            "pos": [base_x + 300, base_y + 480],
            "size": [280, 400],
            "flags": {},
            "order": 13 + pose_idx * 5,
            "mode": 0,
            "inputs": [{"name": "images", "type": "IMAGE", "link": image_link}],
            "outputs": [],
            "properties": {"Node name for S&R": "SaveImage"},
            "widgets_values": [f"18Pose_{pose_name}"],
            "title": f"💾 {pose_name}"
        })
        node_id += 1

        print(f"   ✅ Complete: {pose_name} (5 nodes)")

    # Add workflow links - properly build from node connections
    workflow["links"] = []

    # Helper to extract links from node outputs
    for node in workflow["nodes"]:
        if "outputs" in node:
            for output_idx, output in enumerate(node["outputs"]):
                if "links" in output and output["links"]:
                    for link_id_out in output["links"]:
                        # Find target node that uses this link
                        for target_node in workflow["nodes"]:
                            if "inputs" in target_node:
                                for input_idx, inp in enumerate(target_node["inputs"]):
                                    if inp.get("link") == link_id_out:
                                        workflow["links"].append([
                                            link_id_out,
                                            node["id"],
                                            output_idx,
                                            target_node["id"],
                                            input_idx,
                                            output.get("type", "AUTO")
                                        ])

    # Add groups
    workflow["groups"] = [
        {"title": "📥 INPUT & MODELS", "bounding": [-730, -750, 450, 850], "color": "#3f789e"},
        {"title": "⚙️ OPTIMIZATION", "bounding": [20, -750, 350, 200], "color": "#8A5082"},
        {"title": "🎨 POSE GENERATION (18 Parallel Pipelines)", "bounding": [370, -450, 1800, 1400], "color": "#b58b2a"}
    ]

    workflow["last_node_id"] = node_id
    workflow["last_link_id"] = link_id

    print(f"\n" + "=" * 60)
    print(f"✅ Workflow Generation Complete!")
    print(f"   Total nodes: {node_id - 1}")
    print(f"   Total links: {link_id - 1}")
    print(f"   18 poses ready for parallel generation")

    return workflow

if __name__ == "__main__":
    workflow = generate_workflow()

    output_file = "18-Pose-Complete-Workflow.json"
    with open(output_file, 'w') as f:
        json.dump(workflow, f, indent=2)

    print(f"\n💾 Saved to: {output_file}")
    print(f"📊 File size: {len(json.dumps(workflow)) / 1024:.1f} KB")
    print("\n🎉 Ready to import to ComfyUI!")
