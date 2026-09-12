

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

    jsonRespone.forEach(element => {
        const button = document.createElement('button');
        button.innerText = `${element.home} - ${element.away}`;
        buttonsWrapper.appendChild(button);

    });
}



async function mainFunc(){
    try{
        const response = await getMatchesResponseFromAPI();
        const jsonResponse = await getJsonFromResponse(response);

        createMatchButtons(jsonResponse);

    }
    catch(error){
        console.log(error);
    }

}

mainFunc();