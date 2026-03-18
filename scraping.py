from datetime import datetime
import requests
from bs4 import BeautifulSoup

YEAR='2026'

#gets url from a file (must be only one url in a file)
def get_url(filename : str) -> str:
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
        

def get_soup(url : str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


#return dict with dates (strings) as keys, and list of match spacebars (list[QueryResults]) as values
def create_matches_dict(soup : BeautifulSoup) -> dict : 
    cardEvents = soup.find_all(class_='groupEvents')
    score_wrappers = [event.find_all(class_='scoreboard_wrapper') for event in cardEvents]
    dates=[event.find(class_='groupEvents_headTitle').text for event in cardEvents]

    return dict(zip(dates, score_wrappers))


def get_date(data_str : str) -> datetime:       #data_str format 'xxx day/month'
    date = data_str.split()
    raw_date = date[1] + f'/{YEAR}'
    mask = "%d/%m/%Y"

    return datetime.strptime(raw_date, mask)


def print_matches(data : dict):
    for i in range(len(data)):
        print(list(data.keys())[i])
        for j in list(data.values())[i]:
            print(f"      {j.text}")






