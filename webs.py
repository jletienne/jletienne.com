from flask import Flask, render_template,request, redirect, url_for
from cool_projects.movies import *
from cool_projects.shopping import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/lights')
def lights():
    return render_template('projects/lights.html')

@app.route('/films')
def films():
    return render_template('projects/films.html', movie=request_movie())

@app.route('/shopping')
def shopping():
    return render_template('projects/shopping.html', asics=asics(), jcrew=jcrew())



if __name__ == '__main__':
    #app.debug = True
    app.run()
