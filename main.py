# main.py
from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3

DATABASE = 'database.db'

@app.route('/')# login
def index():
    
    return render_template(
        'login.html',
    )
