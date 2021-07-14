from django.shortcuts import render
import sqlite3
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import UserModel

db = sqlite3.connect('users.db')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id PRIMARY_KEY,
    user_name TEXT,
    password TEXT
);""")


def reg(request):
    return render(request, 'login.html')

