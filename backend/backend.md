backend/
│
├── app/
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── detection.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── detector.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── detection.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── detection_service.py
│   │
│   ├── storage/
│   │   ├── uploads/
│   │   └── outputs/
│   │
│   └── main.py
│
├── models/
│   └── yolov8n.pt
│
├── tests/
│   └── test_health.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
├── README.md
└── docker-compose.yml