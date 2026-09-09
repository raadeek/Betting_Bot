from flask import Flask, render_template
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.loadJson import get_data

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/matches')
def display_matches():
    data = get_data('matches.json')

    return render_template('matches_list.html', matches=data)




if __name__ == '__main__':
    app.run(debug=True)

