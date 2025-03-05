const api = `http://localhost:8000/tasks`;

const displayAll = (all) => {
    const tasks = all.all_items.task.map(task => task);
    const todos = all.all_items.todo.map(todo => todo);
    const gottados = all.all_items.gottado.map(gottado => gottado);
    //task logic
    const task_accordion = document.getElementById("task-accordion");
    task_accordion.innerHTML = ''
    const task_items = tasks.map((x) => {
        return `<div class="accordion-item">
                  <h2 class="accordion-header" id="heading${x.id}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${x.id}" aria-expanded="false" aria-controls="collapse${x.id}">
                      ${x.title}
                    </button>
                  </h2>
                  <div id="collapse${x.id}" class="accordion-collapse collapse" aria-labelledby="heading${x.id}" data-bs-parent="#task-accordion">
                    <div class="accordion-body">
                      ${x.description}
                    </div>
                  </div>
                </div>`;
    });
    task_accordion.innerHTML = task_items.join(' ');
    //todo logic
    const todo_accordion = document.getElementById("todo-accordion");
    todo_accordion.innerHTML = ''
    const todo_items = todos.map((x) => {
        return `<div class="accordion-item">
            <h2 class="accordion-header" id="heading${x.id}">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${x.id}" aria-expanded="false" aria-controls="collapse${x.id}">
                ${x.title}
              </button>
            </h2>
            <div id="collapse${x.id}" class="accordion-collapse collapse" aria-labelledby="heading${x.id}" data-bs-parent="#todo-accordion">
              <div class="accordion-body">
                ${x.description}
                <button type="button" class="btn" data-bs-toggle="popover" data-bs-title="Metadata" data-bs-content="Creation Date: ${x.created_date} \n Expiration Date: ${x.expired_date} \n Completed Date: ${x.completed_date} ">Metadata</button>
              </div>
            </div>
          </div>`;
    });
    todo_accordion.innerHTML = todo_items.join(' ');
    //gottado logic
    const gottado_accordion = document.getElementById("gottado-accordion");
    gottado_accordion.innerHTML = ''
    const gottado_items = gottados.map((x) => {
        return `<div class="accordion-item">
                  <h2 class="accordion-header" id="heading${x.id}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${x.id}" aria-expanded="false" aria-controls="collapse${x.id}">
                      ${x.title}
                    </button>
                  </h2>
                  <div id="collapse${x.id}" class="accordion-collapse collapse" aria-labelledby="heading${x.id}" data-bs-parent="#task-accordion">
                    <div class="accordion-body">
                      ${x.description}
                    </div>
                  </div>
                </div>`;
    });
    gottado_accordion.innerHTML = gottado_items.join(' ');

    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
    [...popoverTriggerList].forEach(el => new bootstrap.Popover(el));
};

const getAll = () => {
    const xhr = new XMLHttpRequest() //Instantiate
    xhr.onreadystatechange=()=> { //Open Connection
        if(xhr.readyState == 4 && xhr.status == 200){
            const data = JSON.parse(xhr.responseText); //Get Data
            console.log(data);
            displayAll(data);
        }
    }

    xhr.open('GET', `${api}/all`, true);
    xhr.send();
};

(() => {
    getAll();

    
})();
