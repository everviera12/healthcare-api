from fastapi import FastAPI
from healthcare_api.doctors.route import router as doctors_router

app = FastAPI(
    title="Healthcare API",
    version="1.0.0",
    description="System for managing healthcare data."
)

app.include_router(doctors_router)

@app.get("/")
def root():
    return {
        "message": "Server is running. See /docs for API documentation."
    }