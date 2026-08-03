#This code is only for generating fictional matches to test frontend

import match, bet, random, json, datetime

from pathlib import Path

TEAMS = [
    "Manchester City",
    "FC Arsenal",
    "Chelsea FC",
    "FC Liverpool",
    "Tottenham Hotspur",
    "Manchester United",
    "Brighton & Hove Albion",
    "Newcastle United",
    "Crystal Palace",
    "AFC Bournemouth",
    "FC Brentford",
    "Aston Villa",
    "Nottingham Forest",
    "FC Everton",
    "Leeds United",
    "AFC Sunderland",
    "FC Fulham",
    "Ipswich Town",
    "Coventry City",
    "Hull City"
]

def generateTeams(data : list):
    if data is None or len(data) < 2:
        raise ValueError
    
    teams = random.sample(data, 2)
    return teams[0], teams[1]

def generateOdds():
    homeOdd = random.uniform(1.2, 5.0)
    awayOdd = 5.0 - homeOdd + 1.0
    drawOdd = (homeOdd + awayOdd) / 2.0

    homeOdd = round(homeOdd * random.uniform(0.9, 1.1), 2)
    awayOdd = round(awayOdd * random.uniform(0.9, 1.1), 2)
    drawOdd = round(drawOdd * random.uniform(0.9, 1.1), 2)

    return homeOdd, awayOdd, drawOdd


def generateDate(days: int):
    dates = []
    a = datetime.date.today()
    for x in range(days):
        dates.append(a + datetime.timedelta(days=x))
    return random.choice(dates)


def createMatch(teams_ : list):
    home, away = generateTeams(teams_)
    homeOdd, awayOdd, drawOdd = generateOdds()
    date = generateDate(10)
    date = str(date)
  
    match_ = match.Match(home, away, homeOdd, awayOdd, drawOdd, date)

    return match_


def generateTestMatches(teams_ : list, n : int):
    matches = [createMatch(teams_) for i in range(n)]
    return matches


def generateJsonFile(filename : str):
    THIS_FILE = Path(__file__).resolve()
    BASE_DIR = THIS_FILE.parent.parent

    matches = generateTestMatches(TEAMS, 20)
    dicts = [m.get_dict() for m in matches]

    with open(BASE_DIR / filename, 'w', encoding='utf-8') as f:
        json.dump(dicts, f, indent=4, ensure_ascii=False)


generateJsonFile('matches.json')



