import requests
import sys, os
import json
import re
import datetime
import calendar

def getPlayers(team='None'):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Players.json'.format(team)

    r = requests.get(URL).json()
    return r

def chomba(start_time = 'None', location='None', team='None', opponent = 'None', year=2016, month=1, day=1):
    my_date = datetime.date(year, month, day)
    gameday = str(my_date)
    weekday = calendar.day_name[my_date.weekday()]
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Events/{}.json'.format(team, gameday)

    gameinfo = {
                    'Start_Time': start_time,
                    'Location': location,
                    'Opponent': opponent,
                    #'Players': getPlayers(team),
                    'Date': '{:%b %d, %Y}'.format(my_date),
                    'Weekday': weekday
                }

    r = requests.put(URL, data=json.dumps(gameinfo))
    print(URL)
    return r

def getDate(date='Jan 1, 2099'):
        return datetime.datetime.strptime(date, '%b %d, %Y').date()

def getNextEvent(team='Chupacabras'):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Events.json'.format(team)
    r = requests.get(URL).json()

    future_events = {i for i in r if datetime.date.today <= getDate(r[i]['Date'])}
    next_event = sorted(future_events)[0]

    return next_event


def doAll():
    '''
    print(chomba(team='Hit_This', start_time='8:50 pm', opponent='Roll Toad', month=7, day=11, year=2016, location='Glencoe Park'))
    print(chomba(team='Hit_This', start_time='7:30 pm', opponent='The Crystal Mets', month=7, day=18, year=2016, location='Glencoe Park'))
    print(chomba(team='Hit_This', start_time='9:10 pm', opponent='Balls Deep', month=7, day=25, year=2016, location='Glencoe Park'))
    print(chomba(team='Hit_This', start_time='8:40 pm & 9:30 pm', opponent='CDC Ballers & Les Miseraballs', month=8, day=1, year=2016, location='Churchill Park'))
    print(chomba(team='Hit_This', start_time='6:40 pm', opponent='Triage', month=8, day=8, year=2016, location='Glencoe Park'))
'''


def getTeams():
    URL = 'https://chup-chombas.firebaseio.com/Teams.json'
    r = requests.get(URL).text
    return r


def incrementTrip(team='None'):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Visits.json'.format(team)
    r = requests.get(URL).json()
    increment = r + 1
    doIt = requests.put(URL, data=json.dumps(increment))
    return URL

def getEvents(team='None'):
    URL = 'https://chup-chombas.firebaseio.com/Teams/{}/Events.json'.format(team)
    r = requests.get(URL).json()
    return r

def getNextPlayerEvent(events='None'):

    try:
        future_events = {i for i in events if datetime.date.today() <= getDate(events[i]['Date'])}
        next_event = sorted(future_events)[0]
    except:
        next_event = 'No Next Event'

    return next_event

def aggregate(player='None'):
    URL = 'https://chup-chombas.firebaseio.com/Players/{}/Teams.json'.format(player)
    r = requests.get(URL).json()

    x = {}

    for i in r:
        x.update(getEvents(i))

    date =  getNextPlayerEvent(x)

    if date == 'No Next Event':
       next_event_info = {'Date': 'Regular Season Over!', 'Weekday':'Had a Blast', 'Location': 'We\'ll do it again', 'Time': 'Offseason', 'Opponent': 'See You Next Season!', 'Start_Time': 'That Was Fun'}
       return next_event_info


    return x[date]

def getPlayerName(player='None'):
    URL = 'https://chup-chombas.firebaseio.com/Players/{}.json'.format(player)
    r = requests.get(URL).json()
    return r['Name']


if __name__ == "__main__":
    #print(incrementTrip('Black'))
    doAll()
    #print(aggregate('JL'))
    #print type(datetime.date.today())
