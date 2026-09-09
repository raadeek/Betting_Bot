from datetime import datetime

class BetEvent:
    '''
        Every single event player bets is stored as a BetEvent. Each Bet consist of multiple BetEvents.
        betted - -1 if betted away_team, 0 if betted draw, 1 if betted home team
    '''
    def __init__(self, home : str, away : str, odds : float, betted : int, date : datetime):
        self.home_team = home
        self.away_team = away
        self.odds = odds
        self.date = date
        self.betted = betted
        self.betted_dict = {
            -1 : self.away_team,
            0 : "Draw",
            1 : self.home_team,
        }

    def __str__(self):
        return f"{self.home_team} - {self.away_team} --> {self.betted_dict.get(self.betted, 'Wrong key in self.betted_dict{}')}: {self.odds}"       
    

    