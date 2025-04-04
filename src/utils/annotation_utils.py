
from src.common_imports import *


class DrawFuncErrHandling:
    def draw(self,Image, track):
        raise CustomException("New class not implemented ",sys)

class DefaultAnnotation(DrawFuncErrHandling):
    def draw(self, Image, track):
        print(f"Default box annotation for unknown class: {track['cls_name']}")
        return Image
    
class DefaultBoxAnnotation(DrawFuncErrHandling):     
    def draw(self, Image, track):
        Image = box_annotate(Image, track["cls_name"], track["box_corners"])
        return Image

class DefaultAnnotation(DrawFuncErrHandling):
    def draw(self, Image, track):
        print(f"Default annotation for unknown class: {track['cls_name']}")
    
class Type_1_annotation(DrawFuncErrHandling):
    def draw(self, Image, track):
        x,y = track['mid_point'][0],(track['mid_point'][1] - 20)
        radius = common_radius_calc(track)
        Image = point_annotate(Image,'mid_point', [x,y], radius)
        return Image


class Type_2_annotation(DrawFuncErrHandling):
    def draw(self, Image, track):
        radius = common_radius_calc(track)
        x,y = track['mid_point'][0],(track['mid_point'][1] + common_y_offset_calc(track))
        Image = point_annotate(Image,'mid_point',[x,y], radius)
        return Image

class Type_3_annotation(DrawFuncErrHandling):
    def draw(self, Image, track):
        x,y = track['mid_point'][0],(track['mid_point'][1] - 20)
        radius = common_radius_calc(track)
        Image = point_annotate(Image,'mid_point', [x,y], radius)
        return Image
        
class Type_4_annotation(DrawFuncErrHandling):
    def draw(self, Image, track):
        p1 = track['box_corners'][1]
        p2 = track['box_corners'][2]
        mid_point = track['mid_point']
        radius = common_radius_calc(track)
        right_point = [int((mid_point[0]+p1[0])/2), mid_point[1]+ common_y_offset_calc(track) - 10]
        left_point = [int((mid_point[0]+p2[0])/2) - 30 ,mid_point[1] - 10]
        Image = point_annotate(Image,'mid_point', right_point,radius)
        Image = point_annotate(Image,'mid_point', left_point,radius)
        return Image