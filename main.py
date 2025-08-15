from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI(title="Simple Deploy API", version="1.0.0")


@app.get("/")
async def root():
    return {
        "message": "Welcome to Simple Deploy API",
        "version": "1.0.0",
        "environment": "production",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
async def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "simple-deploy",
            "timestamp": datetime.now().isoformat()
        }
    )


@app.get("/info")
async def get_info():
    return {
        "name": "Simple Deploy API",
        "description": "A simple FastAPI application deployed with Docker and Traefik",
        "features": [
            "FastAPI framework",
            "Docker containerization",
            "Traefik reverse proxy",
            "HTTPS with Let's Encrypt",
            "Health check endpoint"
        ],
        "endpoints": {
            "/": "Root endpoint",
            "/health": "Health check",
            "/info": "API information",
            "/docs": "Interactive API documentation",
            "/redoc": "Alternative API documentation"
        }
    }