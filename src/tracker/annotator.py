
from src.common_imports import *
# from src.utils.annotation_utils_2M import *

class Annotator:
    def __init__(self):
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

    def annotate(self, Image, track_details):
        for cls_name, class_name_attributes in track_details.items():
            assigned_class_name_annotator = self.annotations_methods.get(cls_name,self.default_annoatation)
            print(assigned_class_name_annotator)
            for track_id, track_id_attributes in class_name_attributes.items():
                temp_track = track_id_attributes
                temp_track["cls_name"] = cls_name 
                Image = self.default_box_annoatate.draw(Image, temp_track)  
                Image = assigned_class_name_annotator.draw(Image, temp_track)
        return Image 
    

    
class ImageAnnotator(Annotator):
    def __init__(self,Image,track_details):
        self.Image = Image
        # Image is single so always the frame no will be 0 
        # self.Image_track_details = track_details[0]
        self.Image_track_details = track_details
        super().__init__()
        
    def image_annotation(self):
        annotated_Image = self.annotate(self.Image,self.Image_track_details)
        return annotated_Image