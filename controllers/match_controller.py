from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.match_schema import MatchCreate, MatchResponse, MatchUpdateInProgress, MessageResponse, MatchUpdateResult, \
    MatchUpdate
from services.match_service import MatchService
from services.login_service import LoginService

router = APIRouter(prefix="/matches", tags=["Matches"])

service = MatchService()
service_login = LoginService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MatchCreate)
def create_match(match: MatchCreate,
                 _: str = Depends(service_login.verify_token),
                 db: Session = Depends(get_db)):
    match = service.match_create(db, match)
    return match


@router.get("/", response_model=list[MatchResponse])
def list_match(db: Session = Depends(get_db)):
    match = service.find_all(db)
    return match


@router.get("/progress", response_model=list[MatchResponse])
def list_match(in_progress: Optional[bool] = None, db: Session = Depends(get_db)):
    if in_progress is None:
        return service.find_all(db)
    match = service.find_in_progress(db, in_progress)
    return match


@router.patch("/{match_id}/finished", response_model=MessageResponse)
def patch_match(match_id: int,
                match: MatchUpdateInProgress,
                _: str = Depends(service_login.verify_token),
                db: Session = Depends(get_db)):
    patch = service.patch_in_progress(db, match_id, match.in_progress)

    if not patch:
        raise HTTPException(status_code=404, detail="Match not found")

    return {"message": "Finished"}


@router.patch("/{match_id}/result", response_model=MatchUpdateResult)
def patch_result(
        match_id: int,
        match: MatchUpdateResult,
        _: str = Depends(service_login.verify_token),
        db: Session = Depends(get_db)):
    patch = service.patch_result(db, match_id, match.home_team_goals, match.away_team_goals)

    if not patch:
        raise HTTPException(status_code=404, detail="Match not found")
    return patch


@router.patch("/{match_id}/all", response_model=MatchResponse)
def update_match(
        match_id: int,
        match: MatchUpdate,
        _: str = Depends(service_login.verify_token),
        db: Session = Depends(get_db)
):
    updated = service.patch_all(db, match_id, match)

    if not updated:
        raise HTTPException(status_code=404, detail="Match not found")

    return updated
