from datetime import datetime
import requests
from bs4 import BeautifulSoup

YEAR='2026'

'''
Scraping gets data from website
'''

class Scraping:
    def __init__(self, filename):
        self.url = self.get_url(filename)
        self.soup = self.get_soup(self.url)
        self.matches_dict = self.create_matches_dict(self.soup)
        #self.print_matches()

    #gets url from a file (must be only one url in a file)
    @staticmethod
    def get_url(filename : str) -> str:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
            
    @staticmethod
    def get_soup(url : str) -> BeautifulSoup:
        response = requests.get(url.strip())
        return BeautifulSoup(response.text, "html.parser")


    #return dict with dates (strings) as keys, and list of match spacebars (list[QueryResults]) as values
    @staticmethod
    def create_matches_dict(soup : BeautifulSoup) -> dict : 
        cardEvents = soup.find_all(class_='groupEvents')
        #score_wrappers = [event.find_all(class_='scoreboard_wrapper') for event in cardEvents]
        match_event = [event.find_all(class_='cardEvent_content') for event in cardEvents]
        dates=[event.find(class_='groupEvents_headTitle').text for event in cardEvents]
        return dict(zip(dates, match_event))
    



    def get_date(data_str : str) -> datetime:       #data_str format 'xxx day/month'
        date = data_str.split()
        raw_date = date[1] + f'/{YEAR}'
        mask = "%d/%m/%Y"
        return datetime.strptime(raw_date, mask)
    
    @staticmethod
    def get_home_team(match) -> str:
        if match is None or not match:
            raise ValueError("get_home_team error.")

        return match[0].find(class_='scoreboard_contestant scoreboard_contestant-1').text
    
    
    @staticmethod
    def get_away_team(match) -> str:
        if match is None or not match:
            raise ValueError("get_away_team error.")

        return match[0].find(class_='scoreboard_contestant scoreboard_contestant-2').text
    
    
    #index = 0; home_odds, index = 1; draw_odds, index = 2; away_odds
    @staticmethod
    def get_odds(match, index) -> str: 
        if match is None or not match:
            raise ValueError("get_home_odds error.")

        odds = [div.get_text(strip=True) for div in match[0].find_all(class_='btn_label') if div.get_text(strip=True)[0].isdigit()]
        return odds[index]


    def get_match_from_team_name(self, team_name : str):               #TODO problem when one team has more than one match on the page
        data = self.matches_dict
        for i in range(len(data)):
            for j in list(data.values())[i]:
                if team_name in j.text:
                    return j
                
    def get_matches_from_date(self, date) -> list:
        data = self.matches_dict
        for i in range(len(data)):
            if date in list(data.keys())[i]:
                return [j for j in list(data.values())[i]]    
        return -1      


    
    #used in create_bet_event
    @staticmethod
    def get_betted(teamname, home, away):
        if teamname in home:
            return 1
        elif teamname in away:
            return -1
        else:
            return 0

    #creates dict with data needed for bet_event based on self.matches_dict. teamname - team which has been betted on
    def create_bet_event(self, teamname : str) -> dict:
        data = self.matches_dict
        query = self.get_match_from_team_name(teamname)
        bet_event = {
            "home" : query.find(class_='scoreboard_contestant scoreboard_contestant-1').text,
            "away" : query.find(class_='scoreboard_contestant scoreboard_contestant-2').text,
            "odds" : [div.get_text(strip=True) for div in query.find_all(class_='btn_label') if div.get_text(strip=True)[0].isdigit()],             #TODO add date
        }
        
        bet_event["betted"] = self.get_betted(teamname, bet_event['home'], bet_event['away'])

        return bet_event


    def print_matches(self):
        data = self.matches_dict
        for i in range(len(data)):
            print(list(data.keys())[i])
            for j in list(data.values())[i]:
                print(f"      {j.text}")



if __name__ == "__main__":
    sc = Scraping('urls.txt')
    #sc.print_matches()
    matches = sc.get_matches_from_date("19")
    print(matches[0].text)
    print(sc.get_home_team(matches))
    print(sc.get_away_team(matches))
    for i in range(3):
        print(sc.get_odds(matches, i))