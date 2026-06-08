from pydantic import BaseModel


class Detection(BaseModel):
    label: str
    confidence: float
    bbox: list[int]


class DetectionResponse(BaseModel):
    image_id: str
    download_url: str
    detections: list[Detection]