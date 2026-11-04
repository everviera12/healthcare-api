from fastapi import FastAPI, APIRouter

router = APIRouter(
    prefix="/doctors", 
    tags=["Doctors"]
)

doctors = [
  { "id": 1, "name": "Dr. Gregory House", "specialty": "Diagnostics", "gender": "male" },
  { "id": 2, "name": "Dra. Meredith Grey", "specialty": "General Surgery", "gender": "female" },
  { "id": 3, "name": "Dr. John Dorian", "specialty": "Internal Medicine", "gender": "male" }
]

@router.get("/")
def get_doctors():
    return doctors