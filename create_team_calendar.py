import requests
import sys, os
import json
import re
import datetime
import calendar
import cool_projects.chomba as chomba


import requests
import json
import re



URL = 'http://stats.pointstreak.com/players/print/players-team-schedule.html?teamid=709641&seasonid=17484'

def make_regex(x):
    ips = x
    products = "".join(ips)
    return products

def html_source(URL):
    return requests.get(URL).text


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
    print(i)

if __name__ == "__main__":

    doAll()
