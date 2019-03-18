# Kanban Board User Guide
**CS162 Assignment**
**Yuhao Chen**

## Introduction to KanBan Application
This KanBan Board application is designed to help people to manage their schedule. They can add new event to the KanBan
Board. There are three states for an event: "doing", "to do", and "done". If an event is marked as doing, it means you are
doing this task; if an event is marked as "to do", it means you are going to do this task in the future; if an event is
marked as "done", it means you have done this task. The states of events can be switched to each other. You can also
delete an event from the Board.

## Instruction for Installation

1. Use `cd` to enter the CS162_Kanban folder

2. Use `python3.6 -m venv .venv` command to create the python environment for the application

3. Use `source .venv/bin/activate` command to activate the python environment

4. Use `pip3 install -r requirements.txt` command to install the required libraries for the application

5. Use `python3 run.py` command to run the application

## Instruction for Unittest

1. Use `cd` to enter the CS162_Kanban folder

2. Use `python test_basic.py` command to run the unit test

## Structure of Project

   $ CS162_Kanban
    ├── Kanban
    │   ├── __init__.py
    │   ├── routes.py
    │   ├── templates
    │   │   └── index.html
    │   └── static
    │       └── CSS
    │           └── style.css
    ├── venv
    ├── README.md
    ├── requirements.txt
    ├── test_basic.py
    └── run.py

When entering the CS162_Kanban folder, there will be six files.

+ File “README.md” is the markdown file which explains the main function of the application and instructs a user to install and run the application.

+ Folder “venv” is used to create the environment for using the application. By using command `python3.6 -m venv .venv` and `source .venv/bin/activate`, we can create create the environment and activate it for the application.

+ File “requirements.txt” lists the necessary libraries to use the application. By using command `pip3 install -r requirements.txt`, we can install all required libraries.

+ File “run.py” is the running entry for the application. One can use command `python run.py` to run the Kanban Board application. In this file, I create a database and call the commands from routes.py in Kanban folder.

+ File “test_basic.py” is used for unit test. One can use command `python test_basic.py` to see the result of unit test. In this file, I write 13 unit tests, which tests all post and get requests the application may have.

+ Folder “Kanban” includes most of the code of this project.

  - File “__init__.py” initialize the application, where we build the flask framework.

  - File “routes.py” serves as a terminal which deals with post and get requests and renders the templates for the pages. We use python code and the flask framework to do operations.

  - File “index.html” supports the structure of the homepage of the Kanban Board.

  - File “style.css” supports the styles for the html code of the homepage.



