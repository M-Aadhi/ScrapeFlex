from flask import Flask, render_template, request
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrape_flex.scraper import scrape_website

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        url = request.form['url']
        data = scrape_website(url)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
