import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
#$from logger import logger

from cool_projects.freddie_coach_g_sheets import get_last_fitbod_date

import pandas as pd
import requests
import yaml
import io


if os.environ.get('HEROKU'):
    token = os.environ.get('fitbod_token')
    token = os.environ.get('workout_channel')
else:
    token = yaml.safe_load(open('config.yaml'))['fitbod_token']
    channel_id = yaml.safe_load(open('config.yaml'))['workout_channel']
    
client = WebClient(token)


# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to

def get_fitbod_data():
    try:
        # Call the conversations.history method using the WebClient
        # conversations.history returns the first 100 messages by default
        # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
        result = client.conversations_history(channel=channel_id)

        conversation_history = result["messages"]

        # Print results
        #print("{} messages found in {}".format(len(conversation_history), id))

        newest_workout_url = conversation_history[0]['files'][0]['url_private']
        return newest_workout_url

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))



if __name__ == '__main__':
    get_last_fitbod_date()
