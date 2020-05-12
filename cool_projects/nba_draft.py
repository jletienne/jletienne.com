import requests
import sys, os
import random
import json
import re
from decimal import *

from scipy.stats import binom, norm

import numpy as np


def nba_draft(incoming_picks = '1,2', outgoing_picks = '4,5' ):

    picks_in = [s.strip() for s in incoming_picks.split(",")]
    picks_out = [s.strip() for s in outgoing_picks.split(",")]

    def get_picks():
        filename = os.path.join("static", 'nba_data.json')
        with open(filename) as blog_file:
            return json.load(blog_file)
    data = get_picks()

    def get_points(picks):
       return [data[str(pick)]['Star'] for pick in picks]

    class draft(object):

        #define class to simulate a simple calculator
        def __init__ (self, picks):

            #start with zero
            self.picks = picks
            self.quantity = len(picks)
            self.points = get_points(picks)
        # Return Stardom Probability of each pick in draft

        # Data we use from get_picks()

        def value_picks(self): # Value picks from binomial cdf
            points =  self.points
            num_picks = len(points)
            avg_picks = sum(points) / num_picks

            p = {str(n+1) + ' Star': 1 - binom.cdf(n, num_picks, avg_picks) for n in range(5)}
            return p


        def clean_value_picks(self):  # return this in a clean format
            points =  get_points(self.picks)
            num_picks = self.quantity
            avg_picks = sum(points) / num_picks

            p = {str(n+1) + ' Star': str(int(100*(1 - binom.cdf(n, num_picks, avg_picks)))) + '%' for n in range(5)}
            return p

        def picks_results(self):
            return {'rawValue': self.value_picks(), 'cleanValue': self.clean_value_picks(), 'picks': self.picks}


    team_a = draft(picks_in)
    team_b = draft(picks_out)

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

    #picks_in_results = {'rawValue': value_picks(picks_in), 'cleanValue': clean_value_picks(picks_in), 'picks': picks_in}
    #picks_out_results = {'rawValue':value_picks(picks_out), 'cleanValue': clean_value_picks(picks_out), 'picks': picks_out}


    trade_results = compare_picks(team_a.picks_results()['rawValue'], team_b.picks_results()['rawValue'])



    def grade_trade(trade_results):
        if int(trade_results['1 Star'][:-1]) < 0:
            return "This is a good trade for your team!"
        elif int(trade_results['1 Star'][:-1]) < 5:
            return "Decent trade, but you can you get more!"
        else:
            return "THAT'S RIGHT I WANT A GM WHO RIPS OTHERS OFF!"




    trade_grade = grade_trade(trade_results)


    pageInfo = {
                'title': 'NBA Draft',
                'picks_in': team_a.picks_results(),
                'picks_out': team_b.picks_results(),
                'trade': trade_results,
                'picks_sorted': sorted(trade_results),
                'trade_grade': trade_grade}

    return pageInfo


if __name__ == "__main__":
    print(nba_draft())
