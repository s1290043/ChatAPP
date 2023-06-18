from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):

    username = StringField('Username')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')