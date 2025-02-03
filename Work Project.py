# Sviluppo Work Project by Samuele Di Fabio
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from tinydb import TinyDB, Query
from book import books



db= TinyDB('db.json')
app=Flask(__name__,static_folder='assets')
app.config['SECRET_KEY']= 'chiave_segreta'



#form di add-book
class AddBookForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired()])
    author= StringField('Autore', validators=[DataRequired()])
    year= StringField('Anno', validators=[DataRequired()])
    type= StringField('Genere', validators=[DataRequired()])
    isbn= StringField('ISBN', validators=[DataRequired()])
    submit= SubmitField('Aggiungi un libro')

#form di Registrazione
class RegistrationForm(FlaskForm):
    username = StringField('Il tuo Username', validators=[DataRequired(), Length(min=5, max=20)])
    email= StringField('Email', validators=[DataRequired(),Email(message='Email non valida')])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    submit= SubmitField('Registrati')



#form di Login
class LoginForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=5)])
    submit = SubmitField('Login')



@app.route('/')
def index():
    return "<h1>Work Project by Samuele</h1>"

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', books=books)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method== 'POST':
       print (request.form)
    form = RegistrationForm()
    print(form)
    if form.validate_on_submit():
        flash('Registrazione avvenuta con successo!', 'Success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Registrazione alla mia libreria', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login avvenuto con successo!', 'Success')
        return redirect (url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/books', methods=['GET', 'POST'])
def books():
    form = AddBookForm()
    if form.validate_on_submit():
        books(db, form.author.data, form.title.data, form.isbn.data, form.year.data, form.type.data)
        return redirect (url_for('home'))
        
    return render_template('books.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)

