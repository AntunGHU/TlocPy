# https://www.pythonforbeginners.com/development/development-environment-in-python
# Development Environment in Python
# Author: PFB Staff Writer
# Last Updated: May 21, 2020


# ******Overview******
# Some of the steps needed to setup a development environment includes:
# Operating system 	- e.g Linux / Mac
# Project structure  	- project structure
# Virtualenv   		- isolated installation of the project
# Pip     		    - a tool for installing and managing Python packages
# Git     		    - source control
# Webserver     		- where we can manage our applications
# Fabric    		    - automated deployment#

# ******Project Structure******
# Create an empty top-level directory for our new project:
# $ helloflask/
# $     -static/
# $         -css
# $         -font
# $         -img
# $         -js
# $     -templates
# $     -routes.py
# Then cd into the directory
# $ cd helloflask

# ******Virtualenv******
# Many developers uses virtualenv (virtual environment) on their computer, which is useful when you want to run several applications on the same computer.
# Virtualenv will manage all dependencies and enables multiple side-by-side installations of Python, one for each project.
# It doesn't install separate copies of Python, but provides a way to keep different project environments isolated.
# If we want to run more than one (which is often the case) web application on that host, then you should really install 'Virtualenv'.
# If you don't use virtualenv , you will have it all globally installed.
# ***Installing Virtualenv
# Download and Install Virtualenv into a virtual environment
# # If you are using Linux/Mac:
# $ sudo pip install virtualenv
# ***Setup a new project
# Navigate to the directory you want your project in:
# $ virtualenv venv      		    # this creates the folder venv
# $ source venv/bin/activate    	# start working on your new project
# (venv)$ pip install Flask    	# installs Flask
# For more information on how to download install virtualenv, see this article.(https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv)

# ******Pip******
# PIP is a tool for installing and managing Python packages.
# PIP comes with a command-line interface, which makes installing Python software packages as easy as issuing one command
# ? pip install some-package-name
# Users can also easily implement the package's subsequent removal
# ? pip uninstall some-package-name
# Pip has a feature to manage full lists of packages and corresponding version numbers through a "requirements" file.
# This permits the efficient re-creation of an entire group of packages in a separate environment (e.g. another computer) or virtual environment.
# This can be achieved with a properly formatted requirements.txt file
# ? pip install -r requirements.txt
# This makes dependencies easy, you can create a requirements file based on a set of packages installed in your virtual environment.
# ? pip freeze > requirements.txt
# When deploying to a server it is important to register which requirements we need.
# The requirements file can be done automatically using the freeze command for pip.
# This command will generate a plain text file that contains the names of the required Python packages and their versions, for example Flask==0.9
# To do this we freeze the installed packages and store this setup in a requirements.txt file
# ? cat requirements.txt
# Flask==0.9
# Jinja2==2.6
# Werkzeug==0.8.3
# The requirements file can be used to rebuild a virtual environment or to deploy a virtual environment into the machine.

# ******Start coding******
# Now that we have a clean Flask environment to work in, we'll create our simple application.
# The simplest Flask App looks something like this:
# Put this code into the file and name it 'hello.py'
# ?  Lx from flask import Flask
# ?  Lx app = Flask(__name__)
# ?  Lx @app.route('/')
# ?  Lx def hello():
# ?  Lx     return 'Hello World!'

# ******Github – Central Repository******
# Now it's time to create the repository on Github. The purpose of setting up a Github project, is so that we can push files from our local computer to Github and then pull the files from Github to our web server.
# Create a new Github account and create a new project (helloflask)

# ******Git – Local Computer******
# By using a versioning system, we can store all our files in a Github repository.
# The first thing you need to do on your local computer is to install and setup git.
# ***Install Git
# To install git, simple run:
# ? sudo apt-get install git
# ***Setup Git
# Put in your username and email into the .gitconfig file (~/.gitconfig)
# ? git config --global user.name "pythonforbeginners"
# ? git config --global user.email pythonforbeginners@example.com
# ***Git Ignore
# Since our current directory contains a lof of extra files, we'll want to configure our repository to ignore these files with a .gitignore file:
# ? * venv
# ? *.pyc
# * Next, we’ll create a new git repository and save our changes. Initialize Git in our project directory
# ? git init
# This creates a git repository in the current directory.
# Add all of our files to our initial commit
# ? git add .
# Check the status, this will list all files
# ? git status
# With the files added to the Git index, we can now commit them to our repo:
# ? git commit -m 'Initial commit'
# Now we have created a local Git repository for our application (local) files.
# ***Setup Github as the origin
# ? git remote add origin git@github.com:USERNAME/helloflask.git
# ? git push -u origin master

# ******Web Server – Host******
# Now its time to start up the web server and do some configuration.
# If you want to use Apache as a web server, you can install it like this:
# ? sudo apt-get install apache2
# Configure a virtual host (vhost) in /etc/apache2/sites-available/siteX
# Install virtualenv just like you did on your local computer.
# Set up the environment for the website, here I use /var/www
# Cd into that folder and clone the project that you setup on Github, by typing:
# ? git clone git@github.com:USERNAME/helloflask.git
# Initialize and activate your virtualenv
# ? virtualenv helloflask
# ? cd helloflask
# ? source bin/activate
# ***Install dependencies
# ? pip install -r requirements.txt

# ******Fabric******
# Fabric is used for deployment. You can of course always manually upload the code and restart the web server to reflect the configuration changes.
# Using fabric in a development environment, where you have multiple servers with multiple people pushing the code multiple times per day, this can be incredible very useful.
# Fabric can configure the system, execute commands on local/remote server, deploy your application, do rollbacks etc.
# It does that by using its command-line utility that will run a fabfile containing instructions on how to deploy to a server.
# A common practice when developing is to use Git to deploy and Fabric to automate it.
# ***Install Fabric
# ? pip install fabric
# Fabric expects a fabfile named fabfile.py which defines all of the actions we can take.
# The fabfile.py should be in your project's root directory.
# I like to use this script that asks the server to pull from the git repository and restart apache.
# ? [source](https://yuji.wordpress.com/2011/04/09/# django-python-fabric-deployment-script-and-example/)
# ? Lx from fabric.api import *                        # import fabrics API functions
# ? Lx env.hosts = ['user@example.com:22']             # add the remote server information
# ? Lx def pushpull():
# ? Lx     local('git push')      		               # runs the command on the  local environment
# ? Lx     run('cd /path/to/project/; git pull')       # runs the command on the  remote environment
# ? #Run it with:
# ? $ fab pushpull
# For more information on how to use fabric in a development environment, please refer to this article(https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-a-development-environment).
