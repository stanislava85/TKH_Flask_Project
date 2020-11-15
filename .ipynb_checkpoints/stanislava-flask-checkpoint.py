from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask('webapp')
URL = 'https://worldpopulationreview.com/country-rankings/maternity-leave-by-country'  #lab 1 ex 3
page = requests.get(URL)
soup = BeautifulSoup(page.content)

@app.route('/')     #lab 1 ex 3
def home():
    return soup.prettify()  

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
    app.run(debug=True)