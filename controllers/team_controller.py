from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.team_schema import TeamCreate, TeamResponse, TeamUpdate, TeamDelete
from services.team_service import TeamService

router = APIRouter(prefix="/teams", tags=["Teams"])
service = TeamService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TeamResponse)
def create_item(team: TeamCreate, db: Session = Depends(get_db)):
    return service.create_team(db, team)


@router.get("/", response_model=list[TeamResponse])
def list_items(db: Session = Depends(get_db)):
    return service.list_teams(db)


@router.get("/{team_id}", response_model=TeamResponse)
def list_team_id(team_id: int, db: Session = Depends(get_db)):
    return service.list_team_by_id(db, team_id)


@router.put("/{team_id}")
def update_team(team_id: int, item: TeamUpdate, db: Session = Depends(get_db)):
    updated = service.update_team(db, team_id, item.team_name)
    if not updated:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated


@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_team(db, team_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team removed"}
