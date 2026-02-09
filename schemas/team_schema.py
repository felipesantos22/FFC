from pydantic import BaseModel, ConfigDict


class TeamCreate(BaseModel):
    team_name: str


class TeamResponse(BaseModel):
    id: int
    team_name: str

    class Config:
        model_config = ConfigDict(from_attributes=True)


class TeamMatchResponse(BaseModel):
    team_name: str

    class Config:
        model_config = ConfigDict(from_attributes=True)


class TeamUpdate(BaseModel):
    team_name: str


class TeamDelete(BaseModel):
    team_name: str
