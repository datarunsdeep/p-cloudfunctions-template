#!/usr/bin/env bash
# use this to set the project and activate the service account from your local
# credentials.json would be your service account file
# don't forget to give relevant access needed to service account 
gcloud config set project mydeal-bigquery
gcloud auth activate-service-account \
    service-account.iam.gserviceaccount.com \
    --key-file=credentials.json
