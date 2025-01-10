from typing import List
from fastapi import APIRouter, Depends, HTTPException
from datetime import date # Импортируем date из datetime
from app.hotels.schemas import SHotelBase
from app.hotels.dao import HotelDAO

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)

@router.get('', response_model=List[SHotelBase])
async def get_all_hotels() -> List[SHotelBase]:
    hotels = await HotelDAO.find_all()
    if not hotels:
        raise HTTPException(status_code=404, detail="Отели не найдены")
    return hotels

@router.get('/{hotel_id}', response_model=SHotelBase)
async def get_one_hotel(hotel_id: int) -> SHotelBase:
    hotel = await HotelDAO.find_by_id(hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Отель не найден")
    return hotel

# @router.get('')
# async def get_all_hotels() -> list[SHotelBase]:
#     return await HotelDAO.find_all()


# @router.get("/{location}", response_model=HotelList)
# async def get_hotels_by_location(location: str, date_from: date = None, date_to: date = None): # Изменено на date
#     hotels = await HotelDAO.get_hotels_with_availability(location, date_from, date_to)
#     if not hotels:
#         raise HTTPException(status_code=404, detail="Отели не найдены")
#     return {"hotels": hotels}

