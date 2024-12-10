from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from app.database import Base


class Rooms(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
    