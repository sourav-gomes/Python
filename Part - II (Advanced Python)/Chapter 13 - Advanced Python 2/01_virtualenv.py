## Virtual Environment: An environment which is same as System Interpretor but is isolated from the other system environment(s) on the system

# $ pip freeze > requirements.txt       # To note the existing environment

# $ pip install virtualenv              # Command to install virtual environment in system

# $ virtualenv myprojectenv     # Create a virtual environment named 'myprojectenv'
# Immediately a 'myprojectenv' folder gets created. If you delete the folder the virtual envronment is deleted

# NB: Learn from https://www.digitalocean.com/community

## How to Activate your virtual environment?

# $ source myprojectenv/bin/activate        # For Linux/Mac users
# (myprojectenv) joseph@jsg-lpt:~/Downloads/python$     # NB: When virtual environment is activated (<virtualenv_name>) shows at the begining of the line

# $ .\myprojectenv\Scripts\activate.ps1     # For Windows users
# Sometimes it throws an error in Windows like... 'running scripts is disabled' (can google it)
# $ Set-ExecutionPolicy Unrestricted -Force     # Solution to 'running scripts is disabled' error

## Now you can install packages like flask & pygame in your virtual environment

# $ pip install flask
# $ pip install pygame

## Now when you run the 'pip freeze' command it will show all packages installed in virtualenv
# (myprojectenv) $ pip freeze
# click==8.0.1
# Flask==2.0.1
# itsdangerous==2.0.1
# Jinja2==3.0.1
# MarkupSafe==2.0.1
# pygame==2.0.1
# Werkzeug==2.0.1

# (myprojectenv) $ pip freeze > requirements1.txt       # To copy the existing environment package details to a file


# (myprojectenv) $ deactivate       # To deactivate virtual environment 'myprojectenv'
# $                       # Returns back from virtual environment to System Interpreter


# The following 2 commands will NOT run from System Interpreter and give 'ModuleNotFoundError'. But it will run & NOT give any error if we run it from Virtual env

# import flask
# import pygame


# $ pip install -r requirements1.txt      # To import a virtual environment from requirement.txt file
# So you can always share the requirement.txt file to anyone who wants to import the environment
