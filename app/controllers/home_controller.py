from flask import render_template, send_file, url_for
import os

def index():
    return render_template('home/home.jinja')

def favicon():
    return send_file('static/favicon.ico')