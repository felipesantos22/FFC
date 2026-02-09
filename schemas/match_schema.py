from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from schemas.team_schema import TeamMatchResponse


class MatchCreate(BaseModel):
    home_team_id: int
    away_team_id: int
    home_team_goals: int
    away_team_goals: int
    in_progress: bool = True


class MatchResponse(BaseModel):
    id: int
    home_team_id: int
    away_team_id: int
    home_team_goals: int
    away_team_goals: int
    in_progress: bool
    homeTeam: TeamMatchResponse = Field(alias="home_team")
    awayTeam: TeamMatchResponse = Field(alias="away_team")

    class Config:
        model_config = ConfigDict(from_attributes=True)


class MatchUpdateInProgress(BaseModel):
    in_progress: bool


class MessageResponse(BaseModel):
    message: str


class MatchUpdateResult(BaseModel):
    home_team_goals: int
    away_team_goals: int


class MatchUpdate(BaseModel):
    in_progress: Optional[bool] = None
    home_team_goals: Optional[int] = None
    away_team_goals: Optional[int] = None
