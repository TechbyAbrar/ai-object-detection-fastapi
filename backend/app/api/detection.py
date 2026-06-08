from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Query,
    Depends
)

from app.core.detector import (
    Detector,
    get_detector
)

from app.services.detection_service import (
    DetectionService
)

from app.schemas.detection import (
    DetectionResponse
)

router = APIRouter()


@router.post(
    "/images/detect",
    response_model=DetectionResponse
)
async def detect_image(
    file: UploadFile = File(...),
    confidence: float = Query(
        0.25,
        ge=0.0,
        le=1.0
    ),
    detector: Detector = Depends(
        get_detector
    )
):

    service = DetectionService(detector)

    image_id, image_path = (
        await service.save_upload(file)
    )

    results = service.detect(
        str(image_path),
        confidence
    )

    detections, output_path = (
        service.annotate(
            image_id,
            str(image_path),
            results
        )
    )

    return {
        "image_id": image_id,
        "download_url":
            f"/api/v1/downloads/{output_path.name}",
        "detections": detections
    }
    
    
# download_api
from pathlib import Path

from fastapi.responses import FileResponse

from app.core.config import settings


@router.get(
    "/downloads/{filename}"
)
async def download_file(
    filename: str
):

    path = (
        Path(settings.output_dir)
        / filename
    )

    return FileResponse(path)