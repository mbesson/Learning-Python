# Understanding third party packages

# What's already there? pip is the primary installer
# pip3 install (--user) mymodule
# pip3 freeze to se what do you have
# pip3 list
# pip3 freeze > requirements.txt
# pip3 install --user -r requirments.txt

# every project as acess to this packages -> could lead to problems

# virtual env sandbox
 # mkdir ~/venvs
 # python3 -m venv ~/venvs/pg
 # source ~/venvs/pg/bin/activate
 # which python
 # which pip
 # pip3 install psycopg2
 # deactivate

# A more modern tool : Pipenv

# pip3 install --user pipenv
# cd ~
# mkdir database
# cd database
# pipenv --python python3
# ls 
# pipenv shell
# pipenv install pandas
# exit