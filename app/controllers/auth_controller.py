from flask import render_template, redirect, flash, request
from app.forms import LoginForm, RegistrationForm
from app.models.user import User
from app import db
from flask_login import login_user, current_user, logout_user, login_required

def login():
    if current_user.is_authenticated:
        return redirect('/')
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if( user and user.verify_password(form.password.data)):
            login_user(user)
            flash(f'Udało Ci się zalogować jako: {current_user.username}', 'success')
            return redirect('/')
        flash('Coś poszło nie tak!', 'danger')
        return redirect('/auth/login/')
    return render_template("auth/login.jinja", form=form)

def register():
    if current_user.is_authenticated:
        return redirect('/')
    
    form = RegistrationForm()
    if request.method == 'POST' and not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in the {getattr(form, field).label.text} field - {error}", 'danger')
        
        return redirect('/auth/register/')
    
    if request.method == 'POST' and form.validate():
        user = User(username = form.username.data, 
                    email    = form.email.data, 
                    password = form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Zarejestrowano pomyślnie', 'success')
        except:
            flash('Coś poszło nie tak!', "danger")
            return redirect('/auth/register/')
        return redirect('/auth/login/')

    return render_template("auth/register.jinja", form=form)


def logout():
    if not current_user.is_authenticated:
        return redirect('/')

    logout_user()
    flash('Wylogowano pomyślnie', 'success')
    return render_template("home/home.jinja")