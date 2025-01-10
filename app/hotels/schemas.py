from typing import Optional
from pydantic import BaseModel


class SHotelBase(BaseModel):
    id: int
    name: str
    location: str
    services: list[str] 
    rooms_quantity: int
    image_id: Optional[int] = None
    
    class Config:
        orm_mode = True
