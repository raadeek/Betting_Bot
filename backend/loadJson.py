import json
from pathlib import Path
from backend.match import Match

def get_data(filename : str):
    BASE_DIR = Path(__file__).parent.parent.resolve()

    a = BASE_DIR / filename

    if not a.exists():
        raise FileNotFoundError

    with open(BASE_DIR / filename, 'r') as f:
        d = json.load(f)


    matches = [Match(match['home'], match['away'], match['homeOdds'], match['awayOdds'], match['drawOdds'], match['date']) for match in d]

    return matches


#get_data('matches.json')

