import requests
import sys, os
import json
import re
import datetime
import calendar


def addEvent(start_time = '10 pm', location = 'location', opponent = 'Opponent',year=3000, month=1, day=1, team='None'):
    event_date = datetime.date(year, month, day)
    gameday = str(event_date)
    weekday = calendar.day_name[event_date.weekday()]

    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Events/{}.json'.format(team, gameday)
    players = getPlayers(team)

    gameinfo = {
                    'Start_Time': start_time,
                    'Location': location,
                    'Opponent': opponent,
                    'Players': players,
                    'Date': '{:%b %d, %Y}'.format(event_date),
                    'Date2': gameday,
                    'Weekday': weekday,
                }

    r = requests.put(URL, data=json.dumps(gameinfo))
    return URL

def getPlayers(team):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Players.json'.format(team)
    r = requests.get(URL).json()

    return r

def make_regex(x):
    ips = x
    products = "".join(ips)
    return products

def html_source(URL):
    return requests.get(URL).text

def add_allen_team(my_team='Red', location='Allen Hockey Rink', URL=None):

    game_times = re.findall(make_regex(['<td>(.*)</td>']), html_source(URL))
    game_dates = re.findall(make_regex(['<td class="text-center">(.*?)</td>']), html_source(URL))

    regex2 = r'<td class=\\"text-left\\"><a href(.*)</a>'
    home_team1 = re.findall(make_regex([regex2]), html_source(URL))
    home_team2 = re.findall(make_regex(['<tr><td class="text-left"><span class="highlight"></span><a href(.*)</a>']), html_source(URL))

    away_team1 = re.findall(make_regex(['<td class="text-left"><a href(.*)</a>']), html_source(URL))
    away_team2 = re.findall(make_regex(['([^<tr>])<td class="text-left"><span class="highlight"></span><a href(.*)</a>']), html_source(URL))

    regex = r'>(.*)'

    away_teams = [re.findall(regex, str(i))[0] for i in away_team1 + [j[1] for j in away_team2]]
    home_teams = [re.findall(regex, str(i))[0] for i in home_team1 + home_team2]

    x = [[a[0]] + [a[1]] + [1*(a[2] != my_team)*a[2] + 1*(a[3] != my_team)*a[3]] for a in zip(game_times, game_dates, home_teams, away_teams)]

    for i in x:
        hockey_month = int(datetime.datetime.strptime('2018 ' + i[1].strip(), '%Y %a, %b %d').strftime("%m"))
        hockey_day = int(datetime.datetime.strptime('2018 ' + i[1].strip(), '%Y %a, %b %d').strftime("%d"))
        addEvent(start_time = i[0], location = location, opponent = i[2],year=2018, month=hockey_month, day=hockey_day, team=my_team)


if __name__ == "__main__":
    #print(incrementTrip('Black'))
    my_team = 'Red'
    location = 'Allen Hockey Rink'
    year = 2018
    URL = 'http://stats.pointstreak.com/players/print/players-team-schedule.html?teamid=709641&seasonid=17484'
    add_allen_team(my_team=my_team, location='Allen Hockey Rink', URL=URL)
    #print(aggregate('JL'))
    #print type(datetime.date.today())
