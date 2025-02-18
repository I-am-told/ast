from fastapi import FastAPI

from app.users.router import router as router_users
from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)


# class SHotel(BaseModel):
#     adress: str
#     name: str
#     stars: int
    
    
# class HotelSearchArgs:
#     def __init__(
#         self,
#         hotel_id: int,
#         date_from: date,
#         date_to: date,
#         has_spa: Optional[bool] = None,
#         stars: Optional[int] = Query(None, ge=1, le=5),
#     ):
#         self.hotel_id = hotel_id
#         self.date_from = date_from
#         self.date_to = date_to
#         self.has_spa = has_spa
#         self.stars = stars
        
    

# @app.get('/hotels')
# def get_hotels(
#     search_args: HotelSearchArgs = Depends()
# ) -> list[SHotel]:
#     hotels = [
#         {
#             'adress': 'ул. Гагарина, 1, Алтай',
#             'name': 'Super Puper',
#             'stars': 5,
#         }
#     ]
#     return hotels

