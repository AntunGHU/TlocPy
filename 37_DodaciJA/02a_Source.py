# https://yuji.wordpress.com/2011/04/09/django-python-fabric-deployment-script-and-example/
# Yuji Tomita
# Yuji's Increasingly Infrequent Ramblings
# Django / Python – Fabric Deployment Script and Example
# Apr 09 2011


# *******Fabric*******
# I’d heard about it for at least a year+ but I never got around to it.
# I was a little intimidated by it.
# The examples seemed so simple, but that was the problem – they seemed too simple, like the examples you run into which look completely uninformative, just a quick blot of code and no explanation.
# Well, it turns out fabric really is just that magical.
# This is straight life changing!
# This is as useful as when I first discovered how much easier it was (for me) to use Git for branching / merging than SVN, or deciding to switch to a linux-like environment for web development.
# I’m writing about this today because I was always intimidated by it / thought it would take some time to learn, when there was no reason to be. It’s extremely simple.
# Hopefully, it helps somebody out there with the same reservations.
# First, let me point you to the official fabric docs where you can find the tutorial and more.(http://docs.fabfile.org/en/1.0.1/index.html)
# ***Install fabric.
# First, pip install fabric on each machine you need to use fabric on.
# ? pip install fabric
# ***Create the fab file that contains functions
# Create a blank file called fabfile.py in the directory you’d like to use the fabric commands from.
# For my django project, that’s the directory that contains settings.py and manage.py. My “home base”, or where you’ll find me in an average terminal window.
# ***Create your first fabric command
# In just a few lines of code, let’s set up a fabric script that asks the server to pull from the git repository and restart apache.
# Lx # import fabrics API functions - self-explanatory once you see
# Lx from fabric.api import *
# Lx def pushpull():
# Lx     local('git push')                        # runs the command on the local environment
# Lx     run('cd /path/to/project/; git pull')    # runs the command on the remote  environment
# Let’s try running that in bash.
# $ bash$ fab pushpull
# It will ask you for a server to connect to that’s running fabric. You will want to enter in your username@host:port here.
# Obviously, typing the full URL every time defeats the purpose of an automation script – let’s add it into our fabric file.
# ***Add remote server commands
# Let’s add the remote server information to our fabric file. We need to add our server information to our fabric script via the env.hosts parameter.
# Lx from fabric.api import *
# Lx env.hosts = ['me@example.com:22']
# Lx def pushpull():
#       local('git push') # runs the command on the local environment
#       run('git pull') # runs the command on the remote environment
# env is a dictionary containing various settings, one of which is ‘hosts’ – a list of hosts that all commands will run through.
# Now, if we run fab pushpull, we won’t need to type in the server name. If you have SSH keys set up, you won’t need a password.
# ***Add more server setup commands
# Next, I want support for working on a development server or production.
# Adding this information via a separate function ensures our commands are not tied to specific environments. For example, I use the same functions chained with # “dev” or “prod” to determine which environment I am applying the command towards.
# Okay, our first roadblock; it turns out that you can not dynamically set env.hosts within a function – it will not register.
# Lx def pushpull(host=None):
# Lx    env.hosts = [host] # this will fail
# Lx bash$ fab pushpull:me@example.com # fails
# You need to define it in a separate function. Here’s what I’ve done.
# I’ve set up a “dev” and “prod” function that sets up the environment prior to running another fab command. For good measure, I also created an “all” command.
# Lx dev_sever = 'me@dev.example.com:22'
# Lx prod_server = 'me@example.com:22'
# Lx
# Lx def dev():
# Lx    """ Use development server settings """
# Lx    env.hosts = [dev_server] # this is the place to add other setup, such as if the django project is in a different directory
# Lx    # reference this variable later
# Lx    env['dir'] = '/path/'
# Lx
# Lx
# Lx def prod():
# Lx    """ Use production server settings """
# Lx    env.hosts = [prod_server]
# Lx
# Lx
# Lx def all():
# Lx    """ Use all serves """
# Lx    env.hosts = [dev_server, prod_server]
# Now, we can run the command.
# $ bash$ fab dev pushpull bash$ fab prod pushpull bash$ fab all pushpull
# Wow, amazing. The possibilities already are limitless!
# ***Some tips – reuse functions.
# I’ve found that writing many small functions helps since I’m not always using fabric.
# For example, I have a large, full deployment function that…
#     commits local changes
#     pushes the changes
#     pulls the changes on the remote machine
#     syncdbs the remote machine
#     migrates the remote machine
#     restarts apache and other servers
# Now, each one of these functions is actually another separate function, since who knows, I might have committed my changes myself and even pushed changes and now # I only need a server restart – for me that’s “fab prod deploy”
# ***Passing arguments to fabric functions.
# Functions can accept arguments, and are passed to the python functions from the shell via a colon
# $ bash$ fab dev some_func:arg1,arg2,keyword=kwarg
# ***Preventing errors from blowing up
# Any non success exit code will stop your function. Use the settings function from the api to allow them to silently pass.
# For example, git commit -a will fail if there’s nothing to add.
# Lx def foo():
# Lx     with settings(warn_only=True):
# Lx         local('git commit -a') # fabric will no longer abort
# ***Keep functions open-ended via *args
# There are tons of special case scenarios with django-south and its commands, so I’ve made a migrate fabric command that accepts an arbitrary number of arguments, # to support say migrate myapp 0001 —fake
# Lx def migrate(*args):
# Lx     with cd(env['mypath']): # every command will now be run in the path specified
# Lx         run('python manage.py migrate ' + ' '.join(args))
# $ bash$ fab dev migrate:--all,--fake,0001
# ***Define a way to revert a mistake
# Make sure you have a way out of an operation that kills your site.
# In my case, I have set up a git revert command as “revert”
# Lx def revert():
# Lx     """ Revert git via reset --hard @{1} """
# Lx     with cd(env['dir']):
# Lx         run('git reset --hard @{1}')
# Lx         arestart() # restarts server
# This command would undo the last pull to the working state the server should have been in before we forced a pull.
# ***Use docstrings
# The first line of your docstring appears when you list your fab functions via fab –list
# ***One final note:
# Check the docs. There are functions such as sudo(‘myfunc’) that will run as root. Very useful
