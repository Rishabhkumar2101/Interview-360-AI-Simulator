from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Interview-360 AI Simulator",
    description="AI-powered mock interview and placement preparation platform",
    version="1.0.0"
)

# CORS configuration for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://127.0.0.1:8501"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to Interview-360 AI Simulator",
        "service": "FastAPI Backend"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Backend is running properly"
    }