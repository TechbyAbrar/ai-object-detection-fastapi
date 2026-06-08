import uuid

from pathlib import Path

import cv2
import aiofiles

from fastapi import UploadFile

from app.core.config import settings
from app.core.detector import Detector
from app.schemas.detection import Detection


class DetectionService:

    def __init__(self, detector: Detector):
        self.detector = detector

    async def save_upload(
        self,
        file: UploadFile
    ) -> tuple[str, Path]:

        image_id = uuid.uuid4().hex

        suffix = Path(file.filename).suffix

        path = (
            Path(settings.upload_dir)
            / f"{image_id}{suffix}"
        )

        async with aiofiles.open(path, "wb") as buffer:
            content = await file.read()
            await buffer.write(content)

        return image_id, path

    def detect(
        self,
        image_path: str,
        confidence: float
    ):

        return self.detector.predict(
            image_path=image_path,
            confidence=confidence
        )

    def annotate(
        self,
        image_id: str,
        image_path: str,
        results
    ):

        image = cv2.imread(image_path)

        detections = []

        result = results[0]

        for box in result.boxes:

            x1, y1, x2, y2 = (
                box.xyxy[0]
                .cpu()
                .numpy()
                .astype(int)
            )

            cls = int(box.cls[0])

            conf = float(box.conf[0])

            label = result.names[cls]

            detections.append(
                Detection(
                    label=label,
                    confidence=round(conf, 4),
                    bbox=[x1, y1, x2, y2]
                )
            )

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                f"{label} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

        output_path = (
            Path(settings.output_dir)
            / f"{image_id}.jpg"
        )

        cv2.imwrite(
            str(output_path),
            image
        )

        return detections, output_path