from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.match_model import Matches

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    team_name = Column(String(30), nullable=False, unique=True)

    home_matches = relationship(
        "Matches",
        foreign_keys=[Matches.home_team_id],
        back_populates="home_team"
    )

    away_matches = relationship(
        "Matches",
        foreign_keys=[Matches.away_team_id],
        back_populates="away_team"
    )
