from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask('webapp')
URL = 'https://worldpopulationreview.com/country-rankings/maternity-leave-by-country'  #week 9, lab 2 ex 2
page = requests.get(URL)
soup = BeautifulSoup(page.content)

@app.route('/')     #week 9, lab 1 ex 2
def home():
    return soup.prettify() 


if __name__ == '__main__':
    app.run(debug=True)