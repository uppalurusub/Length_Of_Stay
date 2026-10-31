from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.los_router import (
    router as los_router
)

# ==================================================
# APP
# ==================================================

app = FastAPI(
    title="Hospital Length Of Stay",
    description="""
    Hospital Length of Stay Prediction API
    """,
    version="1.0.0"
)

# ==================================================
# CORS
# ==================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ==================================================
# ROOT
# ==================================================

@app.get("/")
async def root():

    return {
        "application":
            "Clinical Decision Support System",

        "version":
            "1.0.0",

        "status":
            "Running"
    }

# ==================================================
# HEALTH
# ==================================================

@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }

# ==================================================
# ROUTERS
# ==================================================

app.include_router(
    los_router
)