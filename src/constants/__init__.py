from src.common_imports import *



def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()


#Root directory
ROOT_DIR_KEY = os.getcwd()

# The Artifacts directory to store all the things 
ARTIFACT_DIR_KEY = "artifacts"

STUBS_FOLDER = "stubs"
STUB_FILE = "tracked_features.pkl"
# REPORTS = "reports"


MODEL_FOLDER = "models"
CURRENT_MODEL = "version_1.pt"


DATA_FOLDER = "data"
DATA_YAML_FILE = "data.yaml"


INPUT_FOLDER = "input"
VIDEO_FOLDER = "videos"
VIDEO_FILE = "type3N.MOV"

IMAGE_FOLDER = "images"
IMAGE_FILE = "image.png"