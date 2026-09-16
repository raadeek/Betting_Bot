

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
        oddsButtonsWrapper.appendChild(homeOddsButton);

        const drawOddsButton = document.createElement('button');
        drawOddsButton.classList.add('odds-buttons');
        drawOddsButton.innerText = `${element.draw_odds}`;
        oddsButtonsWrapper.appendChild(drawOddsButton);

        const awayOddsButton = document.createElement('button');
        awayOddsButton.classList.add('odds-buttons');
        awayOddsButton.innerText = `${element.away_odds}`;
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


async function mainFunc(){
    try{
        const response = await getMatchesResponseFromAPI();
        const jsonResponse = await getJsonFromResponse(response);

        createMatchButtons(jsonResponse);

        oddsButtons = document.querySelectorAll(".odds-buttons");
        
        oddsButtons.forEach((button) => {
            button.addEventListener('click', () =>{
                selectOddsButton(button);
            });
        });

    }
    catch(error){
        console.log(error);
    }

}

mainFunc();