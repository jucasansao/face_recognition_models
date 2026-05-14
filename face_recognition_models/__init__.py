from importlib.resources import files

__author__ = "Adam Geitgey"
__email__ = "ageitgey@gmail.com"
__version__ = "0.3.0"

_models = files(__name__) / "models"


def pose_predictor_model_location() -> str:
    return str(_models / "shape_predictor_68_face_landmarks.dat")


def pose_predictor_five_point_model_location() -> str:
    return str(_models / "shape_predictor_5_face_landmarks.dat")


def face_recognition_model_location() -> str:
    return str(_models / "dlib_face_recognition_resnet_model_v1.dat")


def cnn_face_detector_model_location() -> str:
    return str(_models / "mmod_human_face_detector.dat")
