
# Installation Step

Step 1 - Install the module
===========================

pip install chatterbot==1.0.4

pip install spacy

python -m spacy download en_core_web_sm

python -m spacy link en_core_web_sm en

pip install profanity_filter

pip install langdetect


Step 2 - Command to create user
================================

# Command to create user

go to examples/django_app

python manage.py migrate

python manage.py createsuperuser

Step 3 -  Test and Run the server
================================

go to examples/django_app

python manage.py runserver 0.0.0.0:8000

# Android App Download Below
https://drive.google.com/file/d/1WvaGH481KPkzh1ocRd1rPVDD3MP8J57Y/view?usp=sharing


# SQL Lite Issues
This is an issue with the included version of SQLite on CentOS 7 being quite old. Here's how I solved it, IIRC:
Upgrade the CentOS 7 system install of SQLite to 3.29 by compiling it from source. Download the source, and then be sure to ./configure --prefix=/usr to upgrade the system version. Then make and sudo make install. You must include the prefix or it'll install to /usr/local instead by default!
Make sure the system version installed is 3.29 with sqlite3 --version
Re-compile Python 3.7.x. Be sure to do a make clean before sudo make install if you've already installed it.
Open python3.7 and check the version. import sqlite3, followed by sqlite3.sqlite_version
That should work; the only difference is I installed from Python 3.6 from IUS Community. After upgrading the system SQLite, I did a sudo yum remove python36u then a sudo yum install python36u and the Python included SQLite had successful upgraded to 3.29.

pip install pysqlite


# How To Check SQL Lite Version
sqlite3 --version

# How to Check SQL Lite Version using Python
>>> import sqlite3 
>>> sqlite3.sqlite_version  

# Python Deployment Server path and run this to reinstall SQL Lite

cd /home/bayibot/Python-3.7.9

LD_RUN_PATH=/usr/local/lib ./configure --prefix=/usr   --with-openssl=/home/username/openssl
LD_RUN_PATH=/usr/local/lib make 
LD_RUN_PATH=/usr/local/lib make altinstall

# Deployment Server path
/home/bayibot/ChatterBot-master/examples/django_app

yum install openssl-devel libffi-devel

# Open SSL issues 
first install openssl, please refer to this page below
https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username

install python and ./configure --with-openssl=/home/username/openssl
at last, run python3 -m ssl and nothing outputs, it's ok.

# Other Bot Samples
https://www.elbot.com/

https://www.pandorabots.com/mitsuku/

# Command to start centos in screen

Below are the most basic steps for getting started with screen: This is to avoid server closed when quit the terminal or putty.

On the command prompt, type screen.
Run the desired program.
Use the key sequence Ctrl-a + Ctrl-d to detach from the screen session.
Reattach to the screen session by typing screen -r.
