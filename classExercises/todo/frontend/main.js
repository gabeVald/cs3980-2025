const api = 'http://127.0.0.1:8000/todos'; //URL of the application (base for different API calls)

//ITS JAVASCRIPT DON'T FORGET ; AT THE END
//Mapping our data from response to frontend table element.


//FOR UPDATE: IN INDEX: ADD NEW MODAL WITH ID EDIT/SAVE SO YOU CAN HAVE AN EVENT LISTENER WHICH HITS THE UPDATE ENDPOINTS

//SUPER IMPORTANT CONCEPT IN JS: EVENT LISTENER
document.getElementById('save-new-todo').addEventListener('click', (e) => {
    e.preventDefault();
    postTodo();
    const closeBtn= document.getElementById('add-close')
    closeBtn.click();
});

//SUPER IMPORTANT, PAIRED W ABOVE
const postTodo= () => {
    const titleInput = document.getElementById("new-title");
    const title = titleInput.value;
    const descInput = document.getElementById("new-desc");
    const desc = descInput.value; 
    console.log(title)
    console.log(desc); 

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange=()=>{
    if(xhr.readyState== 4 && xhr.status == 201){
        getTodos();
        };
    };
    xhr.open("POST", api, true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({title, desc})); //MUST MATCH ABOVE REFERENCES
};

const deleteTodo=(id)=>{
    console.log(`Deleting todo id = ${id}`);
    const xhr = new XMLHttpRequest()
    xhr.onreadystatechange=()=>{
        if(xhr.readyState== 4 && xhr.status == 200){
            //Re-display
            getTodos();
            };
        };
        xhr.open("DELETE", `${api}/${id}`, true);
        xhr.send();

}

const displayTodos = (todos) => { 
    const tbody = document.getElementById("todo-rows");
    tbody.innerHTML = '' //Contents of tbody in index.html
    const rows = todos.map(x=>{
        return `<tr>
                    <td>${x.id}</td>
                    <td>${x.title}</td>
                    <td>${x.desc}</td>
                    <td><button onclick="deleteTodo(${x.id})" id='delete-${x.id}' type="button" class="btn btn-danger">Delete</button></td>
                </tr>`//How each row should be mapped from todo x
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