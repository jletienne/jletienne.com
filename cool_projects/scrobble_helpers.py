import yaml
import pandas as pd
import requests
import base64
from cool_projects.g_sheets import get_last_date
import os
import json

if os.environ.get('HEROKU'):
    a2 = os.environ.get('SCROBBLE_CREDENTIALS')
    credentials = json.loads(base64.urlsafe_b64decode(a2))
else:
    credentials = yaml.safe_load(open('credentials/credentials.yaml'))


# Load credentials
key = credentials['api_key']
user= credentials['user']

url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={}&api_key={}&format=json&limit=200'.format(user, key)
r = requests.get(url)
tracks = r.json()
print(r.status_code)


'''def get_last_date():
    df = pd.read_csv('max_date_uts.csv')
    return df.iloc[0]['max_date_uts']'''

def get_recent_tracks_df():
    recent_tracks = []
    for i in tracks['recenttracks']['track']:
        try:
            track = {}
            track['artist_name'] = i['artist']['#text']
            track['artist_id']   = i['artist']['mbid']
            track['album_name']  = i['album']['#text']
            track['album_id']    = i['album']['mbid']
            track['date_uts']    = i['date']['uts']
            track['track_name']  = i['name']
            track['track_id']    = i['mbid']
            recent_tracks.append(track)
        except:
            pass
    final = pd.DataFrame(recent_tracks)
    final['date_uts'] = final['date_uts'].astype(int)
    return final

def get_filter_data(final):
    final = get_recent_tracks_df()
    filtered_data = final[final['date_uts'] > get_last_date()]
    return filtered_data

def get_new_max_date_df(final):
    max(final['date_uts'])
    max_date_uts = max(final['date_uts'])
    return pd.DataFrame([{'max_date_uts': max_date_uts}])

if __name__ == '__main__':
    get_last_date()
