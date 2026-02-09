from sqlalchemy.orm import Session, joinedload
from models.match_model import Matches
from models.team_model import Team
from schemas.match_schema import MatchCreate, MatchUpdate


class MatchesRepository:

    def create(self, db: Session, data: MatchCreate) -> Matches:
        match = Matches(**data.model_dump())
        db.add(match)
        db.commit()
        db.refresh(match)
        return match

    def find_by_id_team(self, db: Session, home_team_id: int, away_team_id: int) -> list[Team]:
        teams = (db.query(Team).filter(Team.id.in_([home_team_id, away_team_id])).all())
        return teams

    def find_all(self, db: Session):
        return (
            db.query(Matches)
            .options(
                joinedload(Matches.home_team),
                joinedload(Matches.away_team)
            )
            .all()
        )

    def find_in_progress(self, db: Session, in_progress: bool):
        return (
            db.query(Matches)
            .filter(Matches.in_progress == in_progress)
            .all()
        )

    def find_by_id(self, db: Session, match_id: int):
        return db.query(Matches).filter(Matches.id == match_id).first()

    def patch_in_progress(self, db: Session, match_id: int, in_progress: bool) -> Matches:
        match = db.query(Matches).filter(Matches.id == match_id).first()
        if not match:
            return None
        match.in_progress = in_progress
        db.commit()
        db.refresh(match)
        return match

    def patch_result(self, db: Session, match_id: int, home_team_goals: int, away_team_goals: int) -> Matches:
        match = db.query(Matches).filter(Matches.id == match_id).first()
        if not match:
            return None
        match.home_team_goals = home_team_goals
        match.away_team_goals = away_team_goals
        db.commit()
        db.refresh(match)
        return match

    def patch_match_all(db: Session, match_id: int, match: MatchUpdate):
        db_match = db.query(Matches).filter(Matches.id == match_id).first()

        if not db_match:
            return None

        data = match.dict(exclude_unset=True)

        for field, value in data.items():
            setattr(db_match, field, value)

        db.commit()
        db.refresh(db_match)
        return db_match
