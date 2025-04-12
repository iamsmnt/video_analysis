import os
import sys
import clip
import torch
import numpy as np
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import frames


device = "cuda" if torch.cuda.is_available() else "cpu"
mac_device = "mps" if torch.backends.mps.is_available else device
print(f"device found: {mac_device}")
model, preprocess = clip.load("ViT-B/32", device=mac_device)

def embed_frames(frames):
    print(f"inside embed_frames!")
    preprocessed = [preprocess(Image.fromarray(f)).unsqueeze(0).to(mac_device) for f in frames]
    with torch.no_grad():
        embeddings = [model.encode_image(img) for img in preprocessed]
    embeddings = torch.stack(embeddings)
    return embeddings.mean(dim=0).cpu().numpy()

if __name__=="__main__":
    # from utils import frames
    video_path = "/Users/somnathmahato/video_analysis/tests/files/test_video_1.mp4"
    video_name = video_path.split("/")[-1]
    frames = frames.extract_frames(video_path)
    print(f"Got {len(frames)} frames from video: {video_name}")
    video_embeddings = embed_frames(frames)
    print("Embeddings generated successfully!")
