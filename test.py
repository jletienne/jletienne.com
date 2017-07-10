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
    print(chomba(start_time='07:30 pm', opponent='Minor Threat', month=6, day=4, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time='10:00 pm', opponent='Trout', month=6, day=11, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time='08:45 pm', opponent='Ice Cougars', month=6, day=18, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time='08:45 pm', opponent='Lighting', month=6, day=25, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time=' All Day', opponent='Fourth of July', month=7, day=4, year=2016, team='Chupacabras', location='USA'))
    print(chomba(start_time='09:30 pm', opponent='Royals', month=7, day=9, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time='07:00 pm', opponent='Minor Threat', month=7, day=16, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time='08:15 pm', opponent='Trout', month=7, day=23, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))
    print(chomba(start_time='07:00 pm', opponent='Royals', month=7, day=30, year=2016, team='Chupacabras', location='Allen Community Ice Rink'))


    print(chomba(start_time='07:00 pm', opponent='Knicks', month=6, day=3, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Dream Team', month=6, day=10, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='09:00 pm', opponent='Last One Picked', month=6, day=17, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='09:00 pm', opponent='Tropics', month=6, day=24, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Fourth of July', month=7, day=4, year=2016, team='Cha-Ching', location='USA'))
    print(chomba(start_time='08:00 pm', opponent='ULINE', month=7, day=8, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Knicks', month=7, day=15, year=2016, team='Cha-Ching', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Dream Team', month=7, day=22, year=2016, team='Cha-Ching', location='The Core'))


    print(chomba(start_time='11:00 AM', opponent='Grapes of Wrath', month=6, day=11, year=2016, team='Orange', location='Carson Beach'))


    print(chomba(start_time='07:15 PM', opponent='Indeed 2', month=6, day=13, year=2016, team='Black', location='CPCT (Red)'))


    print(chomba(start_time='09:00 pm', opponent='Tropics', month=6, day=3, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Cha-Ching', month=6, day=10, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Knicks', month=6, day=17, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='08:00 pm', opponent='ULINE', month=6, day=24, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time=' All Day', opponent='', month=7, day=4, year=2016, team='Dream', location='USA'))
    print(chomba(start_time='09:00 pm', opponent='Last One Picked', month=7, day=8, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='09:00 pm', opponent='Tropics', month=7, day=15, year=2016, team='Dream', location='The Core'))
    print(chomba(start_time='07:00 pm', opponent='Cha-Ching', month=7, day=22, year=2016, team='Dream', location='The Core'))

    print(chomba(start_time='10:00 pm', opponent='Ice Cougars', month=6, day=4, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time='10:00 pm', opponent='Chupacabras', month=6, day=11, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time='07:30 pm', opponent='Royals', month=6, day=18, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time='07:30 pm', opponent='Minor Threat', month=6, day=25, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time=' All Day', opponent='Fourth of July', month=7, day=4, year=2016, team='Trout', location='USA'))
    print(chomba(start_time='07:00 pm', opponent='Lightning', month=7, day=9, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time='08:15 pm', opponent='Ice Cougars', month=7, day=16, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time='08:15 pm', opponent='Chupacabras', month=7, day=23, year=2016, team='Trout', location='Allen Community Ice Rink'))
    print(chomba(start_time='08:15 pm', opponent='Lightning', month=7, day=30, year=2016, team='Trout', location='Allen Community Ice Rink'))

    print(chomba(team='Hit_This', start_time='8:50 pm', opponent='Roll Toad', month=6, day=27, year=2016, location='Glencoe Park'))

    print(chomba(team='Black', start_time='7:15 pm', opponent='Blue Sky', month=7, day=6, year=2016, location='Court Blue Full'))
    print(chomba(team='Black', start_time='7:15 pm', opponent='Indeed 2', month=7, day=13, year=2016, location='Court Blue Full'))
    print(chomba(team='Black', start_time='9:15 pm', opponent='WWE', month=7, day=20, year=2016, location='Court Blue Full'))
    print(chomba(team='Black', start_time='8:15 pm', opponent='RSM', month=7, day=27, year=2016, location='Court Red Full'))
    print(chomba(team='Black', start_time='9:15 pm', opponent='Gartner', month=8, day=3, year=2016, location='Court Blue Full'))
    print(chomba(team='Black', start_time='9:15 pm', opponent='Jumpmen', month=8, day=10, year=2016, location='Court Blue Full'))
    print(chomba(team='Black', start_time='8:15 pm', opponent='Vineyard Vines', month=8, day=17, year=2016, location='Court Blue Full'))
    print(chomba(team='Black', start_time='9:15 pm', opponent='Blue Sky', month=8, day=24, year=2016, location='Court Blue Full'))

    print(chomba(team='Hit_This', start_time='8:50 pm', opponent='Roll Toad', month=7, day=11, year=2016, location='Glencoe Park'))
    print(chomba(team='Hit_This', start_time='7:30 pm', opponent='The Crystal Mets', month=7, day=18, year=2016, location='Glencoe Park'))
    print(chomba(team='Hit_This', start_time='9:10 pm', opponent='Balls Deep', month=7, day=25, year=2016, location='Glencoe Park'))
    print(chomba(team='Hit_This', start_time='8:40 pm & 9:30 pm', opponent='CDC Ballers & Les Miseraballs', month=8, day=1, year=2016, location='Churchill Park'))
    print(chomba(team='Hit_This', start_time='6:40 pm', opponent='Triage', month=8, day=8, year=2016, location='Glencoe Park'))
'''
    print(chomba(team='Hardhats', start_time='7:55 pm', opponent='Tequila Makes Our Helmets Fall Off', month=7, day=11, year=2017, location='Fair Oaks Park'))
    print(chomba(team='Hardhats', start_time='7:55 pm', opponent='Pitches Be Crazy', month=7, day=18, year=2017, location='Fair Oaks Park'))
    print(chomba(team='Hardhats', start_time='TBA', opponent='TBA', month=7, day=25, year=2017, location='Fair Oaks Park'))

    print(chomba(team='Purple', start_time='8:45pm', opponent='Red', month=8, day=3, year=2017, location='Allen Community Ice Rink'))
    print(chomba(team='Purple', start_time='8:45pm', opponent='Yellow', month=8, day=10, year=2017, location='Allen Community Ice Rink'))


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
