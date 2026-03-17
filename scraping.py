import requests
from bs4 import BeautifulSoup

#gets url from a file (must be only one url in a file)
def get_url(filename : str) -> str:
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
        
def get_response(url : str):
    return requests.get(url)

def get_soup(url : str) -> BeautifulSoup:
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






