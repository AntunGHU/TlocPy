# https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-a-development-environment

# How to use Fabric in a development environment
# Author: PFB Staff Writer
# Last Updated: August 27, 2020

# *******Overview*******
# I earlier wrote a post on "How to use Fabric in Python", which can be found here.
# I received a lot of responses from that article, so I decided to write another post about Fabric. This time I would like to focus on how to use it in a # development environment.

# *******What is Fabric?*******
# Just to recap what Fabric is
# Fabric is a Python (2.5 or higher) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.
# It provides a basic suite of operations for executing local or remote shell
# commands (normally or via sudo) and uploading/downloading files, as well as
# auxiliary functionality such as prompting the running user for input, or aborting execution.

# *******Why use Fabric in the development environment?*******
# So, we can use Fabric for streamlining the use of SSH for application deployment or systems administration tasks.
# In a development environment, where you have multiple servers with multiple people pushing the code multiple times per day, this can be very useful.
# If you would be the only person in the project who worked on a single server, a git pull (A git pull is what you would do to bring your repository up to date with # a remote repository) and start working with it.
# Often, you are not the only developer in a projet and there is where Fabric comes into the picture. To avoid logging into multiple servers and running remote # commands, we can use Fabric to automate this whole process.
# It can configure the system, execute commands on local/remote server, deploy your application, do rollbacks etc. A common practice when developing is to use Git # to deploy and Fabric to automate it.

# *******Fabric requirements*******
# An SSH server like OpenSSH needs to be installed on your server and an SSH client needs to be installed on your client.
# Fabric relies on the SSH Model, you can use SSH Keys but you can also control access to root via sudoers.
# The user on the server does not need to be added to "~/.ssh/authorized_keys", but if it is you don't have to type the password every time you want to execute a # command.
# If you ever have to disable the access to a user, just turn off their SSH account.
# There is no transfer of code, so you only need to have ssh running on the remote machine and have some sort of shell (bash is assumed by default).

# *******Fabric Installation*******
# First off, we will have to install it, that can be done through pip
# $ pip install fabric

# *******Fabric and Fabfile.py*******
# The installation added a Python script called "fab" to a directory in your path.
# This is the command Fabric will use when it logs into one or more servers.
# The fabile.py (see below) will be executed by the fab command.
# All fabric does at its core is execute commands locally and remotely.
# Fabric just provides a nice pythonic way of doing it.
# The fabile is what Fabric uses to to exectue task and we need to specify which shell commands we want Fabric to execute. In short, a fabfile is what controls what # Fabric executes.
# The commands that we put into the fabfile will be  executed on one or more hosts.
# Every fabric scripts need to be in a file called fabfile.py. These hosts can be defined either in the fabfile or on the command line.
# All the functions defined in this file will show up as fab subcommands.

# *******Fabric functions*******
# Fabric provides a set of commands in fabric.api that are simple but powerful,below are some of them
#     local	# execute a local command)
#     run	# execute a remote command on all specific hosts, user-level permissions)
#     sudo	# sudo a command on the remote server)
#     cd	# changes the directory on the serverside, use with the "with" statement)
#     put  	# uploads a local file to a remote server)
#     get 	# download a file from the remote server)
#     prompt	# prompt user with text and return the input (like raw_input))
#     reboot	# reboot the remote system, disconnect, and wait for wait seconds)
# One of the most common Fabric functions is run()
# It executes whatever command you put in as a parameter on the server.
# Below you can see an example.
# $ run("uptime")
# This will run the uptime command on any server that we specify in the fabfile.py.
# The server(s) are set using env.hosts:
# $ env.hosts = ['superuser@host1.example.com']
# This tells the script to use the username 'superuser' with the server address 'host1.example.com'
# Basically, it's just like ssh'ing into a box and running the commands you've put into run() and sudo(), but Fabric allows you to use several more calls.

# *******Setting up the development environment*******
# Before we start with creating Fabric functions, I want to show an example of how a directory structure may look like:
# $ mkdir /var/www/yourapplication
# $ cd /var/www/yourapplication
# $ virtualenv --distribute env
# Before we can do anything, we first need to create a fabile.py.
# If you are located in the same directory as "fabfile.py" you can go "fab --list" to see a list of available commands and then "fab [COMMAND_NAME]" to execute a # command.
# Now when everything is setup and we have an fabfile.py, let's put something in it.
# Let's first start defining roles and then specify what action to do.
# Lx from fabric.api import *
# Lx # Define sets of servers as roles
# Lx env.roledefs = {
# Lx     'www': ['www1', 'www2', 'www3', 'www4', 'www5'],
# Lx     'databases': ['db1', 'db2']
# Lx }
# Lx # Set the user to use for ssh
# Lx env.user = 'fabuser'
# Lx # Restrict the function to the 'www' role (that we created above)
# Lx @roles('www')
# Lx def uptime():
# Lx     run('uptime')
# If we now want to see the uptime on all our web-servers, all we have to do is run:
# $ fab -R www
# # To run uptime on both roles (www and databases);
# $ fab uptime
# Any function you write in your fab script can be assigned to one or more roles.
# You can also include a single server in multiple roles.
# So this is nice, Fabric makes it really easy to run commands across sets of
# machines.

# *******Deployment using Fabric*******
# Let's see now how we can deploy something with Fabric. Often, we want to create more than one function, depending on how your environment looks like (live, # staging, dev)
# Lx env.roledefs = {
# Lx     'hostsDev': ['dev1', 'dev2'],
# Lx     'hostsStaging':[ 'stg1', 'stg2'],
# Lx }
# Lx
# Lx @roles('hostsDev')
# Lx
# Lx def deploy_dev():
# Lx
# Lx   # Specify the path to where your codebase is located
# Lx   path = "/home/fabuser/codebase"
# Lx
# Lx   # Get the code from Github
# Lx   run ("git clone https://www.github.com/user/repo.git")
# Lx
# Lx @roles('hostsStaging')
# Lx
# Lx def deploy_staging():
# Lx     # do something
# If you now want to do a git clone to your development servers, all you need to do is use the fab command:
# $ fab deploy_dev
# That's how you can create a deploy function using Fabric.

# *******Virtualenv and Requirements*******
# Now we have cloned our code from the Github repository. That is nice, but we can do more, we can also install the requirements into a virtual environment.
# For those of you that don't know what "requirements" is;
# It's basically a file called requirements.txt which contain a list of packages to install.
# Instead of running something like pip install MyApp and getting whatever libraries come along, you can create a requirements file that includes all dependencies.
# Example of a requirements.txt file
#     BeautifulSoup==3.2.0
#     python-dateutil==1.4.1
#     django==1.3.0
#     django-debug-toolbar==0.8.5
#     django-tagging==0.3
#     Markdown==2.0.1
# ...
# ...
# To install all packages that are in that file, simple type
# $ pip install -r requirements.txt
# A virtual environment can be created with /bin/virtualenv 'app_name' and
# activated by typing source /bin/activate

# *******Use Fabric to install packages from requirements.txt*******
# Having that information, let's create a Fabric script to install it.
# Lx # Import the module
# Lx from fabric.api import *
# Lx
# Lx # Specify the user and host
# Lx env.hosts = ['fabuser@host1.example.com']
# Lx
# Lx def deploy():
# Lx      with cd("/home/fabuser/codebase/"):
# Lx
# Lx           run("git clone https://github.com/user/repo.git")
# Lx
# Lx      run("source /home/fabuser/codebase/venv/bin/activate && pip install -r /path/to/requirements.txt")
# That small script will activate the virtual environment and install all packages specified in the requirements.txt file.
# Sample output
# Downloading/unpacking BeautifulSoup==3.2.0 ....
#   Downloading BeautifulSoup-3.2.0.tar.gz
#   Running setup.py egg_info for package BeautifulSoup
# ...
# ...
# ...
# Storing complete log in /home/fabuser/.pip/pip.log

# *******Use Fabric to restart Apache servers*******
# We can use Fabric for many other things, we can also create a Fabric script for restarting our Apache servers.
# That would look something like this
# Lx from fabric.api import *
# Lx
# Lx env.hosts = ['superuser@host1.example.com:22']
# Lx
# Lx def restart_apache2():
# Lx     sudo('service apache2 restart')
# To restart apache2 on host 'host1.example.com', the only thing we have to do is
# $fab restart_apache2

# *******Use Fabric to send emails*******
# We aren't limited to hosts in "roledefs", we could also for example put in email addresses.
# Lx from fabric.api import env, run
# Lx # Define sets of email addresses as role
# Lx env.roledefs = {
# Lx     'test': ['localhost'],
# Lx     'dev': ['user@dev.example.com'],
# Lx     'staging': ['user@staging.example.com'],
# Lx     'production': ['user@production.example.com']
# Lx }
# Lx def deploy():
# Lx     run('echo test')
# To run it a specific role use the -R switch
# $ fab -R test deploy
# [localhost] Executing task 'deploy'
