import cv2 
import os 
from src.logger import logging

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames=[]
    # frame_num = 0
    while True:
        ret,frame = cap.read()
        if not ret :
            break

        frames.append(frame)
        # break
    logging.info(f"Succesfully read {os.path.dirname(video_path)} contains {len(frames)} frames")
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_video_path,fourcc,24,(output_video_frames[0].shape[1],output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    logging.info(f"Successfully saved {output_video_path}")
    out.release()
    

def read_image(image_path):
    img = cv2.imread(image_path)
    logging.info(f"The image read from {image_path} is {img.shape}")
    return img

def save_image(image, image_path):
    cv2.imwrite(image_path, image)
    logging.info(f"Successfully saved {image_path}")