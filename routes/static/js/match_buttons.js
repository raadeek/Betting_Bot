

async function getMatchesResponseFromAPI(){
    try{
        const response = await fetch("api/data");
        
        if(!response){
            throw new Error("Cannot fetch matchData");
        }

        return response;

    }
    catch(error){
        console.error(error);
    }
}

function getJsonFromResponse(response) {
    return response.json();
}


function createMatchButtons(jsonRespone){
    buttonsWrapper = document.querySelector(".match-buttons-wrapper");

    try{
        jsonRespone.forEach(element => {
        const matchWrapper = document.createElement('div');
        matchWrapper.classList.add("match-button-wrapper");
        matchWrapper.id = element.id;
        buttonsWrapper.appendChild(matchWrapper);

        const teamNamesWrapper = document.createElement('div');
        teamNamesWrapper.classList.add("team-names-wrapper");
        teamNamesWrapper.innerText = `${element.home_team} vs ${element.away_team}`;
        matchWrapper.appendChild(teamNamesWrapper);

        const oddsButtonsWrapper = document.createElement('div');
        oddsButtonsWrapper.classList.add('odds-buttons-wrap');
        matchWrapper.appendChild(oddsButtonsWrapper);

        const homeOddsButton = document.createElement('button');
        homeOddsButton.classList.add('odds-buttons');
        homeOddsButton.innerText = `${element.home_odds}`;
        homeOddsButton.dataset.buttonType = "home_odds";
        oddsButtonsWrapper.appendChild(homeOddsButton);

        const drawOddsButton = document.createElement('button');
        drawOddsButton.classList.add('odds-buttons');
        drawOddsButton.innerText = `${element.draw_odds}`;
        drawOddsButton.dataset.buttonType = "draw_odds";
        oddsButtonsWrapper.appendChild(drawOddsButton);

        const awayOddsButton = document.createElement('button');
        awayOddsButton.classList.add('odds-buttons');
        awayOddsButton.innerText = `${element.away_odds}`;
        awayOddsButton.dataset.buttonType = "away_odds";
        oddsButtonsWrapper.appendChild(awayOddsButton);


        });
    }
    catch(error){
        console.error(error);
    }

}

function selectOddsButton(selectedButton){
    const buttonsWrapper = selectedButton.parentElement;
    const oddsButtons = Array.from(buttonsWrapper.children);

    selectedButton.classList.toggle('selected');

    oddsButtons.forEach((btn) => {
        if(btn != selectedButton){
            btn.classList.remove('selected');
        }
    });
}

function createBet(selectedButtons){           //TODO check if user is logged in
    if(!selectedButtons || selectedButtons.length == 0){
        console.log("No buttons selected");
        return;
    }

    try{
        let odds = 1;
        const beteventList = [];

        selectedButtons.forEach((element) =>{
            odds *= parseFloat(element.innerText);
            const betEvent = {
                "eventId" : element.parentElement.parentElement.id,
                "bettedOn" : element.dataset.buttonType
            };
            beteventList.push(betEvent);

        });

        odds = Number(odds.toFixed(2));

        const date = new Date();


        let betJson = {
            "odds" : odds,
            "username" : "test",
            "date" : date,
            "betList" : beteventList
        };

        return betJson;

    }
    catch(error){
        console.error(error);
    }

}


async function mainFunc(){
    try{
        const response = await getMatchesResponseFromAPI();
        const jsonResponse = await getJsonFromResponse(response);

        createMatchButtons(jsonResponse);

        const oddsButtons = document.querySelectorAll(".odds-buttons");
        
        oddsButtons.forEach((button) => {
            button.addEventListener('click', () =>{
                selectOddsButton(button);
            });
        });

        const betButton = document.querySelector(".bet-button");

        betButton.addEventListener('click', () =>{
            const selectedButtons = document.querySelectorAll(".selected");

            let betJson = createBet(selectedButtons);
            console.log(betJson); 
        });

    }
    catch(error){
        console.log(error);
    }

}

mainFunc();