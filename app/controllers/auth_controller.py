from flask import render_template

def login():
    return render_template("auth/login.jinja")

def register():
    return render_template("auth/register.jinja")