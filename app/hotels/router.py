from fastapi import APIRouter, Depends

from app.hotels.dao import HotelDAO
from app.exceptions import HotelNotFound


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
    )


@router.get("{location}")
async def get_hotels_by_location(location: str):
    hotels = await HotelDAO.find_by_location(location=location)
    if not hotels:
        raise HotelNotFound
    return hotels




@router.get("")
async def get_hotels():
    return await HotelDAO.find_all()

