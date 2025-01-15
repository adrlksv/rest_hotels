from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels

from app.pages.router import router as page_router
from app.images.router import router as image_router

app = FastAPI()

app.mount('/static', StaticFiles(directory="app/static"), "static")

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)

app.include_router(page_router)
app.include_router(image_router)
