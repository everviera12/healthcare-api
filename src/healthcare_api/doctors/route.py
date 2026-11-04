from typing import Optional, Literal
from pydantic import BaseModel
from fastapi import status, APIRouter
from healthcare_api.doctors.model import DoctorModel

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None
    gender: Optional[Literal['male', 'female']] = None

router = APIRouter(
    prefix="/doctors", 
    tags=["Doctors"]
)

doctors = [
  { "id": 1, "name": "Dr. Gregory House", "specialty": "Diagnostics", "gender": "male" },
  { "id": 2, "name": "Dra. Meredith Grey", "specialty": "General Surgery", "gender": "female" },
  { "id": 3, "name": "Dr. John Dorian", "specialty": "Internal Medicine", "gender": "male" },
]

@router.get("/", status_code=status.HTTP_200_OK)
def get_doctors():
    return doctors

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_doctor_by_id(id: int):
    for doctor in doctors:
        if doctor["id"] == id:
            return {
                "message": "Doctor founded successfully",
                "doctor": doctor
            }
    
    return {
        "status_code": status.HTTP_404_NOT_FOUND,
        "message": "Doctor not found",
        "doctor": None
    }
    
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: DoctorModel):
    doctors.append(doctor)

    return {
        "message": "Doctor created successfully",
        "doctor": doctor        
    }

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_doctor(id: int):
    for doctor in doctors:
        if doctor["id"] == id:
            doctors.remove(doctor)
            return {
                "message": "Doctor deleted successfully",
                "doctor": doctor
            }
    
    return {
        "status_code": status.HTTP_404_NOT_FOUND,
        "message": "Doctor not found",
        "doctor": None
    }

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_doctor(id: int, doctor: DoctorModel):
    for index, existing_doctor in enumerate(doctors):
        if existing_doctor["id"] == id:
            updated_doctor = {
                "id": id, 
                **doctor.model_dump()
            }

            doctors[index] = updated_doctor
            
            return {
                "message": "Doctor updated successfully",
                "doctor": updated_doctor
            }
    
    return {
        "status_code": status.HTTP_404_NOT_FOUND,
        "message": "Doctor not found",
        "doctor": None
    }

@router.patch("/{id}", status_code=status.HTTP_200_OK)
def patch_doctor(id: int, doctor_update: DoctorUpdate):
    for index, existing_doctor in enumerate(doctors):
        if existing_doctor["id"] == id:
            update_data = doctor_update.model_dump(exclude_unset=True)
            doctors[index].update(update_data)
            
            return {
                "message": "Doctor partially updated successfully",
                "doctor": doctors[index]
            }
    
    return {
        "status_code": status.HTTP_404_NOT_FOUND,
        "message": "Doctor not found",
        "doctor": None
    }