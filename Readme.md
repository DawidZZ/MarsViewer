## Before starting the App make sure that all packages are installed!
# It is reckommended to install packages in venv

> python -m venv venv
> venv\Scripts\activate (windows)
> pip install -r requirements.txt

# Database needs to be created before starting the App

> python

> from app import db
> db.create_all()

# Starting the app

in the root directory:

> python mars_viewer.py
