import requests
import sys, os
import json
import re
import datetime

def getPlayers(team):
    URL = 'https://chup-chombas.firebaseio.com/{}}/Players.json'.format(team)
    r = requests.get(URL).json()

    return r

def addEvent(start_time = '10 pm', location = 'location', opponent = 'Opponent',year=3000, month=1, day=1, team='None'):
    event_date = datetime.date(year, month, day)
    gameday = str(event_date)
    weekday = calendar.day_name[event_date.weekday()]

    URL = 'https://chup-chombas.firebaseio.com/{}/Events/{}.json'.format(team, gameday)
    players = getPlayers(team)

    gameinfo = {
                    'Start_Time': start_time,
                    'Location': location,
                    'Opponent': opponent,
                    'Players': players,
                    'Date': '{:%b %d, %Y}'.format(my_date),
                    'Date2': my_date,
                    'Weekday': weekday,
                }

    r = requests.put(URL, data=json.dumps(gameinfo))
    return URL

def eventInfo(date, team='None'):
   URL = 'https://chup-chombas.firebaseio.com/{}/Events/{}/.json'.format(team, date)
   r = requests.get(URL).json()

   return r

def teamInfo(team='None'):
   URL = 'https://chup-chombas.firebaseio.com/{}.json'.format(team)
   r = requests.get(URL).json()

   return r


def getDate(date='Jan 1, 2099'):
   return datetime.datetime.strptime(date, '%b %d, %Y').date()


def getNextEvent(team='Chupacabras'):
   URL = 'https://chup-chombas.firebaseio.com/{}/Events.json'.format(team)
   r = requests.get(URL).json()

   future_events = {i for i in r if datetime.date.today() <= getDate(r[i]['Date'])}
   next_event = sorted(future_events)[0]

   return next_event



if __name__ == "__main__":
    print(cassel())
