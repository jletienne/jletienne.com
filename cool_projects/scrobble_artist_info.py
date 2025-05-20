import yaml
import pandas as pd
import requests
import base64
from cool_projects.g_sheets import get_last_date, get_all_artists_df, get_known_artists_df
import os
import json
from datetime import date


if os.environ.get('HEROKU'):
    a2 = os.environ.get('SCROBBLE_CREDENTIALS')
    credentials = json.loads(base64.urlsafe_b64decode(a2))
else:
    credentials = yaml.safe_load(open('credentials/credentials.yaml'))


# Load credentials
key = credentials['api_key']
user= credentials['user']

def clean_all_artists_df():
    values = get_all_artists_df()
    all_artists_df = pd.DataFrame(values)
    all_artists_df.columns = ['artist_name']
    all_artists_df.drop_duplicates()

    return all_artists_df

def clean_known_artists_df():
    known_artists_values = pd.DataFrame(get_known_artists_df())
    known_artists_df = pd.DataFrame(known_artists_values)
    known_artists_df.columns = ['artist_name']

    return known_artists_df

def get_missing_artists():

    all_artists_df = clean_all_artists_df()
    known_artists_df = clean_known_artists_df()

    outer = all_artists_df.merge(known_artists_df, how='outer', indicator=True)

    anti_join = outer[(outer._merge=='left_only')]#.drop('_merge', axis=1)
    df = anti_join.drop_duplicates()
    return list(df['artist_name'])

def apply_genre_tags(final):

    final.genre[final["tags"].str.len() == 0] = 'Pop'
    final.genre[final.tags.map(set(['pop']).issubset) & final.genre.isnull() ] = 'Pop'
    final.genre[final.tags.map(set(['empty-default-pop']).issubset) & final.genre.isnull() ] = 'Pop'

    final.genre[final.tags.map(set(['electronic']).issubset) & final.genre.isnull()] = 'Pop'

    final.genre[final.tags.map(set(['country']).issubset) & final.genre.isnull()] = 'Country'


    final.genre[final.artist.map(set(['Jacobs Vocal Academy']).issubset) & final.genre.isnull()] = 'Vocal Lessons'

    final.genre[final.tags.map(set(['Corridos tumbados']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Corridos']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['corridos']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Salsa']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['salsa']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Bachata']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['bachata']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Latin']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['latin']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Mexian']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Mexico']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Mexico']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['Reggaeton']).issubset) & final.genre.isnull()] = 'Latin'
    final.genre[final.tags.map(set(['reggaeton']).issubset) & final.genre.isnull()] = 'Latin'


    final.genre[final.tags.map(set(['k-pop']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['Soundtrack']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['experimental']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['Lo-Fi']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['indie pop']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['indie']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['pop punk']).issubset) & final.genre.isnull()] = 'Pop'

    final.genre[final.tags.map(set(['rap']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['hip hop']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['hip-hop']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['Hip-Hop']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['trap']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['trap rap']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['emo rap']).issubset) & final.genre.isnull()] = 'Hip-Hop'
    final.genre[final.tags.map(set(['cloud rap']).issubset) & final.genre.isnull()] = 'Hip-Hop'


    final.genre[final.tags.map(set(['rock']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['alternative rock']).issubset) & final.genre.isnull()] = 'Pop'

    final.genre[final.tags.map(set(['alternative']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['House']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['instrumental']).issubset) & final.genre.isnull()] = 'Pop'


    final.genre[final.tags.map(set(['folk']).issubset) & final.genre.isnull()] = 'Country'

    final.genre[final.tags.map(set(['acoustic']).issubset) & final.genre.isnull()] = 'Pop'
    final.genre[final.tags.map(set(['rnb']).issubset) & final.genre.isnull()] = 'Pop'


    final['date_added']= str(date.today())
    final = final[['artist', 'genre', 'date_added', 'tags']]

    return final

def get_artist_genres():

    missing_artists = get_missing_artists()


    artist_tags=[]
    for artist in missing_artists[0:100]:
        try:
            url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={}&user={}&api_key={}&format=json'.format(quote(artist), user, key)
            r = requests.get(url)
            tracks = r.json()
            tags = [i['name'] for i in tracks['artist']['tags']['tag']]
            artist_tags.append([artist, tags])
        except:
            artist_tags.append([artist, ['empty-default-pop']])

    final = pd.DataFrame(artist_tags)
    final['genre'] = None
    final.columns = ['artist', 'tags', 'genre']
    
    artist_genre_df = apply_genre_tags(final)

    return artist_genre_df

if __name__ == '__main__':
    get_artist_genres()