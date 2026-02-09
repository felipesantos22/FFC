import uvicorn
from fastapi import FastAPI

from database import Base, engine

from controllers.team_controller import router as item_router
from controllers.user_controller import router as user_router
from controllers.login_controller import router as login_router
from controllers.match_controller import router as match_router
from controllers.leaderboards_controller import router as leaderboards_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project FFC With FastAPI")

app.include_router(item_router)
app.include_router(user_router)
app.include_router(login_router)
app.include_router(match_router)
app.include_router(leaderboards_controller)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
