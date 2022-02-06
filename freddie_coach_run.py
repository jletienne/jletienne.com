import yaml
import pandas as pd
import requests
import io
from cool_projects.get_fitbod_data import *
from cool_projects.freddie_coach_g_sheets import do_all, do_all2
import os

if os.environ.get('HEROKU'):
    a2 = os.environ.get('SCROBBLE_CREDENTIALS')
    credentials = json.loads(base64.urlsafe_b64decode(a2))
else:
    credentials = yaml.safe_load(open('credentials/credentials.yaml'))


# Load credentials
key = credentials['api_key']
user= credentials['user']


def update():

    try:
        final = get_fitbod_data()

        new_data = get_fitbod_filter_data(final)
        #print(new_data)
        #max_date_df = get_new_max_date_df(final)
    except:
        print('it messed up')
        new_data = 'Done'

    if len(new_data) > 0:
        stream = io.StringIO()
        new_data.to_csv(stream, header=False, index=False)
        stream.seek(0)
        do_all(stream)

        # this bs isn't needed, just use a max function in google sheets tbh
        '''stream2 = io.StringIO()
        max_date_df.to_csv(stream2, index=False)
        stream2.seek(0)
        return do_all2(stream2)'''
    else:
        return 'some say deadlifts are leg day, others say deadlifts are for backday, I say deadlifts are for another day. no new workouts!'


if __name__ == '__main__':
    print(update())


# Create Google Sheet Integration (done)
# csv stream
# to do load into heroku
# run every hour
# Publish to Tableau Public
