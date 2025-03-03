# 📌 GottaDo: A Flexible To-Do Management App

## 📖 Overview

GottaDo is a lightweight and intuitive task management web application that allows users to organize their to-dos into three categories based on priority and timeline:

- **Tasks** – Daily tasks that need immediate attention.
- **To-Dos** – Short-term tasks (within a week) that are upcoming but not urgent.
- **GottaDos** – Long-term tasks that should not be forgotten.
- **History Log** – A record of completed tasks for reference and insights.

The application is built using **FastAPI** for the backend and **HTML/JavaScript/CSS** for the front end, ensuring a seamless and dynamic user experience.

---

## ✨ Key Features

### 📂 Task Organization

- Categorize tasks into **Tasks, To-Dos, and GottaDos**.
- **Drag & Drop** functionality to easily move tasks between categories.
- **Tagging System** for efficient filtering and searching.

### 🔍 Search & Filtering

- Search tasks by **title, description, and tags**.
- Filter tasks by **category, priority, or due date**.
- Sort tasks based on **urgency and completion status**.

### ✅ Task Completion & History

- **Mark tasks as complete**, which moves them to the History Log.
- View **previously completed tasks** for reference.
- Option to **revive completed tasks** and move them back into active categories.

### 🔗 Backend & API

- Built with **FastAPI** for efficient handling of CRUD operations.
- Uses an **in-memory database** (list) for storing tasks.
- Provides **RESTful API endpoints** for easy front-end integration.

### 🎨 UI & UX Enhancements

- **Simple and intuitive interface** with a clean design.
- **Color-coded categories** for quick visual organization.
- **Minimalist progress indicators** to track daily task completion.

### 🚀 Future Enhancements (Planned)

- **Recurring tasks** for repetitive actions.
- **Reminders & notifications** for upcoming deadlines.
- **Collaboration features** to share tasks with others.

---

## 📂 Project Structure

```
📦 TaskFlow
├── backend/             # FastAPI backend
│   ├── main.py         # Main API entry point
│   ├── GottaDo_routes.py  # API endpoints for task management
│   ├── GottaDo.py         # Task model and logic
├── frontend/            # Frontend assets
│   ├── index.html      # Main UI
│   ├── style.css       # Styling
│   ├── app.js         # Frontend logic
├── README.md           # Project documentation
```

---

## ⚡ Getting Started

### Prerequisites

- Python 3.11+
- FastAPI
- Uvicorn

### Setup & Run Backend

```sh
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn backend.main:app --reload
```

### Run Frontend

Simply open `frontend/index.html` in a browser.

---

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 📷 Screenshots

(Include relevant screenshots of the app interface here)

