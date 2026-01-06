import yaml
import pandas as pd
import requests
import io
from cool_projects.health_helpers import *
from cool_projects.g_sheets_health import get_health_steps_df, do_all_health
import os

if os.environ.get('HEROKU'):
    a2 = os.environ.get('SCROBBLE_CREDENTIALS')
    credentials = json.loads(base64.urlsafe_b64decode(a2))
else:
    credentials = yaml.safe_load(open('credentials/credentials.yaml'))


# Load credentials
# key = credentials['api_key']
# user= credentials['user']


def update_health_steps():

    health_updates = [
        ('1eUSxuwoYrPbY0iL3JotWekR6zDTlpPgx', '1Mj3VpGIALaA4ojJnLb1-yTScIvoa90woOfHivOW-_Ig', 'walking_steps'),
        ('1vXXghTEtu8olOXdNE5_v81Try02w8ub7', '1A7ugrJSoC7L6Jx66nEHjWP7hOSbQ3-hhqE7ha_hIu0c', 'weight'),
        ('1st423xCXiPmTjfwRZRGLsbCP1XrJuGZv', '15cUCWS6swZd5WUj1dzQXT4hGmVEoadFZ8SQPdpaeS5k', 'sleep_hrs')
    ]

    for i in health_updates:

        final = get_health_steps_df(folder_id=i[0])
        new_data = final
        #print(new_data)



        stream = io.StringIO()
        new_data.to_csv(stream, header=False, index=False)
        stream.seek(0)
        do_all_health(stream, SPREADSHEET_ID=i[1])


    return 'done'





if __name__ == '__main__':
    print(update_health_steps())


# View all files
# Union all files
# Append to google sheet
# run every half hour
