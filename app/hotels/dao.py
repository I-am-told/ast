from app.dao.base import BaseDAO
from app.hotels.models import Hotels


class HotelDAO(BaseDAO):
    model = Hotels
    
    @classmethod
    async def find_all(cls, **filter_by):
        return await super().find_all(**filter_by)