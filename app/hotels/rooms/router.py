from app.hotels.router import router
from app.hotels.rooms.dao import RoomDAO


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id):
        return await RoomDAO.get_rooms_by_hotel_id(hotel_id=hotel_id)