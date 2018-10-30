# lug.cs.uic.edu-2018
------------------------------------------------------------------
* Project Oversight: LUG President Bennett Maciorowski
* Project Lead/Manager: Joshua Castor
* Project BackEnd Lead: Will Toher
* Project Deployment: Bharat Middha (LUG VP/SysAdmin)
* Project FrontEnd Lead: Joshua Castor 
  
# Backend Server

The backend server is based on **Python 3.7.x**, using the **Flask** framework.

## Installation

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

### VSCode Setup

If you are using VSCode, you should install the following plugins:
* [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

To make pipenv work with VSCode, you'll need to add this line to your `settings.json`:
```
"python.venvPath": "~/.virtualenvs",
```
Then enter `Ctrl-P` and select the command `Python: Select Interpreter`; from that
list, choose the one with "lug.cs.uic.edu-2018" in its name.

## Running

(Omit `pipenv shell` from all below instructions if not using)

Powershell (Windows):

```posh
pipenv shell
$env:FLASK_APP = 'server.py'
$env:FLASK_ENV = 'development'
flask run
```

Bash (MacOS and Linux):
```bash
pipenv shell
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
```
