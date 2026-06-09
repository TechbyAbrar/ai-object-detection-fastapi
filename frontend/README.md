# 🚀 YOLO Object Detection Frontend

A modern, responsive React (Vite) frontend for real-time AI object detection powered by YOLOv8 + FastAPI backend.

Upload an image → run detection → visualize results instantly.

---

# ✨ Features

- 🔥 Upload images for object detection
- 🎯 Adjustable confidence threshold (0.0 - 1.0)
- 🖼️ View original and detected images
- 📊 Detection results table (label, confidence, bounding box)
- ⚡ Fast Vite + React performance
- 📱 Fully responsive design (mobile, tablet, desktop)
- ⏳ Loading state during inference
- 🔗 Seamless FastAPI backend integration

---

# 🧠 Tech Stack

- React (Vite)
- JavaScript (ES6+)
- CSS (Responsive UI with Flexbox & Grid)
- Fetch API
- YOLOv8 (Backend)
- FastAPI (Backend)

---

# ⚙️ Setup Instructions

## 1. Install dependencies

cd frontend
npm install

---

## 2. Create environment file

Create a `.env` file in the frontend root:

VITE_API_BASE_URL=http://localhost:8000

---

## 3. Run the project

npm run dev

Open in browser:
http://localhost:5173

---

# 🔗 Backend Requirement

Make sure backend is running before using frontend:

uvicorn app.main:app --reload

Backend URL:
http://localhost:8000

---

# 🔌 API Endpoints Used

POST /api/v1/images/detect
- Upload image and get detection results

GET /api/v1/downloads/{filename}
- Get annotated output image

GET /health
- Backend health check

---

# 🧪 How It Works

1. Upload image from UI
2. Frontend sends image to FastAPI backend
3. YOLOv8 model processes the image
4. Backend returns:
   - detected objects
   - confidence scores
   - bounding boxes
   - annotated image URL
5. Frontend displays:
   - original image
   - detection result image
   - detection table

---

# 🏗️ Build for Production

npm run build

Output folder:
dist/

---

# ⚠️ Important Notes

- Backend must be running before frontend
- Enable CORS in FastAPI if API calls fail
- Default backend URL: http://localhost:8000

---

# 👨‍💻 Author
**Md. Abrar Fahim**
GitHub: https://github.com/TechbyAbrar
LinkedIn: https://www.linkedin.com/in/techbyabrar/
Portfolio: https://techbyabrar.netlify.app/

Built with React + FastAPI + YOLOv8

A full-stack AI object detection project focused on speed, simplicity, and real-world usability.