from sqlalchemy.orm import Session
from models.team_model import Team

class TeamRepository:

    def create(self, db: Session, team: Team):
        db.add(team)
        db.commit()
        db.refresh(team)
        return team

    def find_all(self, db: Session):
        return db.query(Team).all()

    def find_by_id(self, db: Session, team_id: int):
        return db.query(Team).filter(Team.id == team_id).first()

    def update(self, db: Session, team: Team, team_name: str):
        team.name = team_name
        db.commit()
        db.refresh(team)
        return team

    def delete(self, db: Session, team: Team):
        db.delete(team)
        db.commit()
        return None
