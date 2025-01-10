from fastapi import APIRouter

from app.hotels.dao import HotelDAO


router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)

@router.get('/all')
async def get_hotels():
    return await HotelDAO.find_all()

# @router.get('/{Hotels.name}')
# async def get_hotel(name):
#     return await HotelDAO.find
