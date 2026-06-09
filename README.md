# 🚀 AI Object Detection System (YOLOv8 + FastAPI + React)

A full-stack AI-powered object detection platform built using **YOLOv8**, **FastAPI**, and **React (Vite)**.

Upload an image → run AI inference → get real-time object detection results with bounding boxes and confidence scores.

---

# 🌟 Overview

This project is a production-style full-stack AI system designed for real-world computer vision deployment.

It consists of:

- ⚙️ Backend: FastAPI + YOLOv8 inference engine
- 🎨 Frontend: React (Vite) interactive UI
- 🧠 AI Model: Ultralytics YOLOv8
- 📦 Storage: Local file system for uploads and outputs

The system is built with a **clean separation of backend and frontend services**, communicating via REST APIs.

---

# ✨ Features

## 🧠 AI Backend Features
- 🎯 YOLOv8 object detection engine
- 📊 Confidence-based filtering
- 🖼️ Bounding box annotation on images
- 📁 Image upload handling
- 📥 Download processed images
- ⚡ Fast API-based inference system

---

## 🎨 Frontend Features
- 📤 Image upload interface
- 🎚️ Confidence threshold control
- 🖼️ Original vs detected image preview
- 📊 Detection results table (label, confidence, bounding box)
- ⚡ Fast Vite-powered UI
- 📱 Fully responsive design (mobile, tablet, desktop)
- ⏳ Loading states during inference

---

# 🏗️ Project Structure
Please, follow the both frontend and backend project folder, there are integrated the structure.


---

# 📡 API Endpoints (Backend)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/images/detect` | Run object detection on uploaded image |
| GET | `/api/v1/downloads/{filename}` | Get annotated output image |
| GET | `/health` | Backend health check |

---

# 🚀 How to Run This Project

This project is fully modular.

👉 Please refer to each module for setup instructions:

- 📄 `backend/README.md` → Backend setup, API details, YOLO configuration
- 📄 `frontend/README.md` → Frontend setup, UI usage, environment setup

---

# 🔗 Communication Flow

- Frontend sends image to backend API
- Backend processes image using YOLOv8
- Backend returns:
  - Detected objects
  - Confidence scores
  - Bounding boxes
  - Annotated image URL
- Frontend renders results visually

---

# 🧠 Design Philosophy

This project follows a clean **microservice-style architecture**:

- Backend is fully independent (AI inference only)
- Frontend is fully independent (UI only)
- Communication happens only through REST APIs

This ensures:
- Scalability
- Maintainability
- Easy future upgrades

---

# 🔮 Future Improvements Roadmap

This project is designed to evolve into a **full AI SaaS platform**.

---

## 🔐 Authentication System
- User registration & login
- JWT authentication
- Protected routes & API access control

---

## 🎥 Video Inference Support
- Video upload processing
- Frame-by-frame detection
- Real-time video analysis

---

## 📥 Export System
- Download annotated images
- Export detection results (JSON / CSV)
- Batch processing support

---

## 🌐 Frontend Upgrade (Next.js Migration)
- Move React (Vite) → Next.js
- SSR (Server-Side Rendering)
- SEO optimization
- Improved routing system

---

## ⚡ Backend Optimization
- Migration to **uv** package manager
- Faster dependency resolution
- Lightweight production builds

---

## ☁️ Deployment Strategy
- Docker containerization
- Backend deployment (Render / AWS / Fly.io)
- Frontend deployment (Vercel / Netlify)
- CI/CD pipeline integration

---

## 🧠 AI Enhancements
- Multi-model support (YOLOv8, YOLOv9, custom models)
- Object tracking system
- Real-time webcam detection
- Heatmap visualization

---

## 📊 Analytics Module
- Detection history tracking
- Usage analytics dashboard
- Performance monitoring

---

# ⚠️ Important Notes

- Backend and frontend must run simultaneously
- Ensure backend is running before using frontend
- Enable CORS in FastAPI for frontend communication
- Default backend URL: `http://localhost:8000`

---

# 👨‍💻 Author

Built with ❤️ using:

**FastAPI + YOLOv8 + React**

A scalable foundation for modern AI-powered applications, designed to grow into a production-grade AI SaaS platform.