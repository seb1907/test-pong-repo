from django.shortcuts import render
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
   return render_template('open_me.html')

@app.route("/easy")
def easy():
    return render_template('easy.html')
@app.route('/hard')
def hard():
    return render_template('hard.html')

if __name__ == "__main__":
   app.run( debug=True ,port=5000)