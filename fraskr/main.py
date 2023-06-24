from fraskr import app, db, login_manager
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from fraskr.classform import LoginForm, RegisterForm
from fraskr.user import User

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,            
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Your info is registered correctly!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

