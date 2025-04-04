from src.tracker import Tracker, NewTracker
from src.utils.video_utils import read_video,save_video,read_image,save_image
from src.config.configuration import *
from src.exception import CustomException
import sys
import os 
from pathlib import Path 
import glob 
# For now just give video as the input 
# Have to 
def main():
    
    # read_file_path = IMAGE_INPUT_MULTIPLE_FOLDER
    # tracker = Tracker(MODEL_PATH) 
    # output_path = r"output_images"
    # if not os.path.exists(output_path):
    #     try:
    #         os.makedirs(output_path)
    #     except Exception as e:
    #         logging.info("Error in making output folder dir")
    #         raise CustomException(e,sys)   

    # # Getting all the image paths in the list 
    # input_folder = Path(read_file_path)  
    # image_paths = [file for ext in ["jpg", "png", "jpeg", "bmp"] for file in input_folder.glob(f"*.{ext}")]
    # # print(image_paths)
    # for image in image_paths:
    #     img = read_image(image)
    #     output_image = tracker.get_image_track(img)
    #     save_image(output_image,os.path.join(output_path,os.path.basename(image)))
        
        
    read_file_path = IMAGE_INPUT_MULTIPLE_FOLDER
    tracker = NewTracker(MODEL_PATH) 
    output_path = r"output_images"
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path)
        except Exception as e:
            logging.info("Error in making output folder dir")
            raise CustomException(e,sys)   

    # Getting all the image paths in the list 
    input_folder = Path(read_file_path)  
    image_paths = [file for ext in ["jpg", "png", "jpeg", "bmp"] for file in input_folder.glob(f"*.{ext}")]
    # print(image_paths)
    for image in image_paths:
        img = read_image(image)
        output_image = tracker.get_image_track(img)
        save_image(output_image,os.path.join(output_path,os.path.basename(image)))
        
        


if __name__ == "__main__":
    main()