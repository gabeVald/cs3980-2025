const api = 'http://localhost:8000/todos'; //URL of the application (base for different API calls)

//ITS JAVASCRIPT DON'T FORGET ; AT THE END
//Mapping our data from response to frontend table element.
const displayTodos = (todos) => { 
    const tbody = document.getElementById("todo-rows");
    tbody.innerHTML = '' //Contents of tbody in index.html
    const rows = todos.map(x=>{
        return `<tr><td>${x.id}</td><td>${x.title}</td><td>${x.desc}</td><td></td></tr>`//How each row should be mapped from todo x
    });
    tbody.innerHTML = rows.join(' ');
};

//Get the todos from the backend and display them using the displayTodos function
const getTodos = () => {
    const xhr = new XMLHttpRequest() //Instantiate
    xhr.onreadystatechange=()=> { //Open Connection
        if(xhr.readyState == 4 && xhr.status == 200){
            data = JSON.parse(xhr.responseText); //Get Data
            console.log(data);
            displayTodos(data);
        }
    }

    xhr.open('GET', api, true);
    xhr.send();
};

//Running the function when the site loads initially. 
(() => {
    getTodos();
})();