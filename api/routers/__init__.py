from api.routers.owner_router import router as owner_router
from api.routers.space_router import router as space_router
from api.routers.reservation_router import router as reservation_router

routers = [
    owner_router,
    space_router,
    reservation_router,
]