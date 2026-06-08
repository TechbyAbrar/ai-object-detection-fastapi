from pathlib import Path

from fastapi import FastAPI

from app.api.detection import router

from app.core.config import settings


Path(
    settings.upload_dir
).mkdir(
    parents=True,
    exist_ok=True
)

Path(
    settings.output_dir
).mkdir(
    parents=True,
    exist_ok=True
)

app = FastAPI(
    title="YOLO Detection API",
    version="1.0.0"
)

app.include_router(
    router,
    prefix=settings.api_prefix
)


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }