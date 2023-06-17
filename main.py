# main.py
from fraskr import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from fraskr.user import User
from fraskr.classform import LoginForm, RegisterForm
import sqlite3

DATABASE = 'database.db'

@app.route("/")
def index():
    return redirect(url_for('app.login')) #login.htmlは一時的

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.username.data
        )
        DATABASE.session.add(user)
        DATABASE.session.commit()
        flash('registered correctly!')
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('app.index'))
            else:
                flash('Invalid password.')
                return redirect(url_for('app.login'))
        else:
            flash('The username is not registered.')
            return redirect(url_for('app.login'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.login'))
