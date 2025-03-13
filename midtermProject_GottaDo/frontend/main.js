const api = `http://127.0.0.1:8000/tasks`;

document.getElementById("save").addEventListener("click", (e) => {
    console.log("button pressed");
    e.preventDefault();
    postTodo();
    const closeBtn = document.getElementById("modal-close");
    closeBtn.click();
});

const alertPlaceholder = document.getElementById("liveAlertPlaceholder");
const appendAlert = (message, type) => {
    const wrapper = document.createElement("div");
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        "</div>",
    ].join("");

    alertPlaceholder.append(wrapper);
};

const deleteItem = (id) => {
    console.log(`Deleting item with ID: ${id}`);
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            //Re-display:
            getAll();
            appendAlert(`Deleted Item with ID: ${id}`, "success");
        }
    };
    xhr.open("DELETE", `${api}/${id}`, true);
    xhr.send();
};

const togglePriority = (id) => {
    console.log(`Updating priority of item with id: ${id}`);
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            getAll();
        }
    };
    xhr.open("PATCH", `${api}/high_priority/${id}`, true);
    xhr.send();
    getAll();
    appendAlert(`Priority updated for Item with ID: ${id}`, "success");
};

const postTodo = () => {
    const titleInput = document.getElementById("title-input");
    const title = titleInput.value;
    const descInput = document.getElementById("description-input");
    const description = descInput.value;
    const highPriorityCheckbox = document.getElementById("high-priority");
    const high_priority = highPriorityCheckbox.checked;
    const itemTypeSelect = document.getElementById("item-type");
    let level = itemTypeSelect.value;
    const tags = [];
    const completed = false;
    const created_date = new Date();
    const completed_date = new Date(44, 3, 15);

    if (level == 1) {
        level = "task";
    } else if (level == 2) {
        level = "todo";
    } else if (level == 3) {
        level = "gottado";
    }

    console.log(title);
    console.log(description);

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 201) {
            getAll();
            titleInput.value = "";
            descInput.value = "";
            highPriorityCheckbox.checked = false;
            itemTypeSelect.selectedIndex = 0;
        }
    };
    xhr.open("POST", `${api}/create`, true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(
        JSON.stringify({
            title,
            description,
            tags,
            completed,
            created_date,
            completed_date,
            high_priority,
            level,
        })
    );
    appendAlert(`Created ${level}!`, "success"); //MUST MATCH ABOVE REFERENCES
};

const updateItem = (id) => {
    console.log(`Updating item with ID: ${id}`);
    const titleInput = document.getElementById(`title-input-${id}`);
    const title = titleInput.value;
    const descriptionInput = document.getElementById(`description-input-${id}`);
    const description = descriptionInput.value;

    // Update counter to track when both requests are complete
    let updatesCompleted = 0;

    // Create separate XHR objects for each request
    const titleXhr = new XMLHttpRequest();
    const descXhr = new XMLHttpRequest();

    // Handler for both requests
    const handleComplete = () => {
        updatesCompleted++;
        if (updatesCompleted === 2) {
            getAll(); // Only refresh after both updates are done
        }
    };

    // Title update
    titleXhr.onreadystatechange = () => {
        if (titleXhr.readyState == 4 && titleXhr.status == 200) {
            handleComplete();
        }
    };

    // Description update
    descXhr.onreadystatechange = () => {
        if (descXhr.readyState == 4 && descXhr.status == 200) {
            handleComplete();
        }
    };

    // Send title update
    titleXhr.open("PATCH", `${api}/title/${id}`, true);
    titleXhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    titleXhr.send(JSON.stringify(title));

    // Send description update
    descXhr.open("PATCH", `${api}/desc/${id}`, true);
    descXhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    descXhr.send(JSON.stringify(description));
    appendAlert(`Updated Item with ID: ${id}`, "success");
};

const displayAll = (all) => {
    console.log("Display All called with:", all); // Debug log

    const tasks = all.all_items.task.map((task) => task);
    const todos = all.all_items.todo.map((todo) => todo);
    const gottados = all.all_items.gottado.map((gottado) => gottado);

    console.log("Parsed arrays:", { tasks, todos, gottados }); // Debug log

    //task logic
    const task_accordion = document.getElementById("task-accordion");
    task_accordion.innerHTML = "";
    const task_items = tasks.map((x) => {
        const priority = x.high_priority;
        let logo = "";
        let logoStyle = "";
        if (priority == true) {
            logo = "⭐";
            logoStyle = "background-color: gold;";
        } else if (priority == false) {
            logo = "★";
        }

        return `<div class="accordion-item">
					<h2 class="accordion-header" id="heading${x.id}">
						<div class="accordion-button collapsed input-group" 
									type="button"
									data-bs-toggle="collapse"
									data-bs-target="#collapse${x.id}"
									aria-expanded="false"
									aria-controls="collapse${x.id}">
							<input id="title-input-${x.id}" type="text" class="form-control" value="${x.title}" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
						</div>

					</h2>
					<div
						id="collapse${x.id}"
						class="accordion-collapse collapse"
						aria-labelledby="heading${x.id}"
						data-bs-parent="#todo-accordion"
					>
						<div class="row">
							<div class="col-12">
								<div class="form-floating">
									<textarea class="form-control" placeholder="Description" id="description-input-${x.id}" style="height: 100px">${x.description}</textarea>
									<label for="description${x.id}">Description</label>
								</div>
							</div>
						</div>
						<div class="row">
							<div class="col-12 d-flex justify-content-end">
								<div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
									<div class="btn-group" role="group" aria-label="Basic outlined example">
											<input
												type="checkbox"
												class="btn-check"
												onclick="togglePriority(${x.id})"
												id="btn-check-${x.id}"
												autocomplete="off"
											/>
											<label class="btn btn-outline-primary" style="${logoStyle}" for="btn-check-${x.id}">${logo}</label>

											<button
												onclick="updateItem(${x.id})"
												type="button"
												id="update-${x.id}"
												class="btn btn-outline-primary"
											>
												💾
											</button>
											<button
												onclick="deleteItem(${x.id})"
												type="button"
												id="delete${x.id}"
												class="btn btn-outline-primary"
											>
												🗑️
											</button>
										</div>
									</div>
									<a
										tabindex="0"
										role="button"
										class="btn btn-outline-primary popover-dismiss"
										data-bs-toggle="popover"
										data-bs-trigger="focus"
										data-bs-title="Metadata"
										data-bs-content="Item ID: ${x.id}<br>
														Creation Date: ${x.created_date}<br>
														Expiration Date: ${x.expired_date}<br>
														Completed Date: ${x.completed_date}"
									>
										Info
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>`;
    });

    task_accordion.innerHTML = task_items.join(" ");
    //todo logic
    const todo_accordion = document.getElementById("todo-accordion");
    todo_accordion.innerHTML = "";
    const todo_items = todos.map((x) => {
        const priority = x.high_priority;
        let logo = "";
        let logoStyle = "";
        if (priority == true) {
            logo = "⭐";
            logoStyle = "background-color: gold;";
        } else if (priority == false) {
            logo = "★";
        }

        return `<div class="accordion-item">
					<h2 class="accordion-header" id="heading${x.id}">
						<div class="accordion-button collapsed input-group" 
									type="button"
									data-bs-toggle="collapse"
									data-bs-target="#collapse${x.id}"
									aria-expanded="false"
									aria-controls="collapse${x.id}">
							<input id="title-input-${x.id}" type="text" class="form-control" value="${x.title}" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
						</div>

					</h2>
					<div
						id="collapse${x.id}"
						class="accordion-collapse collapse"
						aria-labelledby="heading${x.id}"
						data-bs-parent="#todo-accordion"
					>
						<div class="row">
							<div class="col-12">
								<div class="form-floating">
									<textarea class="form-control" placeholder="Description" id="description-input-${x.id}" style="height: 100px">${x.description}</textarea>
									<label for="description${x.id}">Description</label>
								</div>
							</div>
						</div>
						<div class="row">
							<div class="col-12 d-flex justify-content-end">
								<div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
									<div class="btn-group" role="group" aria-label="Basic outlined example">
											<input
												type="checkbox"
												class="btn-check"
												onclick="togglePriority(${x.id})"
												id="btn-check-${x.id}"
												autocomplete="off"
											/>
											<label class="btn btn-outline-primary" style="${logoStyle}" for="btn-check-${x.id}">${logo}</label>

											<button
												onclick="updateItem(${x.id})"
												type="button"
												id="update-${x.id}"
												class="btn btn-outline-primary"
											>
												💾
											</button>
											<button
												onclick="deleteItem(${x.id})"
												type="button"
												id="delete${x.id}"
												class="btn btn-outline-primary"
											>
												🗑️
											</button>
										</div>
									</div>
									<a
										tabindex="0"
										role="button"
										class="btn btn-outline-primary popover-dismiss"
										data-bs-toggle="popover"
										data-bs-trigger="focus"
										data-bs-title="Metadata"
										data-bs-content="Item ID: ${x.id}<br>
														Creation Date: ${x.created_date}<br>
														Expiration Date: ${x.expired_date}<br>
														Completed Date: ${x.completed_date}"
									>
										Info
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>`;
    });
    todo_accordion.innerHTML = todo_items.join(" ");
    //gottado logic
    const gottado_accordion = document.getElementById("gottado-accordion");
    gottado_accordion.innerHTML = "";
    const gottado_items = gottados.map((x) => {
        const priority = x.high_priority;
        let logo = "";
        let logoStyle = "";
        if (priority == true) {
            logo = "⭐";
            logoStyle = "background-color: gold;";
        } else if (priority == false) {
            logo = "★";
        }

        return `<div class="accordion-item">
					<h2 class="accordion-header" id="heading${x.id}">
						<div class="accordion-button collapsed input-group" 
									type="button"
									data-bs-toggle="collapse"
									data-bs-target="#collapse${x.id}"
									aria-expanded="false"
									aria-controls="collapse${x.id}">
							<input id="title-input-${x.id}" type="text" class="form-control" value="${x.title}" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
						</div>

					</h2>
					<div
						id="collapse${x.id}"
						class="accordion-collapse collapse"
						aria-labelledby="heading${x.id}"
						data-bs-parent="#todo-accordion"
					>
						<div class="row">
							<div class="col-12">
								<div class="form-floating">
									<textarea class="form-control" placeholder="Description" id="description-input-${x.id}" style="height: 100px">${x.description}</textarea>
									<label for="description${x.id}">Description</label>
								</div>
							</div>
						</div>
						<div class="row">
							<div class="col-12 d-flex justify-content-end">
								<div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
									<div class="btn-group" role="group" aria-label="Basic outlined example">
											<input
												type="checkbox"
												class="btn-check"
												onclick="togglePriority(${x.id})"
												id="btn-check-${x.id}"
												autocomplete="off"
											/>
											<label class="btn btn-outline-primary" style="${logoStyle}" for="btn-check-${x.id}">${logo}</label>

											<button
												onclick="updateItem(${x.id})"
												type="button"
												id="update-${x.id}"
												class="btn btn-outline-primary"
											>
												💾
											</button>
											<button
												onclick="deleteItem(${x.id})"
												type="button"
												id="delete${x.id}"
												class="btn btn-outline-primary"
											>
												🗑️
											</button>
										</div>
									</div>
									<a
										tabindex="0"
										role="button"
										class="btn btn-outline-primary popover-dismiss"
										data-bs-toggle="popover"
										data-bs-trigger="focus"
										data-bs-title="Metadata"
										data-bs-content="Item ID: ${x.id}<br>
														Creation Date: ${x.created_date}<br>
														Expiration Date: ${x.expired_date}<br>
														Completed Date: ${x.completed_date}"
									>
										Info
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>`;
    });
    gottado_accordion.innerHTML = gottado_items.join(" ");

    const popoverTriggerList = document.querySelectorAll(".popover-dismiss");
    [...popoverTriggerList].forEach(
        (el) =>
            new bootstrap.Popover(el, {
                trigger: "focus",
                html: true,
            })
    );
};

const getAll = () => {
    const xhr = new XMLHttpRequest(); //Instantiate
    xhr.onreadystatechange = () => {
        //Open Connection
        if (xhr.readyState == 4 && xhr.status == 200) {
            const data = JSON.parse(xhr.responseText); //Get Data
            console.log(data);
            displayAll(data);
        }
    };

    xhr.open("GET", `${api}/all`, true);
    xhr.send();
};
(() => {
    getAll();
})();
