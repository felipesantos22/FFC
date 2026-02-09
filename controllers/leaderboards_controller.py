from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from repositories.leaderboards_repositoty import LeaderboardsRepository
from services.leaderboard_service import LeaderboardService

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_leaderboard(db: Session = Depends(get_db)):
    repository = LeaderboardsRepository()
    service = LeaderboardService(repository)

    result = service.generate(db)

    return result
