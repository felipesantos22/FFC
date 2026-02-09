from sqlalchemy.orm import Session
from repositories.leaderboards_repositoty import LeaderboardsRepository

class LeaderboardService:

    def __init__(self, repository: LeaderboardsRepository):
        self.repository = repository

    def generate(self, db: Session):
        matches = self.repository.find_all(db)

        table = {}

        for match in matches:
            home = match.home_team.team_name
            away = match.away_team.team_name

            # cria time se não existir
            if home not in table:
                table[home] = self._create_team(home)

            if away not in table:
                table[away] = self._create_team(away)

            # jogos
            table[home]["totalGames"] += 1
            table[away]["totalGames"] += 1

            # gols
            table[home]["goalsFavor"] += match.home_team_goals
            table[home]["goalsOwn"] += match.away_team_goals

            table[away]["goalsFavor"] += match.away_team_goals
            table[away]["goalsOwn"] += match.home_team_goals

            # resultado
            if match.home_team_goals > match.away_team_goals:
                table[home]["totalVictories"] += 1
                table[home]["totalPoints"] += 3
                table[away]["totalLosses"] += 1

            elif match.home_team_goals < match.away_team_goals:
                table[away]["totalVictories"] += 1
                table[away]["totalPoints"] += 3
                table[home]["totalLosses"] += 1

            else:
                table[home]["totalDraws"] += 1
                table[away]["totalDraws"] += 1
                table[home]["totalPoints"] += 1
                table[away]["totalPoints"] += 1

        return list(table.values())

    def _create_team(self, name):
        return {
            "name": name,
            "totalPoints": 0,
            "totalGames": 0,
            "totalVictories": 0,
            "totalDraws": 0,
            "totalLosses": 0,
            "goalsFavor": 0,
            "goalsOwn": 0,
        }
