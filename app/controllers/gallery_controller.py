from flask import render_template, request
from requests import get

response = get(
    "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos",
    params={'sol': 2, 'api_key' : 'DEMO_KEY'}
)

res_json = response.json()
print(res_json["photos"])

def main_page():
    return render_template('home/gallery.jinja', images=res_json["photos"])

def user_collection():
    return render_template('home/gallery.jinja', images=res_json["photos"])