from api.routes.owner_routes import router as owner_router
from api.routes.space_routes import router as space_router
from api.routes.reservation_routes import router as reservation_router

routers = [
    owner_router,
    space_router,
    reservation_router,
]