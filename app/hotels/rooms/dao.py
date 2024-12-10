from sqlalchemy import select

from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.database import async_session_maker


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_rooms_by_hotel_id(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
    