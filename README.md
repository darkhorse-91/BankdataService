# BankdataService

This repo contains code for APi service which serves two endpoints to return Indian Banks Data based on query parameter.

## Project Overview

Design and Deploy two endpoints to retrieve data of Indian Banks based on query parameter.
Data used is available from the excel sheet of RBI(Reserve Bank of India).


## Prequisites

* Python 3.6+
* Git

## Project Setup Steps

1. Clone this repo: `$ git clone https://github.com/darkhorse-91/BankdataService.git && cd BankdataService`
2. Create a `.env` file in project root, set env variables that you want to access in the app.
3. Create a virtual environment: `$ python3 -m venv {name of your virtual env}`
4. Activate virtualenv: `$ source {name of your virtual env}/bin/activate`
5. Upgrade pip and install dependencies: `$ pip install --upgrade pip && pip install -r requirements.txt`
6. Run the server: `$ source {name of your virtual env}/bin/activate && python3 main.py`

## API Endpoints

* GET [/api/branches/](http://127.0.0.1:5000/api/branches/?q={search_parameter}) --> Returns response `{'data': [list of lists with matched data]}`
* GET [/api/branches/autocomplete/](http://127.0.0.1:5000/api/branches/autocomplete?q={search_parameter}) --> Returns response `{'data': [list of lists with matched data]}`


## Database 

* Postgres is used as a backend database and connector is Psycopg2 (If you want to use different database or connector you can drop this dependency).


## Hosted Service

* The service is hosted on clever cloud. Endpoints are -

1. http://app-9e83007b-1330-4312-8096-ea2856a1cdb4.cleverapps.io/api/branches/?q=bangalore&limit=5&offset=5

### Curl Script for consuming this endpoint -

curl --location --request GET 'http://app-9e83007b-1330-4312-8096-ea2856a1cdb4.cleverapps.io/api/branches/?q=bangalore&limit=5&offset=5'

2. http://app-9e83007b-1330-4312-8096-ea2856a1cdb4.cleverapps.io/api/branches/autocomplete/?q=rtgs&limit=5&offset=5

### Curl Script for consuming this endpoint -

curl --location --request GET 'http://app-9e83007b-1330-4312-8096-ea2856a1cdb4.cleverapps.io/api/branches/autocomplete/?q=rtgs&limit=5&offset=5'
