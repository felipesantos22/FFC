from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Matches(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)

    home_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    away_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    home_team_goals = Column(Integer, nullable=False)
    away_team_goals = Column(Integer, nullable=False)

    in_progress = Column(Boolean, default=True)

    home_team = relationship(
        "Team",
        foreign_keys=[home_team_id],
        back_populates="home_matches"
    )

    away_team = relationship(
        "Team",
        foreign_keys=[away_team_id],
        back_populates="away_matches"
    )
