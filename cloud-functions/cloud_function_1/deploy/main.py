#!/usr/bin/env python
# coding: utf-8

# - project/PROJECT_NAME
# - owner/editor info
# - copyright© datarunsdeep.com.au

# In[1]:

import base64
from google.cloud import bigquery
from google.cloud import storage
import logging
import os
import json
import configurations as config
import re
import io
import time
from flask import escape
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Use as per your requirement
PROJECT_ID = config.PROJECT_ID
DATASET_ID = config.DATASET_ID
TABLE_ID = config.TABLE_ID
key_file_location = config.SERVICE_CREDENTIALS
bucket_name = config.GCS_BUCKET
webhook = config.WEBHOOK
#Authenticating as a service account
#Passing credentials via environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_file_location
bq_client = bigquery.Client()
gcs_client = storage.Client()
bucket = gcs_client.get_bucket(bucket_name)


# In[4]:
def call_slack(webhook, payload):
        """
    Function definition : sends a message to the slack channel passed as a param
    Args:
         webhook: slack channel webhook.
         payload: message to be displayed.
    """
    if(payload == ''):payload = 'All good for now'
    logging.basicConfig(level=logging.DEBUG)
    webhook_url = webhook
    header = f"Project: {PROJECT_ID}\nAlerts:\n"
    header += payload
    slack_data =  {'text': header}
    try: 
        response = requests.post(webhook_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
    except SlackApiError as e:
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        
def entry_point_function(request):
    
    """
    Function definition.
    Args:
         request: ? .
         returns: ?.
    """
    try:

        # CODE - BLOCK 

        
    except Exception as error:
        logging.error(f"Trace: {traceback.format_exc()}")
        call_slack(webhook, payload)
        time.sleep(1)
        raise error


# For local debugging
if __name__ == '__main__':

    entry_point_function(request)


# In[ ]: