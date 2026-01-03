from fastapi import FastAPI
from database import Base, engine
from controllers.team_controller import router as item_router
from controllers.user_controller import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="CRUD With FastAPI")
app.include_router(item_router)
app.include_router(user_router)
