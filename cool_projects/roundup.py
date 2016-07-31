import requests
import sys, os
import json
import re
import datetime
import calendar
from cool_projects.chomba import *

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
    return r
