from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Zaloguj Się')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[validators.Length(min=4, max=25)])
    email = StringField('Email Address', validators=[validators.Length(min=6, max=35)])
    password = PasswordField('New Password', validators=[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Hasła muszą się zgadzać')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Zarejestruj Się")