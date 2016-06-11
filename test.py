import requests
import sys, os
import json
import re
import datetime
import calendar

def getPlayers(team='None'):
    URL = 'https://chup-chombas.firebaseio.com/{}/Players.json'.format(team)

    r = requests.get(URL).json()
    return r

def chomba(start_time = 'None', location='None', team='None', opponent = 'None', year=2016, month=1, day=1):
    my_date = datetime.date(year, month, day)
    gameday = str(my_date)
    weekday = calendar.day_name[my_date.weekday()]
    URL = 'https://chup-chombas.firebaseio.com/{}/Events/{}.json'.format(team, gameday)

    gameinfo = {
                    'Start_Time': start_time,
                    'Location': location,
                    'Opponent': opponent,
                    'Players': getPlayers(team),
                    'Date': '{:%b %d, %Y}'.format(my_date),
                    'Weekday': weekday
                }

    r = requests.put(URL, data=json.dumps(gameinfo))
    print(URL)
    return r

def getDate(date='Jan 1, 2099'):
        return datetime.datetime.strptime(date, '%b %d, %Y').date()

def getNextEvent(team='Chupacabras'):
    URL = 'https://chup-chombas.firebaseio.com/{}/Events.json'.format(team)
    r = requests.get(URL).json()

    future_events = {i for i in r if datetime.date.today <= getDate(r[i]['Date'])}
    next_event = sorted(future_events)[0]

    return next_event


def doAll():
    '''
    print(chomba(start_time='07:30 pm', opponent='Minor Threat', month=6, day=4))
    print(chomba(start_time='10:00 pm', opponent='Trout', month=6, day=11))
    print(chomba(start_time='08:45 pm', opponent='Ice Cougars', month=6, day=18))
    print(chomba(start_time='08:45 pm', opponent='Lighting', month=6, day=25))
    print(chomba(start_time=' All Day', location='USA', opponent='Fourth of July', month=7, day=4))
    print(chomba(start_time='09:30 pm', opponent='Royals', month=7, day=9))
    print(chomba(start_time='07:00 pm', opponent='Minor Threat', month=7, day=16))
    print(chomba(start_time='08:15 pm', opponent='Trout', month=7, day=23))
    print(chomba(start_time='07:00 pm', opponent='Royals', month=7, day=30))


    print(chomba(start_time='07:00 pm', opponent='Knicks', month=6, day=3, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Dream Team', month=6, day=10, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='09:00 pm', opponent='Last One Picked', month=6, day=17, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='09:00 pm', opponent='Tropics', month=6, day=24, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Fourth of July', month=7, day=4, year=2016, team='Cha-Ching', location='USA'))
    print(chomba(start_time='08:00 pm', opponent='ULINE', month=7, day=8, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Knicks', month=7, day=15, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Dream Team', month=7, day=22, year=2016, team='Cha-Ching', location='The Core'))


    print(chomba(start_time='11:00 AM', opponent='Grapes of Wrath', month=6, day=11, year=2016, team='Orange', location='Carson Beach'))


    print(chomba(start_time='7:15 PM', opponent='Indeed 2', month=6, day=13, year=2016, team='Black', location='CPCT (Red)'))
    '''

    print(chomba(start_time='09:00 pm', opponent='Tropics', month=6, day=3, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Cha-Ching', month=6, day=10, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Knicks', month=6, day=17, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='08:00 pm', opponent='ULINE', month=6, day=24, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='All Day', opponent='', month=7, day=4, year=2016, team='Dream', location='USA'))
    print(chomba(start_time='09:00 pm', opponent='Last One Picked', month=7, day=8, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='09:00 pm', opponent='Tropics', month=7, day=15, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Cha-Ching', month=7, day=22, year=2016, team='Dream', location='The Core'))


if __name__ == "__main__":
    #print(getNextEvent(team='Chupacabras'))
    #print(getNextEvent())
    #print(getDate())
    print(doAll())
