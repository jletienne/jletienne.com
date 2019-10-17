import random


'''points_for = 126
points_against = 40

exponent = 2.37
season_length = 16'''


def pythagorean_expecation(points_for=1,points_against=1, exponent=2.37, season_length=16):
    numer = points_for ** exponent
    denom = points_for ** exponent + points_against ** exponent

    return int(season_length * (numer / denom) + .5)


def judgement(e_wins):
    if e_wins >= 14:
        verdict = ["legendary status!",
                   "we got some dogs!",
                   "i don't want to get ahead of myself, but this team beats the Pats!",
                   "destined for greatness!",
                   "this team will go down in the history books!",
                   "championship aspirations!",
                   "someone's getting a raise!",
                   "this is a model organization with a high caliber track record!",
                   "lesser men wouldn't be this good!"
                  ]
    elif e_wins >= 8:
        verdict = ['we got a solid team!',
                   'proud of the effort!',
                   'when we play well, not many teams can hang with us!',
                   'if we just play our game, we have a chance to win the ship!',
                   'awesome!'
                  ]
    elif e_wins >= 4:
        verdict = ["we'll get this on thing track!",
                   "we're not too far out of the playoff raise!",
                   "just trying to squeak by over here",
                   "some positive momentum is needed!",
                   "we have good players, just gotta get it together!",
                   "not exactly what we expected, but keep grinding!"]
    else:
        verdict = ['yikes!',
                   'do you know benching the qb is an option?',
                   'your GM isn\'t gonna be thrilled!',
                   'wtf is Sachi Brown coaching this team!',
                   'you\'re closer to the \'19 dolphins than the \'72 team',
                   'uhhh, trust the process I guess!',
                   'Tank for Tua!',
                   "don't bother going to another game!",
                   "i'm gonna be real with you chief, this team is trash!"
                   ]

    return random.choice(verdict)


def football_expectation(points_for=1,points_against=1, exponent=2.37, season_length=16):
    e_wins = pythagorean_expecation(points_for,points_against, exponent, season_length)

    result = 'you\'re performing at a {}-{} level, {}'.format(e_wins, season_length-e_wins, judgement(e_wins))
    return {"points_for": points_for,
            "points_against": points_against,
            "verdict": result
            }


if __name__ == '__main__':
    football_expectation(points_for, points_against)
