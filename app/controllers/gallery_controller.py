import json
from flask import render_template, request, redirect
import requests
from flask_login import current_user
from app import db
from app.models.favourite import Favourite
from app.models.user import User


API_KEY = "sa63K3JQBuY23fdtPM5Ub7JMFXyEilI8H6d72pMx"

def fetch_photos(args):
    res = requests.get(
        f"https://api.nasa.gov/mars-photos/api/v1/rovers/{args['rover']}/photos",
        params={'earth_date' : args['date'], 'camera' : args['camera'], 'api_key' : API_KEY}
    )
    return res.json()

def main_page():
    response = {"photos" : []}
    if len(request.args) == 3:
        response = fetch_photos(request.args)
    return render_template('home/gallery.jinja', images=response["photos"], req=request)

def user_collection():
    if not current_user.is_authenticated:
        return redirect('/auth/login/')

    favourites = Favourite.query.filter_by(user=current_user).all()
    favourites = [json.loads(fav.json_data.replace("'", '"')) for fav in favourites]

    response = {"photos" : favourites}
    if len(request.args) == 3:
        response = fetch_photos(request.args)

    return render_template('home/favourites.jinja', images=response["photos"])

def add_favourite():
    if not current_user.is_authenticated:
        return redirect('/gallery/main')

    print(current_user)

    favourite = Favourite(
        json_data = f"{request.get_json()}",
        user = current_user
    )

    db.session.add(favourite)
    db.session.commit()

    return redirect('/gallery/main')

