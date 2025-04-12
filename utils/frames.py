import cv2

def extract_frames(video_path, fps=1):
    print("Inside extract frames!")
    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(video_fps / fps) if video_fps > 0 else 1

    frames = []
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % interval == 0:
            frames.append(frame)
        i += 1
    cap.release()
    return frames


if __name__=="__main__":
    video_path = "/Users/somnathmahato/video_analysis/tests/files/test_video_1.mp4"
    video_name = video_path.split("//")[-1]
    frames = extract_frames(video_path=video_path)
    print(f"Frames Extracted Successfully!")
    print(f"Got {len(frames)} frames from video: {video_name}")