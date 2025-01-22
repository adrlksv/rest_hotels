from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO

from app.bookings.schemas import SBooking
from app.users.models import User
from app.users.dependencies import get_current_user
from app.exceptions import BookingDeleteError
from app.tasks.tasks import send_booking_confirmation_email

from datetime import date


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
async def get_bookings(user: User = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: User = Depends(get_current_user)
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if booking:
        booking_dict = {
            "id": booking.id,
            "room_id": booking.room_id,
            "user_id": booking.user_id,
            "date_from": booking.date_from.isoformat(),
            "date_to": booking.date_to.isoformat(),
            "price": booking.price
        }
        send_booking_confirmation_email.delay(booking_dict, user.email)

        return booking_dict
    
    else:
        return {
            "message": "None"
        }
    # if not booking:
    #     raise RoomCannotBeBooked


@router.delete("/{booking_id}")
async def delete_booking(
    booking_id: int,
    user: User = Depends(get_current_user)
):
    booking = await BookingDAO.delete(user.id, booking_id)
    if not booking:
        raise BookingDeleteError
