import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
#$from logger import logger

from cool_projects.bobby_hiit_jr_g_sheets import get_last_fitbod_date

import pandas as pd
import requests
import yaml
import io




# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to

def get_fitbod_data():

    print('get 4')

    if os.environ.get('HEROKU'):
        token = os.environ.get('fitbod_token_luke')
        channel_id = os.environ.get('workout_channel_luke')
    else:
        token = yaml.safe_load(open('config.yaml'))['fitbod_token_luke']
        channel_id = yaml.safe_load(open('config.yaml'))['workout_channel_luke']

    print('get 5')
    client = WebClient(token)


    try:
        # Call the conversations.history method using the WebClient
        # conversations.history returns the first 100 messages by default
        # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
        result = client.conversations_history(channel=channel_id)

        conversation_history = result["messages"]

        print('get 6')

        # Print results
        #print("{} messages found in {}".format(len(conversation_history), id))

        newest_workout_url = conversation_history[0]['files'][0]['url_private']

        raw_workout_data = requests.get(newest_workout_url, headers={'Authorization': 'Bearer %s' % token})
        workout_data_text = io.StringIO(raw_workout_data.text)
        x = pd.read_csv(workout_data_text)
        final = x.sort_values('Date')
        return final


    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))

def get_fitbod_filter_data(final):
    final = get_fitbod_data()
    fitbod_filtered_data = final[final['Date'] > get_last_fitbod_date()]
    return fitbod_filtered_data


if __name__ == '__main__':
    get_fitbod_filter_data()
