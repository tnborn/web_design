# Main stuff
from flask import Flask, render_template

import requests

app: Flask = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/about_us")
def about_us():

    return 

if __name__ == '__main__':
    app.run(debug=True)