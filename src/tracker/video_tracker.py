from src.common_imports import *    
from src.tracker.tracker_utils import Track_Details


class VideoTracker(Track_Details):
     def __init__(self, track_dict,MODEL_PATH, byte_tracker=None, byte_track_trigger=False):
         super().__init__(track_dict=track_dict,MODEL_PATH=MODEL_PATH, byte_tracker=byte_tracker, byte_track_trigger=byte_track_trigger)
     
     def video_get_object_tracks(self,video_frames):
         #Here I have to use the multi threading for the video frames
         for frame_no, frame in video_frames:
             detection_supervision = self.detect(frame)
             
             