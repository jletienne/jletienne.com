import requests
import sys, os
import json
import re
import datetime
import calendar

def getPlayers(team):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Players.json'.format(team)
    r = requests.get(URL).json()

    return r

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

def incrementTrip(team='None'):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Visits.json'.format(team)
    r = requests.get(URL).json()
    increment = r + 1
    doIt = requests.put(URL, data=json.dumps(increment))
    return doIt

def eventInfo(date, team='None'):
   if date == 'No Next Event':
       next_event_info = {'Date': 'Regular Season Over!', 'Weekday':'Had a Blast', 'Location': 'We\'ll do it again', 'Time': 'Offseason', 'Opponent': 'See You Next Season!', 'Start_Time': 'That Was Fun'}
       return next_event_info

   URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Events/{}/.json'.format(team, date)
   r = requests.get(URL).json()
   incrementTrip(team=team)
   return r

def teamInfo(team='None'):
   URL = 'https://chup-chombas.firebaseio.com/Teams/{}.json'.format(team)
   r = requests.get(URL).json()

   return r


def getDate(date='Jan 1, 2099'):
   return datetime.datetime.strptime(date, '%b %d, %Y').date()


def getNextEvent(team='Chupacabras'):
   URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Events.json'.format(team)

   try:
       r = requests.get(URL).json()

       future_events = {i for i in r if datetime.date.today() <= getDate(r[i]['Date'])}
       next_event = sorted(future_events)[0]
   except:
       next_event = 'No Next Event'
   return next_event

def getTeams():
    URL = 'https://chup-chombas.firebaseio.com/Teams.json'
    r = requests.get(URL).json()
    return r

def add_multiple():



    import requests
    import json
    import re


    def make_regex(x):
        ips = x
        products = "".join(ips)
        return products

    def html_source(URL):
        return requests.get(URL).text

    URL = 'http://stats.pointstreak.com/players/print/players-team-schedule.html?teamid=709641&seasonid=17484'
    game_times = re.findall(make_regex(['<td>(.*)</td>']), html_source(URL))
    game_dates = re.findall(make_regex(['<td class="text-center">(.*?)</td>']), html_source(URL))
    home_team2 = re.findall(make_regex(['<td class="text-left"><span class="highlight"></span><a href="players-team.html?(.*?)</a>']), html_source(URL))
    home_team1 = re.findall(make_regex(['<td class=\"text-left\"><a href="players-team.html?(.*?)</a>']), html_source(URL))

    away_team1 = re.findall(make_regex(['<td class="text-left"><a href="players-team.html?(.*?)</a>']), html_source(URL))
    away_team2 = re.findall(make_regex(['<td class="text-left"><span class="highlight"></span><a href="players-team.html?(.*?)</a>']), html_source(URL))

    home_teams = [i[31:] for i in home_team1 + home_team2]
    away_teams = [i[31:] for i in away_team1 + away_team2]


    x = zip(game_times, game_dates)#, home_teams)#, away_teams)


    for i in x:
        #print(i[1].strip())
        hockey_month = int(datetime.datetime.strptime('2018 ' + i[1].strip(), '%Y %a, %b %d').strftime("%m"))
        hockey_day = int(datetime.datetime.strptime('2018 ' + i[1].strip(), '%Y %a, %b %d').strftime("%d"))
        addEvent(start_time = i[0], location = 'Allen Hockey Rink', opponent = 'Opponent',year=2018, month=hockey_month, day=hockey_day, team='Red')


if __name__ == "__main__":
    print(add_multiple())
