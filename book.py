from tinydb import TinyDB
from flask_wtf import FlaskForm



db= TinyDB('db.json')


def books(db,isbn,author,title,type,year):
    db.insert({
        'isbn':isbn,
        'author':author,
        'title':title,
        'type':type,
        'year':year,
        'status':'available'         })