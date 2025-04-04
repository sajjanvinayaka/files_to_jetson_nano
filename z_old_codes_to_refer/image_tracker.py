from src.common_imports import *
       
class ImageTracker:
    def __init__(self,MODEL_PATH):
        self.model = YOLO(MODEL_PATH)
        self.conf_val = 0.3
        logging.info(f"The model used is {os.path.dirname(MODEL_PATH)} with confidence value {self.conf_val}")
        #Here you need the connection control 
        self.annotations_methods = {
            "type_1_N" : Type_1_annotation(),
            "type_2_N" : Type_2_annotation(),
            "type_3_Y" : Type_3_annotation(),
            "type_4_N" : Type_4_annotation(),
        }
        
        self.default_annoatation = DefaultAnnotation()
        # This is one for error handling for if the sub class is not defiend for new object class 
        self.default_box_annoatate = DefaultBoxAnnotation() 

    def get_image_track(self,img):
        Image = img.copy()
        result = self.model(Image)[0]
        try:
            # Convert YOLO results to supervision format
            detection_supervision = sv.Detections.from_ultralytics(result)
        except Exception as e:
            raise CustomException(f"Error in supervision detection - {e}",sys)
        # print(detection_supervision)
        if detection_supervision.xyxy.size == 0:
            print(f"No detections, found ")
            return None
        # print(detection_supervision)
        box_corners =detection_supervision.data['xyxyxyxy'].tolist()  
        cls_names = detection_supervision.data['class_name']
        # track_id = detection_supervision.tracker_id
        class_conf = detection_supervision.confidence
        
        # for loop iniated with the no of obj classes detected in an image:
        for id, name in enumerate(cls_names):
            p0 =[int(coord) for coord in  box_corners[id][0]]
            p1 =[int(coord) for coord in  box_corners[id][1]]
            p2 =[int(coord) for coord in  box_corners[id][2]]
            p3 =[int(coord) for coord in  box_corners[id][3]]
            obb_angle = get_obb_angle(box_corners[id])
            # change the points if obb has > 0, as the points position gets misplaced 
            if obb_angle > 0:
                box_points = [p2,p3,p0,p1]
            else:
                box_points = [p0,p1,p2,p3]
            track ={
                "box_corners":  box_points,
                "cls_name":     name,
                "obb_angle" :   obb_angle,
                "mid_point":    get_mid_point(box_points),
                "confidence":   class_conf[id],
                "text_position":box_points[2],
                "box_size":     get_box_size(box_points),
            }
            # print("Track attributes\n ", track)
            Image = self.default_box_annoatate.draw(Image, track)
            class_annotation_assign = self.annotations_methods.get(name,self.default_annoatation)
            print(class_annotation_assign)
            Image = class_annotation_assign.draw(Image, track)

        return Image