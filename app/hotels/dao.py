from datetime import date
from sqlalchemy import select, func, and_, text
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms  # Импортируйте ваши модели Hotel и Rooms
from app.dao.base import BaseDAO
from app.database import async_session_maker

class HotelDAO(BaseDAO):
    model = Hotels

    # @classmethod
    # async def get_hotels_with_availability(cls, location: str, date_from: date, date_to: date):
    #     async with async_session_maker() as session:
    #         # Используем raw SQL для большей гибкости в подсчёте доступных номеров
    #         query = text("""
    #             SELECT 
    #                 h.id, h.name, h.location, h.services, h.rooms_quantity, h.image_id,
    #                 (h.rooms_quantity - COALESCE(COUNT(r.id),0)) as rooms_left
    #             FROM 
    #                 hotels h
    #             LEFT JOIN 
    #                 rooms r ON h.id = r.hotel_id
    #             WHERE 
    #                 h.location = :location
    #             GROUP BY 
    #                 h.id, h.name, h.location, h.services, h.rooms_quantity, h.image_id
    #             HAVING 
    #                 COUNT(r.id) < h.rooms_quantity;
    #         """)

    #         result = await session.execute(query, {"location": location})
    #         hotels_data = result.fetchall()
            
    #         hotels = [
    #             Hotels(
    #                 id=hotel.id,
    #                 name=hotel.name,
    #                 location=hotel.location,
    #                 services=hotel.services,
    #                 rooms_quantity=hotel.rooms_quantity,
    #                 image_id=hotel.image_id,
    #                 rooms_left=hotel.rooms_left,
    #             )
    #             for hotel in hotels_data
    #         ]

    #         return hotels


