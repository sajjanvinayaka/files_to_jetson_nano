from src.common_imports import *
from src.tracker.image_tracker import Track_Details,ImageTracker
from src.tracker.annotator import ImageAnnotator,Annotator
# For now just give image as the input 
# Have to do it for the video

def output_folder_check():
    image_output_path = r"output_images"
    if not os.path.exists(image_output_path):
        try:
            os.makedirs(image_output_path)
        except Exception as e:
            logging.info("Error in making output folder dir")
            raise CustomException(e,sys)

    video_output_path = r"output_videos"
    if not os.path.exists(video_output_path):
        try:
            os.makedirs(video_output_path)
        except Exception as e:
            logging.info("Error in making output folder dir")
            raise CustomException(e,sys) 
    
    
def image_main(): 
    output_path = r"output_images" 
    #Definers
    model_path = MODEL_PATH
    track_details_dict = {}
    tracker_details = ImageTracker(track_details_dict,model_path)    
    image_annotator = Annotator()
    read_file_path = IMAGE_INPUT_MULTIPLE_FOLDER
    input_folder = Path(read_file_path)
    
    # Getting all the image paths in the list 
    image_paths = [file for ext in ["jpg", "png", "jpeg", "bmp"] for file in input_folder.glob(f"*.{ext}")]
    # print(image_paths)
    
    
    for img_no, image in enumerate(image_paths):
        img = read_image(image)
        supervision_results = tracker_details.detect(img)
        
        # Updating the tracker_details_dict with image_no as frame_no
        tracker_details.get_object_tracks(supervision_results,img_no)
        
        annotated_image = image_annotator.annotate(img,track_details_dict[img_no])
        # annotated_image = image_annotator.image_annotation()
        save_image(annotated_image,os.path.join(output_path,os.path.basename(image)))


def stub_path_file_checker(file_path):
    stub_path = STUB_PATH
    stub_folder = Path(stub_path)
    stub_folder_file_names = [file.stem for file in stub_folder.glob("*.pkl")]
    file_path_name = Path(file_path).stem
    if file_path_name in stub_folder_file_names:
        return Path.joinpath(stub_folder,Path(file_path_name).with_suffix(".pkl"))
    else:
        return None   
def video_main():
    
    output_path = r"output_videos"
    #Definers
    model_path = MODEL_PATH
    track_details_dict = {}
    tracker_details = Track_Details(track_details_dict,model_path)    
    video_annotator = Annotator()
    
    
    read_video_file_path = VIDEO_INPUT_PATH
    input_video_folder = Path(read_video_file_path)
    video_paths = [file for ext in ["mp4", "avi", "mov"] for file in input_video_folder.glob(f"*.{ext}")]
    
    
    for video_no, video_path in enumerate(video_paths):
        video_frames = read_video(video_path)
        result_from_stub = stub_path_file_checker(video_path)
        if result_from_stub is not None:
            try: 
                with open(result_from_stub, 'rb') as f:
                    track_details_dict = pickle.load(f)
            except Exception as e:
                raise CustomException(e,sys)
            
        else: 
            ########################## Continue the program here 
            for frame_no, frame in enumerate(video_frames):
                supervision_results_frame = tracker_details.detect(frame)
                tracker_details.get_object_tracks(supervision_results_frame,frame_no)
            ###Remeber at this stage I have populated the tracker_details_dict    
            
                
        
        output_video_frames = []
        for frame_no, frame in enumerate(video_frames):
            annotated_frame = video_annotator.annotate(frame,track_details_dict[frame_no])
            output_video_frames.append(annotated_frame)
            
        save_video(output_video_frames,os.path.join(output_path,os.path.basename(video_path)))

        ####After the process I am clearing the "tracker_details_dict" and "output_video_frames"
        track_details_dict = {}
        output_video_frames = []

  
if __name__ == "__main__":
    # main()
    image_main()