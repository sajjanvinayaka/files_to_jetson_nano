from src.common_imports import *
from src.constants.enums import Ratios

def get_obb_angle(box_corners):
    x1,y1 = box_corners[0]
    x2,y2 = box_corners[1]
    angle_rad = np.arctan2(y2-y1,x2-x1)
    angle_deg = np.degrees(angle_rad)
    return angle_deg

def get_mid_point(box_points):
    x1,y1 = box_points[1]
    x2,y2 = box_points[2]
    return [int((x1 +x2)/2), (int(max(y1,y2)) - 10)]
  

# def get_text_position(box_corners,obb_angle):
#     if obb_angle < 0:
#         return box_corners[2]
#     if obb_angle > 0:
#         return box_corners[0]


   
def get_box_size(box_corners):
    p0 = box_corners[0]
    p1 = box_corners[1]
    p2 = box_corners[2]
    p3 = box_corners[3]
    x_width = p0[0] - p3[0]
    y_height = p0[1] - p1[1]
    return (x_width,y_height)


def common_radius_calc(track):
    """
    Calculate the common radius of the bounding box of the track.
    """
    width, _ = track['box_size']
    ratio = Ratios.get_ratio("point_ratio")
    radius = int(ratio * width)
    return radius

def common_y_offset_calc(track):
    """
    Calculate the common y offset of the bounding box of the track.
    """
    _, height = track['box_size']
    ratio = Ratios.get_ratio("offset_y_ratio")
    y_offset = int(ratio * height)
    return y_offset