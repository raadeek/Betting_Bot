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
        response = requests.get(url)
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

    def get_match_from_team_name(self, team_name : str):               #TODO problem when one team has more than one match on the page
        data = self.matches_dict
        for i in range(len(data)):
            for j in list(data.values())[i]:
                if team_name in j.text:
                    print(j.text)
                    return j


    def print_matches(self):
        data = self.matches_dict
        for i in range(len(data)):
            print(list(data.keys())[i])
            for j in list(data.values())[i]:
                print(f"      {j.text}")


sc = Scraping('urls.txt')

