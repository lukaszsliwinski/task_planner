# Task planner

## About
This is simply ToDo app based youtube tutorial: https://www.youtube.com/watch?v=llbtoQTt4qw. It was expanded to my own application to plan and manage tasks. It's made for learning Django and gain experience in web development.

## Demo
https://taskplanner.pythonanywhere.com/

## Used technologies
Python 3.8<br>
Django 3.2.3<br>
SQLite3<br>
HTML5<br>
CSS3

## Setup and run on localhost (Windows)
1 Install Python 3.8 from website:<br>
&emsp;https://www.python.org/downloads/release/python-380/<br>
&emsp;Important - remember to mark "Add Python 3.8 to PATH"!<br>
&emsp;![alt text](https://github.com/lukaszsliwinski/task_planner/blob/master/add-python-to-path.png?raw=true)<br><br>
2 Download repository
```bash
git clone https://github.com/lukaszsliwinski/task_planner
```
3 Go into main directory
```bash
cd task_planner
```
4 Create virtual environment with Python 3.8 (you can use any name)
```bash
py -3.8 -m venv name
```
&emsp;This may take a while<br><br>
5 Run virtual environment
```bash
name\scripts\activate
```
&emsp;Important! Keep virtual environment running always when you use app. To deactivate venv use:
```bash
deactivate
```
6 With venv kept running install required packages from requirements.txt file
```bash
pip install -r requirements.txt
```
&emsp;This may take a while<br><br>
7 Create database
```bash
python manage.py migrate
```
8 Run application on localhost
```bash
python manage.py runserver
```
&emsp;Enter https://127.0.0.1:8000 in browser to run main page of an app<br><br>