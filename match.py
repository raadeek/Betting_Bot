import datetime


class Match:
    def __init__(self, home : str, away : str, home_odds : float, away_odds : float, draw_odds : float, date):
        self.home = home
        self.away = away
        self.home_odds = home_odds
        self.away_odds = away_odds
        self.draw_odds = draw_odds
        self.date = date
        