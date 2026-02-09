from sqlalchemy.orm import Session

from models.match_model import Matches


class LeaderboardsRepository:

    def find_all(self, db: Session) -> list[Matches]:
        return (
            db.query(Matches)
            .filter(Matches.in_progress == False)
            .all()
        )
