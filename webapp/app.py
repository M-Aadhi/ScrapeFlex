from flask import Flask, render_template, request
from scrape_flex.scraper import scrape_website

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        url = request.form['url']
        data = scrape_website(url)
    return render_template('templates/index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
