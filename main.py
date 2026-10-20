
from contextlib import asynccontextmanager

from fastapi import FastAPI

from webapp.database import Base, engine
from webapp.routers.items import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


app = FastAPI(
    title="Items API",
    lifespan=lifespan,
)

app.include_router(items_router)
