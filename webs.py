from flask import Flask, render_template,request, redirect, url_for
from cool_projects.movies import *
from cool_projects.shopping import *
from cool_projects.apple import *
from cool_projects.cassel import *
from cool_projects.chomba import *
from cool_projects.roundup import *
from cool_projects.nfl_draft import *
from cool_projects.nba_draft import *
from cool_projects.sslify import SSLify
from cool_projects.football_expectations import football_expectation
import pandas as pd

app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
sslify = SSLify(app)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/arduino-wifi-smart-lights')
def lights():
    return render_template('projects/lights.html', title = 'Smart Lights Project')

@app.route('/lights')
def lights_rdr():
    return redirect("/arduino-wifi-smart-lights", code=301)

@app.route('/films')
def films():
    return render_template('projects/films.html', movie=request_movie(), title="RTB Films")

@app.route('/movies')
def films_rdr():
    return redirect("/films", code=301)

@app.route('/automated-personal-shopper', methods=['POST', 'GET'])
def shopping():
    title = 'Automated Personal Shopper by Jean-Luc Etienne'
    if request.method == 'POST':
        max_asics=int(request.form['max_asics'])
        #max_jcrew=int(request.form['max_jcrew'])
        #return render_template('projects/shopping.html', asics=asics(max_price=max_asics), jcrew=jcrew(max_price=max_jcrew), title='Shopping Spider')
        return render_template('projects/shopping.html', asics=asics(max_price=max_asics),jcrew=None, title=title)
    return render_template('projects/shopping.html', asics=asics(max_price=100),jcrew=None, title=title)

@app.route('/shopping')
@app.route('/shoppin')
@app.route('/shopping-spider')
def shop_spy():
    return redirect("/automated-personal-shopper", code=301)

@app.route('/apple')
def apple():
    return render_template('projects/apple.html', apple=applebot(), title="Apple")


@app.route('/sports-team-calendars')
def sports_calendars():
    return render_template('teams/sports-team-calendars.html', title="Sports Team Calendars")

@app.route('/teams/<team>')
def teams(team):
    date = getNextEvent(team=team.title())
    return render_template('teams/zteams.html', eventInfo=eventInfo(team=team.title(), date=date), teamInfo=teamInfo(team.title()))

@app.route('/nfl-draft-trade-calculator', methods=['POST', 'GET'])
def nfl():
    if request.method == 'POST':
        # do your work here
        incoming_picks=request.form['incoming_picks']
        outgoing_picks=request.form['outgoing_picks']
        return render_template('projects/nfl-draft-stars.html', pageInfo = nfl_draft(incoming_picks=incoming_picks, outgoing_picks=outgoing_picks), title="NFL Draft Trade Calculator")
    return render_template('projects/nfl-draft-stars.html', pageInfo = nfl_draft(), title="NFL Draft Trade Calculator")

@app.route('/nfl-draft-star')
@app.route('/nfl-draft-stars')
def nfl_rd():
    return redirect("/nfl-draft-trade-calculator", code=301)


@app.route('/football-expected-wins-calculator', methods=['POST', 'GET'])
def football_expected_wins():
    if request.method == 'POST':
        points_for=int(request.form['points_for'])
        points_against=int(request.form['points_against'])
        return render_template("projects/football-expected-wins-calculator.html", pageInfo = football_expectation(points_for=points_for, points_against=points_against), title="Football Expected Wins Calculator")
    return render_template("projects/football-expected-wins-calculator.html", pageInfo = football_expectation(), title="Football Expected Wins Calculator")


@app.route('/nba-draft-trade-calculator', methods=['POST', 'GET'])
def nba():
    if request.method == 'POST':
        incoming_picks=request.form['incoming_picks']
        outgoing_picks=request.form['outgoing_picks']
        return render_template('projects/nba-draft-stars.html', pageInfo = nba_draft(incoming_picks=incoming_picks, outgoing_picks=outgoing_picks), title="NBA Draft Trade Calculator")
    return render_template('projects/nba-draft-stars.html', pageInfo = nba_draft(), title="NBA Draft Trade Calculator")

@app.route('/nba-draft-star')
@app.route('/nba-draft-stars')
def nba_rd1():
    return redirect("/nba-draft-trade-calculator", code=301)

@app.route('/sitemap')
def site_map():
    return render_template('sitemap.xml', title='Sitemap')

@app.route('/referral_test')
def referral_test():
    return render_template("referral_test.html")

@app.route('/links')
def links():
    return render_template("links.html")

@app.route('/football')
def football_redirect():
    return redirect("/jean-luc-etienne-football", code=301)

@app.route('/jean-luc-etienne-football')
def football():
    return render_template("jean-luc-etienne-football.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/test_squarespace')
def checkout():
    return render_template("test_squarespace.html")

@app.route('/count')
def days_count():
    from datetime import datetime, timedelta, date  
    days_since = date.today() - date(2024,8,12)
    return render_template("count.html", days_since=days_since)

@app.route('/last')
@app.route('/recent')
def last_recent_tracks():
    tracks = pd.read_csv('archive/dope_recent_tracks.csv')
    return render_template("last_recent_tracks.html", data=tracks.to_dict(orient='records'))

@app.route('/music_creation')
def music_creation():
    return render_template("music/music_creation.html")

#@app.route('/j30')
#def j30():
#    return render_template("j30_notebook.html")

@app.route('/callback')
def callback():
    return render_template("callback.html")



@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')



if __name__ == '__main__':
    app.debug = True
    app.run()
