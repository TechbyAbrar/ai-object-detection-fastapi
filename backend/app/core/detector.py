from functools import lru_cache

from ultralytics import YOLO

from app.core.config import settings


class Detector:
    def __init__(self) -> None:
        self.model = YOLO(settings.model_path)

    def predict(self, image_path: str, confidence: float):
        return self.model.predict(
            source=image_path,
            conf=confidence,
            save=False,
            verbose=False
        )


@lru_cache
def get_detector() -> Detector:
    return Detector()

# @lru_cache
# loads YOLO once.
# Not per request.