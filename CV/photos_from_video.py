import cv2
import os

def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    
    cap.release()
    print(f"Saved {frame_count} frames to {output_folder}")

# Использование
video_path = "video.mp4"  # Укажите путь к вашему видео
output_folder = "frames"  # Папка для сохранения кадров
extract_frames(video_path, output_folder)
