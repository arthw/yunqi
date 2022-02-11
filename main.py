import flask
from flask import Flask, jsonify, render_template, request
import os
import sys

app = Flask(__name__)

@app.route('/')
def homepage():    
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)