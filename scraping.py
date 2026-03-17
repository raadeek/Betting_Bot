import requests
from bs4 import BeautifulSoup

url = 'https://www.betclic.pl/pilka-nozna-sfootball/premier-league-c3'

def get_response(url):
    return requests.get(url)

def get_soup() -> BeautifulSoup:
    return BeautifulSoup(get_response(url).text, "html.parser")

#return dict with dates (strings) as keys, and list of match spacebars (QueryResults) as values
def get_matches_dates(soup : BeautifulSoup) -> dict : 
    cardEvents = soup.find_all(class_='groupEvents')
    score_wrappers = [event.find_all(class_='scoreboard_wrapper') for event in cardEvents]
    dates=[event.find(class_='groupEvents_headTitle').text for event in cardEvents]

    return dict(zip(dates, score_wrappers))


def print_matches(data : dict):
    for i in range(len(data)):
        print(list(data.keys())[i])
        for j in list(data.values())[i]:
            print(f"      {j.text}")






