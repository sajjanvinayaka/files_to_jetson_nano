import cv2
import numpy as np
from typing import Tuple
from src.constants.enums import ColorEnum

def box_annotate(frame,cls_name,box_corners):
    if not box_corners:
        return frame
    points = np.array(box_corners,dtype =np.int32)
    color = ColorEnum.get_color(cls_name)
    cv2.polylines(frame,[points],isClosed=True, color = color, thickness = 2)
    
    return frame
    
    
def point_annotate(frame: np.ndarray, cls_name: str, mid_points: list, radius: int=20) -> np.ndarray:
    # print(f"Inside the mid_point_anjotate_function \n {cls_name}\n {mid_points}")
    """
    Draws a filled circle at the given midpoint on the frame.

    Args:
        frame (np.ndarray): The image frame.
        cls_name (str): Class name for determining annotation color.
        mid_points (Tuple[int, int]): X, Y coordinates of the midpoint.
        radius (int): Radius of the circle.

    Returns:
        np.ndarray: The modified frame with the annotation.
    """
    if mid_points is None:
        print(f"Inside the mid_point_annoatate_funtion, no mid points found {mid_points}")
        return frame

    color = ColorEnum.get_color(cls_name)  # Assuming ColorEnum is defined elsewhere
    mid_point_np = tuple(mid_points)  # Ensure tuple format
    cv2.circle(frame, mid_point_np, radius=radius, color=color, thickness=-1)

    return frame

# def add_text_annotate(frame, cls_name, position):
#     if not position:
#         return frame 
    
#     color = ColorEnum.get_color(cls_name)
#     position_np =  tuple(np.array(position,dtype =np.int32))
#     cv2.putText(frame,f"{cls_name}",position_np, cv2.FONT_HERSHEY_SIMPLEX,1,color,3)
#     return frame

def add_text_annotate(frame, cls_name, position, box_size):
    if not position or not box_size:
        return frame
    
    color = ColorEnum.get_color(cls_name)
    position_np = tuple(np.array(position, dtype=np.int32))
    
    # Calculate the size of the text
    font_scale = 1
    thickness = 3
    text_size = cv2.getTextSize(f"{cls_name}", cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
    
    # Adjust the font scale if the text size is larger than the box size
    while text_size[0] > box_size[0] or text_size[1] > box_size[1]:
        font_scale -= 0.1
        text_size = cv2.getTextSize(cls_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
        if font_scale <= 0.1:  # Prevent font scale from becoming too small
            font_scale = 0.1
            break
    
    cv2.putText(frame, f"{cls_name}", position_np, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
    return frame