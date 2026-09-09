

async function getMatchesDataFromAPI(){
    try{
        const response = await fetch("api/data");
        
        if(!response){
            throw new Error("Cannot fetch matchData");
        }

        console.log(response);

        const matchData = response.json();

        console.log(matchData);

    }
    catch(error){
        console.error(error);
    }
}


function mainFunc(){
    try{
        getMatchesDataFromAPI();
    }
    catch(error){
        console.log(error);
    }

}

mainFunc();