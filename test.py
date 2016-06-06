import requests
import sys, os
import json
import re
import datetime
import calendar

def getPlayers():
    URL = 'https://chup-chombas.firebaseio.com/Chupacabras/Players.json'

    r = requests.get(URL).json()
    return r

def chomba(start_time = '10 pm', location='Allen Community Ice Rink', opponent = 'Opponent', year=2016, month=1, day=1):
    my_date = datetime.date(year, month, day)
    gameday = str(my_date)
    weekday = calendar.day_name[my_date.weekday()]

    URL = 'https://chup-chombas.firebaseio.com/{}/Events/{}.json'.format('Chupacabras', gameday)

    gameinfo = {
                    'Start_Time': start_time,
                    'Location': location,
                    'Opponent': opponent,
                    'Players': getPlayers(),
                    'Date': '{:%b %d, %Y}'.format(my_date),
                    'Weekday': weekday
                }

    r = requests.put(URL, data=json.dumps(gameinfo))
    print(URL)
    return r

def getNextEvent(team='None'):
    URL = 'https://chup-chombas.firebaseio.com/{}/Events.json'.format(team)
    r = requests.get(URL).json()
    x = []
    for i in r:
        #return r[i]['Date'] == datetime.date(.today())
        x.append(i)
    return r[sorted(x)[0]]['Date'] == datetime.date(2016, 6, 4)

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

if __name__ == "__main__":
    print(getNextEvent(team='Chupacabras'))
