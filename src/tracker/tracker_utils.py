from src.common_imports import *
###--------------Here New Logic understand it ------------
 
        
class Detection:
    """
    A class to handle object detection and tracking using a YOLO model and optional ByteTracker.

    Attributes:
    ----------
    model : YOLO
        The YOLO model used for object detection.
    conf_val : float
        The confidence threshold for detections.
    tracker : ByteTracker, optional
        An optional ByteTracker instance for object tracking.
    byte_track_need : bool
        A flag to indicate whether ByteTracker is needed.

    Methods:
    -------
    __init__(MODEL_PATH, byte_tracker=None, byte_track_trigger=False):
        Initializes the Detection class with the YOLO model and optional ByteTracker.

    detect(frame):
        Performs object detection on a given frame and optionally applies tracking.
    """

    def __init__(self, MODEL_PATH, byte_tracker=None, byte_track_trigger=False):
        """
        Initializes the Detection class.

        Parameters:
        ----------
        MODEL_PATH : str
            The path to the YOLO model file.
        byte_tracker : ByteTracker, optional
            An optional ByteTracker instance for object tracking.
        byte_track_trigger : bool, optional
            A flag to indicate whether ByteTracker is needed (default is False).
        """
        self.model = YOLO(MODEL_PATH)
        self.conf_val = 0.3
        self.tracker = byte_tracker
        logging.info(f"The model used is {os.path.dirname(MODEL_PATH)} with confidence value {self.conf_val}")
        self.byte_track_need = byte_track_trigger

    def detect(self, frame):
        """
        Performs object detection on a given frame and optionally applies tracking.

        Parameters:
        ----------
        frame : np.ndarray
            The input image frame for detection.

        Returns:
        -------
        sv.Detections
            The detections in supervision format, with or without tracking applied.

        Raises:
        ------
        CustomException
            If there is an error during detection or tracking.
        """
        result = self.model(frame)[0]
        try:
            # Convert YOLO results to supervision format
            detection_supervision = sv.Detections.from_ultralytics(result)
        except Exception as e:
            raise CustomException(f"Error in supervision detection - {e}", sys)

        if self.byte_track_need:
            try:
                detection_supervision = self.tracker.update_with_detections(detection_supervision)
            except Exception as e:
                raise CustomException(f"Error in supervision detection - {e}", sys)

        if detection_supervision.xyxy.size == 0:
            print(f"No detections found")
        
        return detection_supervision       
        
        
class Track_Details(Detection):
    def __init__(self, track_dict,MODEL_PATH, byte_tracker=None, byte_track_trigger=False):
        self.track_dict = track_dict
        super().__init__(MODEL_PATH=MODEL_PATH, byte_tracker=byte_tracker, byte_track_trigger=byte_track_trigger) 
  
    def get_object_tracks(self,detection_result,frame_no=0):  # here you can give detection supervision results directly 
        if detection_result.xyxy.size == 0:
            return self.track_dict
        
        box_corners =detection_result.data['xyxyxyxy'].tolist()  
        cls_names = detection_result.data['class_name']
        cls_ids = detection_result.class_id
        class_conf = detection_result.confidence
        
        if self.byte_track_need:
            track_id = detection_result.tracker_id
        else:
            track_id = None
        class_conf = detection_result.confidence 
        
        for id, name in enumerate(cls_names):
            p0 =[int(coord) for coord in  box_corners[id][0]]
            p1 =[int(coord) for coord in  box_corners[id][1]]
            p2 =[int(coord) for coord in  box_corners[id][2]]
            p3 =[int(coord) for coord in  box_corners[id][3]]
            obb_angle = get_obb_angle(box_corners[id])
            if obb_angle > 0:
                box_points = [p2,p3,p0,p1]
            else:
                box_points = [p0,p1,p2,p3]
                
            track_key = track_id[id] if track_id is not None else id
            self.track_dict.setdefault(frame_no, {}).setdefault(name, {})[track_key] = {"box_corners":box_points}

            # if name != "NG":
            self.track_dict[frame_no][name][track_key]["obb_angle"] = obb_angle
            self.track_dict[frame_no][name][track_key]["mid_point"] = get_mid_point(box_points)
            self.track_dict[frame_no][name][track_key]["confidence"] = class_conf[id]
            self.track_dict[frame_no][name][track_key]["text_position"] = box_points[2]
            self.track_dict[frame_no][name][track_key]["box_size"] = get_box_size(box_points)
            