"""
By: Jessica Angela Campisi
Date: 10/30/2019
Purpose: Create a web service that displays a chuck norris quote in html
"""

from flask import Flask
from thechuck import get_chuck
from mystory import Story

app = Flask(__name__)

@app.route('/')
def home():
    #return "<h1> {} </h1>".format(get_chuck())
    myStory = Story()
    return myStory.returnStory()


if __name__ == "__main__":
    app.run(debug=True, port=8080)
