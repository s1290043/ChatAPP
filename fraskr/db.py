import sqlite3

chat_DATABASE = 'chatdatabase.db'
user_DATABASE = 'userdatabase.db'

def create_chat_table():
    con = sqlite3.connect(user_DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS chatLogs (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT)")
    con.close()

def creat_user_table():
    con = sqlite3.connect(user_DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS chatLogs (username, email, password)")
    con.close()