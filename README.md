# lug.cs.uic.edu-2018
------------------------------------------------------------------
* Project Oversight: LUG President Bennett Maciorowski
* Project Lead/Manager: Joshua Castor
* Project BackEnd Lead: Bharat (LUG VP/SysAdmin)
* Project FrontEnd Lead: Joshua Castor

# Requirements
* Node.js 8+

# Setting up the Project

## Basic Setup
1. Download/Clone Development Repo
2. Run `npm install` in the `frontend-site` folder to install dependencies

## Frontend Dev Setup
1. Run through the Basic Setup teps
2. Run `npm run serve` in the `frontend-site` folder to run the dev server for the frontend

## Deployment
1. Run through the Basic Setup steps
2. Set environment variable `FLASK_APP` to have the value `"server.py"`
3. Run `flask run` to start the server
