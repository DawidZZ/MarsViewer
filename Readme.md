# Before starting the App make sure that all packages are installed and database is created!
## It is reckommended to install packages in venv

## Installing requirements

> python -m venv venv
> venv\Scripts\activate (windows)
> pip install -r requirements.txt

# Creating database

> python

> from app import db
> db.create_all()

# Starting the app

in the root directory:

> python mars_viewer.py
