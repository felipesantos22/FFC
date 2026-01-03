from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.team_repository import TeamRepository
from models.team_model import Team
from schemas.team_schema import TeamCreate


class TeamService:

    def __init__(self):
        self.repository = TeamRepository()

    def create_team(self, db: Session, team_create: TeamCreate) -> Team:
        team = Team(**team_create.model_dump())
        return self.repository.create(db, team)

    def list_teams(self, db: Session):
        return self.repository.find_all(db)

    def list_team_by_id(self, db: Session, team_id: int):
        return self.repository.find_by_id(db, team_id)

    def update_team(self, db: Session, item_id: int, name: str):
        item = self.repository.find_by_id(db, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repository.update(db, item, name)

    def delete_team(self, db: Session, item_id: int):
        item = self.repository.find_by_id(db, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repository.delete(db, item)
