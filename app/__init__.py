import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


if __name__ == '__main__':
    app.run(host='127.0.0.1')

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/aboutSebas')
def sebasPage():
    return render_template('sebastian.html', url=os.getenv("URL"))

@app.route('/aboutSally')
def sallysProfile():
    return render_template('sally.html', url=os.getenv("URL"))