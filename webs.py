from flask import Flask, render_template,request, redirect, url_for
from cool_projects.movies import *
from cool_projects.shopping import *
from cool_projects.apple import *
from cool_projects.cassel import *
from cool_projects.chomba import *
from cool_projects.roundup import *
from cool_projects.nfl_draft import *


app = Flask(__name__)
app.config.from_object(__name__)

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



@app.route('/teams/<team>')
def teams(team):
    date = getNextEvent(team=team.title())
    return render_template('teams/{}.html'.format(team), eventInfo=eventInfo(team=team.title(), date=date), teamInfo=teamInfo(team.title()))

@app.route('/nfl-draft-stars')
def nfl():
    return render_template('projects/nfl-draft-stars.html', pageInfo = nfl_draft())

@app.route('/nfl-draft-star', methods=['POST', 'GET'])
def nfls():
    incoming_picks=request.form['incoming_picks']
    outgoing_picks=request.form['outgoing_picks']
    return render_template('projects/nfl-draft-stars.html', pageInfo = nfl_draft(incoming_picks=incoming_picks, outgoing_picks=outgoing_picks))




if __name__ == '__main__':
    app.debug = True
    app.run()
