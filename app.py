from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder='templates')

  # a simple page that says hello
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)