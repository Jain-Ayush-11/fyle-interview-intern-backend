# Fyle Backend Challenge

## Project Setup

The project is dockerized so just need to build and run the docker container.
Install Docker Desktop for easy GUI on windows. Clone the project and open a terminal.
```
$ docker-compose up --build
```
This will build the container and once completed, the container will be running and visible in the container section of the Docker Desktop.
Even if the terminal is closed, the container can be started/stopped from the GUI.<br><br>
<br>This container will run all the resources (redis, postgres, etc) for the project.
<br>We can now access the server at [http://localhost:8000/](http://localhost:8000/).

## Test Coverage

![WhatsApp Image 2024-01-19 at 01 02 54](https://github.com/Jain-Ayush-11/fyle-interview-intern-backend/assets/76158814/96c95770-be84-455e-9451-5357b6546538)


## Who is this for?

This challenge is meant for candidates who wish to intern at Fyle and work with our engineering team. You should be able to commit to at least 6 months of dedicated time for internship.

## Why work at Fyle?

Fyle is a fast-growing Expense Management SaaS product. We are ~40 strong engineering team at the moment. 

We are an extremely transparent organization. Check out our [careers page](https://careers.fylehq.com) that will give you a glimpse of what it is like to work at Fyle. Also, check out our Glassdoor reviews [here](https://www.glassdoor.co.in/Reviews/Fyle-Reviews-E1723235.htm). You can read stories from our teammates [here](https://stories.fylehq.com).


## Challenge outline

This challenge involves writing a backend service for a classroom. The challenge is described in detail [here](./Application.md)


## What happens next?

You will hear back within 48 hours from us via email. 


## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
