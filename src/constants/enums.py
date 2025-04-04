from src.common_imports import *

class ColorEnum(Enum):
    @staticmethod
    def hex_to_bgr(hex_color):
        hex_color = hex_color.lstrip('#')
        r,g,b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return (b,g,r)
    
    NG = hex_to_bgr("#FE0056")   # RED
    NOTHING = hex_to_bgr("#FE0056")
    MID_POINT = hex_to_bgr("#FE0056")  # GOLD
    
    TYPE_1_N = hex_to_bgr("#8622FF")
    TYPE_1_Y = hex_to_bgr("#00ff32")
    
    TYPE_2_N = hex_to_bgr("#FF8000")
    TYPE_2_Y = hex_to_bgr("#00B7EB")
    
    TYPE_3_N = hex_to_bgr("#FF00FF")
    TYPE_3_Y = hex_to_bgr("#FFFF00")
    
    TYPE_4_N = hex_to_bgr("#0E7AFE")
    TYPE_4_Y = hex_to_bgr("#FFABAB")
    
    OTHER = hex_to_bgr("#000000")  # BLACK
    

    @classmethod
    def get_color(cls,class_name):
        return cls.__members__.get(class_name.upper(),cls.OTHER).value
    
    
class Ratios(Enum):
    DEFAULT = 1
    POINT_RATIO = round(20/940, 3)
    
    OFFSET_Y_RATIO = round( 45/ 230 , 3)
    
    
    
    @classmethod
    def get_ratio(cls, ratio_name):
        return cls.__members__.get(ratio_name.upper(), cls.DEFAULT).value
    