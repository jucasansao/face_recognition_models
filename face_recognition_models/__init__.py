from importlib.resources import files
from pathlib import Path

__author__ = "Adam Geitgey"
__email__ = "ageitgey@gmail.com"
__version__ = "0.0.1"

_models = files(__name__) / "models"


def _require(path: str) -> str:
    """Return path, raising a clear error if the model file is missing."""
    p = Path(path)
    if not p.is_file():
        raise RuntimeError(
            f"Model file not found: {p}\n\n"
            "This stub release of face-recognition-models-ng does not include "
            "the model files yet — a PyPI size limit increase is pending.\n"
            "In the meantime, install from GitHub:\n\n"
            "    pip install git+https://github.com/jucasansao/face_recognition_models.git\n"
        )
    return path


def pose_predictor_model_location() -> str:
    return _require(str(_models / "shape_predictor_68_face_landmarks.dat"))


def pose_predictor_five_point_model_location() -> str:
    return _require(str(_models / "shape_predictor_5_face_landmarks.dat"))


def face_recognition_model_location() -> str:
    return _require(str(_models / "dlib_face_recognition_resnet_model_v1.dat"))


def cnn_face_detector_model_location() -> str:
    return _require(str(_models / "mmod_human_face_detector.dat"))
