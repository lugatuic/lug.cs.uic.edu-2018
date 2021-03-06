# lug.cs.uic.edu-2018
------------------------------------------------------------------
* Project Oversight: LUG President Bennett Maciorowski
* Project Lead/Manager: Joshua Castor
* Project BackEnd Lead: Will Toher
* Project Deployment: Bharat Middha (LUG VP/SysAdmin)
* Project FrontEnd Lead: Joshua Castor

# Requirements
* Git
* Node.js 8+
* NPM 6.4.x+ (should come with Node.js)
* Python 3.7.x
* [Pipenv](https://github.com/pypa/pipenv) (recommended)
* An editor that supports Pylint, Editorconfig, ESLint, and Vue syntax highlighting, e.g. VSCode

# Deployment

(TODO)
Current thoughts are to run back end and front end from 2 different docker containers 

# Contributing

We are using a version of the [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) style in this repository. This means that the `master` branch, the first branch you see when you load this page, is the last stable version of the website, and the `develop` branch incorporates more recent changes. Any changes you make should be done in *a new branch which derives from `develop`*.

## Contributing to the Frontend

The frontend site is a project using the **Vue.js** framework.

### Installation

First, make sure you have the following installed:

* Git
* Node.js 8+
* NPM 6.4.x+ (should come with Node.js)
* An editor that supports ESLint and Vue syntax highlighting, e.g. VSCode

Clone the repository and go to the `frontend-site` folder:
```
git clone https://github.com/lugatuic/lug.cs.uic.edu-2018.git
cd lug.cs.uic.edu-2018
cd frontend-site
```

Switch to the `develop` branch:
```
git checkout develop
```

Install dependencies with npm:
```
npm install
```

#### VSCode Setup

If you are using VSCode, you should install the following plugins:
* [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur)
* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

### Running

From the `frontend-site` folder, run the following command to start a local development server. As you make changes to the Vue project, the local server will auto compile your changes and let you know of any errors found.
```
npm run serve
```

If you need to access any backend API endpoints during development, refer to the instructions below on setting up the backend server.

## Contributing to the Backend

The backend server is based on **Python 3.7.x**, using the **Flask** framework.

### Installation

First, make sure you have the following installed:
* Git
* Python 3.7.x
* [Pipenv](https://github.com/pypa/pipenv) (recommended)
* An editor that supports Pylint and Editorconfig, e.g. VSCode

Clone the repository:
```
git clone https://github.com/lugatuic/lug.cs.uic.edu-2018.git
cd lug.cs.uic.edu-2018
```

Switch to the 'develop' branch:
```
git checkout develop
```

Install Python packages with pipenv:
```
pipenv install --dev
```

If you don't want to use pipenv, all package dependencies are listed in the
file `Pipfile`. Currently, these are:
* flask
* flask-cors
* pylint

You can install these packages with the python package management solution of your
choice (`pip`+`virtualenv`, `conda`, `poetry`, ...). Please use a tool and don't
just install random python packages with naked `pip`, though; it might be ok now
but something will break eventually.

#### VSCode Setup

If you are using VSCode, you should install the following plugins:
* [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

To make pipenv work with VSCode, you'll need to add this line to your `settings.json`:
```
"python.venvPath": "~/.virtualenvs",
```
Then enter `Ctrl-P` and select the command `Python: Select Interpreter`; from that
list, choose the one with "lug.cs.uic.edu-2018" in its name.

### Running

(Omit `pipenv shell` from all below instructions if not using Pipenv)

Powershell (Windows):

```posh
pipenv shell
$env:FLASK_ENV = 'development'
$env:FLASK_DEBUG = 1
flask run
```

Bash (MacOS and Linux):
```bash
pipenv shell
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
```
