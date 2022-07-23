# 35'39 indija 2020
# ime videa: Python: How to use Pip, Virtualenv, Virtualenvwrapper and Pipenv on Ubuntu 20.04

# link: Python: Install Virtualenv and Virtualenvwrapper; 2 years ago By Arulmurugan Rajaraman   0 comments;  python virtualenv dev virtualenvwrapper

# * Virtualenv
# Virtualenv is the package with which you can create mutilple isolate python development environments. Every every will have their own site-packages andm environment variables.

# Install virtualenv:# Install Virtualenv using the command
# ? sudo pip3 install virtualenv

# Create virtual environment: Create virtualenv using the command
# ? virtualenv venv_name

# Activate virtual environment: You can activate the virtualenv using the command
# ? source venv_name/bin/activate
# If you see (venv_name) at the beginning of your bash prompt, it denotes the active virtual environment.
# After activating a virtual environment, all the python packages you install will be installed in the virtual environment instead of your system's global python installation. You can create multiple virtual environments and install multiple versions of the same package in each virtual environment.
# But we are not done yet. There are some limitations and rules in using this. You have to be in the virtual environment directory to create and activate virtual environments.

# link-tekst: Python: Install Pip and Pipenv; # 2 years ago By Arulmurugan Rajaraman   0 comments; # python pip pipenv ubuntu venv

# When you are into development using Python, you should know how to manager packages and virtual environments. Pip is the package installer in Python and you can use it to install packages from Python Package Index.
# If you want to use different versions of a same package in your system, you need to create virtual environments. There are mutiple ways to do that. In this guide, let's see how to use Pipenv

# Versions Used
# Ubuntu - 20.04
# Python - 3.8.2
# Pip - 20.2.3
# Pipenv - 2020.8.13

# * Pip
# Pip can be used to install and manage packages which are not part of the standard Python installation. Let's see how to use # install and use it now.

# Installation: To install pip in your system, open the terminal and type the command
# ?  sudo apt install python3-pip
# Install python packages: To install a python package using pip, use the command
# ? pip3 install <package_name>
# For example, to install the latest version of Django you can use the command
# ? pip3 install django
# If you want to install a specific version of a package that is possible too. For example, to install version 2.1.1 of Django you # can use the command
# ? pip3 install django==2.1.1
# List installed python packages: To see the list of Python packages installed in your system, use the command
# ? pip3 list
# This will print the list of packages installed in your system along with their versions. The output will be similar to the one # given below.
# Package         Version
# --------------- ----------
# appdirs         1.4.3
# beautifulsoup4  4.9.1
# blinker         1.4
# CacheControl    0.12.6
# certifi         2019.11.28
# chardet         3.0.4
# colorama        0.4.3

# If you want to see if any of the packages are outdated, use the command
# ? pip3 list -o
# This will print the list of packages which can be updated along with the current installed version and the latest version. You can also use the command pip3 list --outdated. Example output is given below.
# Package     Version    Latest      Type
# ----------- ---------- ----------- -----
# appdirs     1.4.3      1.4.4       wheel
# certifi     2019.11.28 2020.6.20   wheel
# contextlib2 0.6.0      0.6.0.post1 wheel
# distlib     0.3.0      0.3.1       wheel
# distro      1.4.0      1.5.0       wheel
# html5lib    1.0.1      1.1         wheel
# idna        2.8        2.10        wheel

# Freeze requirements: To share the list of packages of your project with others or to push the list to a server, you can use the freeze command as given below
# ? pip3 freeze > requirements.txt
# When you run this command, the list of installed packages will captured in the file requirements.txt in the requirements format. The content of the file will be similar to the one given below (bez tocaka)
# ..... appdirs==1.4.3
# ..... beautifulsoup4==4.9.1
# ..... blinker==1.4
# ..... CacheControl==0.12.6
# ..... certifi==2019.11.28
# ..... chardet==3.0.4
# ..... colorama==0.4.3

# You can install requirements from a file using the command
# ? pip3 install -r requirements.txt
# Note that requirements.txt is the commonly used file name for capturing the package list. But you can also use the file name of your choice.

# Help menu: To see the help menu of Pip, use the command
# ? pip3 --help
# To see the help menu of a specific command, for example, install command
# ? pip3 install --help

# * Pipenv
# Pipenv can be used to create virtual environments in Python. If you want to use multiple versions of a same Python package in your system, virtual environments are the way to do it. Virtual enviroments can be created and used using multiple methods. Pipenv is one of the easiet ways to do it.

# Install pipenv: Install pipenv using the command
# ? sudo pip3 install pipenv

# Create virtual environment: To create a virtual environment using pipenv, install a package using the command pipenv install <package_name>. For example, to # install django
# ? pipenv install django
# This will create an virtual environment and install the specified package.

# Specify python version: To create a virtual environment using specific version of Python, use the command pipenv --python <version>. For example
# ? pipenv --python 3.6

# Install requirements: If you have a requirements file, you can install it using the command
# ? pipenv install -r requirements.txt

# Install specific version of a package: You can use pipenv install <package_name>==<version> to install a specific version of a package. To install Django 2.1.1, use the command
# ? pipenv install django==2.1.1

# Install dev packages To install packages which will be used only in development environments pass the --dev parameter in the install command. For example
# ? pipenv install django-debug-toolbar --dev

# A file named pipfile will be created in your project directory after you create the virtual environment. The file content will be similar the one given below

# [[source]]
# url = "https://pypi.python.org/simple"
# verify_ssl = true
# name = "pypi"
#
# [dev-packages]
# django-debug-toolbar = "*"
#
# [packages]
# django = "==2.1.1"


# Activate virtual environment: To activate a virtual environment, use the command
# ? pipenv shell

# Remove virtual environment: To remove a virtual environment, use the command
# ? pipenv --rm
