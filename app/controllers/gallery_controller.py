import re
from flask import render_template, request
import requests

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
    return render_template('home/gallery.jinja', images=response["photos"])

def user_collection():
    response = {"photos" : []}
    if len(request.args) == 3:
        response = fetch_photos(request.args)
    return render_template('home/gallery.jinja', images=response["photos"])