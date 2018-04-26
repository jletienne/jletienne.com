import requests
import sys, os
import random
import json
import re
from decimal import *

from scipy.stats import binom, norm
import matplotlib.pyplot as plt
import numpy as np

#heroku config:set BUILDPACK_URL=https://github.com/arose13/conda-buildpack.git



def nfl_draft(incoming_picks = '1,2,3', outgoing_picks = '4,5,6' ):
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'JL'},
            'body': 'Yes it was'
        }
    ]



    picks_in = [s.strip() for s in incoming_picks.split(",")]
    picks_out = [s.strip() for s in outgoing_picks.split(",")]

    # Get Pick JSON data from static file
    def get_picks():
        filename = os.path.join("static", 'nfl_data.json')
        with open(filename) as blog_file:
            return json.load(blog_file)

    # Return Stardom Probability of each pick in draft
    def get_points(picks,data):
       return [data[str(pick)]['Points']/10000 for pick in picks]

    # Data we use from get_picks9)
    data = get_picks()

    # Value picks from binomial cdf
    def value_picks(picks):
        points =  get_points(picks,data)
        num_picks = len(picks)
        avg_picks = sum(points) / num_picks

        p = {str(n+1) + ' Star': 1 - binom.cdf(n, num_picks, avg_picks) for n in range(5)}
        return p

    # return this in a clean format
    def clean_value_picks(picks):
        points =  get_points(picks,data)
        num_picks = len(picks)
        avg_picks = sum(points) / num_picks

        p = {str(n+1) + ' Star': str(int(100*(1 - binom.cdf(n, num_picks, avg_picks)))) + '%' for n in range(5)}
        return p

    # Compare Picks from both teams
    def compare_picks(picks_in_results, picks_out_results):
        x = {}

        for a in picks_in_results:
            if picks_out_results[a] == 0:
                if picks_in_results[a] == 0:
                    x[a] = '0%'
                else:
                    x[a] = '100%'
            else:
                x[a] = str(int(100*round((picks_in_results[a]-picks_out_results[a])/picks_out_results[a],2)))+'%'

        return x

    picks_in_results = {'rawValue': value_picks(picks_in), 'cleanValue': clean_value_picks(picks_in), 'picks': picks_in}
    picks_out_results = {'rawValue':value_picks(picks_out), 'cleanValue': clean_value_picks(picks_out), 'picks': picks_out}


    trade_results = compare_picks(picks_in_results['rawValue'], picks_out_results['rawValue'])

    user = {'nickname': 'JL'}

    def grade_trade(trade_results):
        if int(trade_results['2 Star'][:-1]) < 0:
            return "This is a good trade for your team!"
        elif int(trade_results['2 Star'][:-1]) < 5:
            return "Decent trade, but you can you get more!"
        else:
            return "THAT'S RIGHT I WANT A GM WHO RIPS PEOPLE OFF!"


    trade_grade = grade_trade(trade_results)

    picks_in_string = re.sub("[^0-9,]", "", str(picks_in_results['picks']))
    picks_out_string = re.sub("[^0-9,]", "", str(picks_out_results['picks']))

    pageInfo = {'user': user,
                'posts': posts,
                'title': 'NFL Draft',
                'picks_in': picks_in_results,
                'picks_out':picks_out_results,
                'picks_in_string': picks_in_string,
                'picks_out_string': picks_out_string,
                'trade': trade_results,
                'picks_sorted': sorted(trade_results),
                'trade_grade': trade_grade}
    return pageInfo
    #'trade': sorted(trade_results.items(), key=lambda x: x[0])}

if __name__ == "__main__":
    print(nfl_draft())
