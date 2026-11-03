from pydantic import BaseModel, field_validator, ValidationError
from typing import Literal

class DoctorModel(BaseModel):
    id: int
    name: str
    specialty: str
    gender: Literal['male', 'female']
    
    @field_validator('id')
    @classmethod
    def id_positive(cls, value: int) -> int:
        if value <= 0:
            raise ValueError(f'{value} is not a positive integer')
        return value

    @field_validator('name')
    @classmethod
    def name_not_empty(cls, value: str) -> str:
        if len(value) == 0:
            raise ValueError('Name is required')
        return value
    
    @field_validator('specialty')
    @classmethod
    def specialty_not_empty(cls, value: str) -> str:
        if len(value) == 0:
            raise ValueError('Specialty is required')
        return value
    
    @field_validator('gender', mode='before')    
    @classmethod
    def gender_not_empty(cls, value: Literal['male', 'female']) -> Literal['male', 'female']:
        value = value.lower()
        
        if len(value) == 0:
            raise ValueError('Gender is required')
        elif value not in ['male', 'female']:
            raise ValueError('Invalid gender')
        return value
    
try: 
    doctor = DoctorModel(
        id=1, 
        name='John Doe', 
        specialty='Family Medicine', 
        gender='male'
    )
        
    print(doctor)

except ValidationError as err:
    print(err)