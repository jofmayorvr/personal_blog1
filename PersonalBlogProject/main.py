from flask import Flask
from markupsafe import escape
from flask import render_template
import datetime



app = Flask(__name__)

@app.route('/')
def index():
    year = datetime.date.today().year
    return render_template('index.html', year=year)

@app.route('/iletisim')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)