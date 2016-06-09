from flask import Flask, render_template,request, redirect, url_for
from cool_projects.movies import *
from cool_projects.shopping import *
from cool_projects.apple import *
from cool_projects.cassel import *
from cool_projects.chomba import *


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

@app.route('/movies')
@app.route('/films')
def films():
    return render_template('projects/films.html', movie=request_movie())

@app.route('/shopping')
def shopping():
    return render_template('projects/shopping.html', asics=asics(max_price=100), jcrew=jcrew(max_price=50))


@app.route('/shoppin', methods=['POST', 'GET'])
def shoppin():
    max_asics=int(request.form['max_asics'])
    max_jcrew=int(request.form['max_jcrew'])
    return render_template('projects/shopping.html', asics=asics(max_price=max_asics), jcrew=jcrew(max_price=max_jcrew))

    #return render_template('projects/shopping.html', asics=asics(max_price=request.form['max_asics']), jcrew=jcrew(max_price=request.form['max_jcrew']))

@app.route('/apple')
def apple():
    return render_template('projects/apple.html', apple=applebot())

@app.route('/casselz')
@app.route('/cassel-z')
def casselz():
    return render_template('projects/cassel-z.html', cassel=cassel(), cassel2=cassel2())

@app.route('/chombas')
@app.route('/chupacabras')
def chombas():
    date = getNextEvent(team='Chupacabras')
    return render_template('projects/chombas.html', eventInfo=eventInfo(team='Chupacabras', date=date), teamInfo=teamInfo('Chupacabras'))

@app.route('/cha-ching')
@app.route('/chaching')
def chaching():
    date = getNextEvent(team='Cha-Ching')
    return render_template('projects/cha-ching.html', eventInfo=eventInfo(team='Cha-Ching', date=date), teamInfo=teamInfo('Cha-Ching'))


@app.route('/orange')
def orange():
    date = getNextEvent(team='Orange')
    return render_template('projects/orange.html', eventInfo=eventInfo(team='Orange', date=date), teamInfo=teamInfo('Orange'))


if __name__ == '__main__':
    #app.debug = True
    app.run()
