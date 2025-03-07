const census = `https://datausa.io/api/data?drilldowns=Nation&measures=Population`;

const displayCensus = (censusData) => { 
    const tbody = document.getElementById("todo-rows");
    tbody.innerHTML = '' 
    const rows = censusData.data.reverse().map(x => {
        return `<tr>
                    <td>${x.Year}</td>
                    <td>${x.Population.toLocaleString()}</td>
                </tr>`
    });
    tbody.innerHTML = rows.join('');
};


const getAll = () => {
    const xhr = new XMLHttpRequest() //Instantiate
    xhr.onreadystatechange=()=> { //Open Connection
        if(xhr.readyState == 4 && xhr.status == 200){
            const data = JSON.parse(xhr.responseText); //Get Data
            console.log(data);
            displayCensus(data);
        }
    }

    xhr.open('GET', census, true);
    xhr.send();
};


(() => {
    getAll();
})();