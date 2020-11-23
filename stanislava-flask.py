from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask('webapp')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages_from_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<User {self.id} {self.name}>" 

@app.route('/')
def home():
    usrs = User.query.all()
    return render_template("home.html", users=usrs) 

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        un = request.form["name"]
        ms = request.form["message"]
        user = User(username=un, message=ms)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("contact.html")

import math
@app.route('/sqrt/<num>')
def squared_root_num(num):
    return str(math.sqrt(int(num)))

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Welcome to our web app!"


def show_the_login_form():
    return "This is an imaginary login form"
def do_the_login():
    return "This is a login form, which I will work on building :)"

from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
