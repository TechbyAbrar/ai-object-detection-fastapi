# 🚀 AI Object Detection FastAPI Backend

A high-performance backend API built with **FastAPI** for real-time object detection using deep learning models (e.g., YOLO). The system is optimized for low latency inference and containerized using Docker for easy deployment.

---

## 📌 Features

* ⚡ FastAPI-based high-performance REST API
* 🧠 AI object detection (Ultralytics / YOLO support)
* 🖼️ Image upload & processing via multipart form data
* 📦 Docker-ready deployment
* 🔥 Lightweight and CPU-optimized (no GPU required)
* 🧪 Test-ready structure (pytest compatible)
* 📊 Modular and scalable architecture


## 🚀 API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "status": "ok",
  "message": "AI Object Detection API is running"
}
```

---

### Object Detection

```http
POST /predict
```

#### Request

* Content-Type: `multipart/form-data`
* Field: `file` (image)

#### Example (cURL)

```bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@image.jpg"
```

#### Response

```json
{
  "success": true,
  "predictions": [
    {
      "class": "person",
      "confidence": 0.92,
      "bbox": [120, 80, 300, 400]
    }
  ]
}
```

---

## 🐳 Docker Setup

### 1. Build Docker Image

```bash
docker build -t ai-object-detection-backend .
```

### 2. Run Container

```bash
docker run -p 8000:8000 ai-object-detection-backend
```

---

## ⚙️ Local Setup (Without Docker)

### 1. Create Virtual Environment

```bash
python -m venv env
source env/Scripts/activate   # Windows Git Bash
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🧠 Tech Stack

* FastAPI
* Python 3.13
* Ultralytics (YOLO)
* OpenCV
* Pillow
* NumPy
* Docker

---

## 📦 Requirements

* Python 3.10+
* pip
* Docker (optional but recommended)

---

## 🔥 Performance Notes

* CPU-optimized inference
* Lightweight dependencies (`opencv-python-headless`)
* Stateless API design for scalability
* Ready for cloud deployment (AWS / Render / VPS)

---

## 📌 Future Improvements

* [ ] Add authentication (JWT)
* [ ] Add Redis caching for inference results
* [ ] Batch image processing endpoint
* [ ] WebSocket real-time detection
* [ ] GPU acceleration support

---

## 👨‍💻 Author

**Md. Abrar Fahim**
GitHub: https://github.com/TechbyAbrar
LinkedIn: https://www.linkedin.com/in/techbyabrar/
Portfolio: https://techbyabrar.netlify.app/

---

## 📄 License

This project is private and available under the MIT License.
