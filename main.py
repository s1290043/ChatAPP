# main.py
from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3

DATABASE = 'database.db'

@app.route('/')
def index():
    
    return render_template(
        'index.html',
    )
