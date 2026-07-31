import datetime


class Match:
    def __init__(self, home : str, away : str, home_odds : float, away_odds : float, draw_odds : float, date : str):
        self.home = home
        self.away = away
        self.home_odds = home_odds
        self.away_odds = away_odds
        self.draw_odds = draw_odds
        self.date = date

    def get_dict(self):
        match_ = {
            "home" : self.home,
            "away" : self.away,
            "homeOdds" : self.home_odds,
            "drawOdds" : self.draw_odds,
            "awayOdds" : self.away_odds,
            "date" : self.date
        }
        return match_

    def __str__(self):
        return f"{self.home} - {self.away} odds: {self.home_odds} {self.draw_odds} {self.away_odds} Date: {self.date}"