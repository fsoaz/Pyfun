# 📝 Task Manager CLI (Python)

A simple yet functional **command-line task manager** built with Python.  
This project demonstrates core Python concepts such as data structures, functions, control flow, and user input handling through a practical, real-world use case.

---

## 📌 Project Overview

This Task Manager allows users to manage daily tasks directly from the terminal.  
Users can add, edit, delete, update, and filter tasks by status using an interactive menu-driven interface.

The application runs continuously until the user chooses to quit, providing real-time feedback for every action.

---

## ✨ Features

- ➕ Add new tasks with unique IDs  
- ✏️ Edit existing tasks  
- 🗑️ Remove tasks by ID  
- 🔄 Update task status (Pending, In Progress, Done)  
- 📋 View all tasks  
- 🔍 Filter tasks by status  
- ⚠️ Input validation and user-friendly messages  

---

## 🧠 Key Concepts & Skills Demonstrated

- **Python Command-Line Application Design**
  - Interactive terminal-based application with a persistent menu loop

- **CRUD Operations**
  - Create, read, update, and delete functionality for tasks

- **Data Modeling**
  - Lists for task storage
  - Dictionaries for task attributes (ID, title, status)

- **Function-Based Architecture**
  - Reusable, single-responsibility functions
  - Improved readability and maintainability

- **State Management**
  - In-memory data handling
  - Unique task IDs using a global counter

- **Control Flow**
  - `while` loops for continuous execution
  - `if / elif / else` for decision-making
  - `for` loops for searching and updating data

- **Input Validation**
  - Numeric input validation using `.isdigit()`
  - Status validation before updates

- **Task Workflow Management**
  - Task lifecycle: Pending → In Progress → Done
  - Filtering tasks by status with list comprehensions

- **String Formatting**
  - Clean output using Python f-strings

- **Problem Solving**
  - Handling empty task lists and invalid task IDs
  - Clear success and error messages

---

## 🛠️ Technologies Used

- **Language:** Python 3  
- **Environment:** Command Line / Terminal  
- **Libraries:** Python Standard Library only  
