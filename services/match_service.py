from fastapi import HTTPException, status
from repositories.match_repository import MatchesRepository
from sqlalchemy.orm import Session
from schemas.match_schema import MatchCreate, MatchUpdate
from models.match_model import Matches


class MatchService:

    def __init__(self):
        self.repository = MatchesRepository()

    def match_create(self, db: Session, match_create: MatchCreate) -> Matches:

        if match_create.home_team_id == match_create.away_team_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="It is not possible to create a match with two equal teams"
            )

        teams = self.repository.find_by_id_team(
            db,
            match_create.home_team_id,
            match_create.away_team_id
        )

        if len(teams) != 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There is no team with such id!"
            )

        return self.repository.create(db, match_create)

    def find_all(self, db: Session):
        return self.repository.find_all(db)

    def find_in_progress(self, db: Session, in_progress: bool):
        return self.repository.find_in_progress(db, in_progress)

    def find_by_id(self, db: Session, match_id: int) -> Matches:
        return self.repository.find_by_id(db, match_id)

    def patch_in_progress(self, db: Session, match_id: int, in_progress: bool) -> Matches:
        match = self.repository.patch_in_progress(db, match_id, in_progress)
        if not match:
            raise HTTPException(status_code=404, detail="Match not found")
        return match

    def patch_result(self, db: Session, match_id: int, home_team_goals: int, away_team_goals: int) -> Matches:
        match = self.repository.patch_result(db, match_id, home_team_goals, away_team_goals)
        if not match:
            raise HTTPException(status_code=404, detail="Match not found")
        return match

    def patch_all(self, db: Session, patch: MatchUpdate) -> Matches:
        match = self.repository.patch_match_all(db, patch)
        if not match:
            raise HTTPException(status_code=404, detail="Match not found")
        return match
