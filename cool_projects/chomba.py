import requests
import sys, os
import json
import re
import datetime

def getPlayers():
    URL = 'https://chup-chombas.firebaseio.com/Chupacabras/Players.json'

    r = requests.get(URL).json()
    return r

def addEvent(start_time = '10 pm', location = 'location', opponent = 'Opponent',year=3000, month=1, day=1, team='None'):
    event_date = datetime.date(year, month, day)
    gameday = str(event_date)
    weekday = calendar.day_name[event_date.weekday()]

    URL = 'https://chup-chombas.firebaseio.com/{}/Events/{}.json'.format(team, gameday)
    players = getPlayers()

    gameinfo = {
                    'Start_Time': start_time,
                    'Location': location,
                    'Opponent': opponent,
                    'Players': players,
                    'Date': '{:%b %d, %Y}'.format(my_date),
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


def getNextEvent(team='None'):
    return datetime.date(2016, 6, 11)

'''
def doAll():
    print(chomba(start_time='7:30 pm', opponent='Minor Threat', month=6, day=4))
    print(chomba(start_time='7:00 pm', opponent='Trout', month=6, day=11))
    print(chomba(start_time='8:45 pm', opponent='Ice Cougars', month=6, day=18))
    print(chomba(start_time='8:45 pm', opponent='Lighting', month=6, day=25))
    print(chomba(start_time='All Day', location='USA', opponent='Fourth of July', month=7, day=4))
    print(chomba(start_time='9:30 pm', opponent='Royals', month=7, day=9))
    print(chomba(start_time='7:00 pm', opponent='Minor Threat', month=7, day=16))
    print(chomba(start_time='8:15 pm', opponent='Trout', month=7, day=23))
    print(chomba(start_time='7:00 pm', opponent='Royals', month=7, day=30))
    '''


if __name__ == "__main__":
    print(cassel())
