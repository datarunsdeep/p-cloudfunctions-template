#!/usr/bin/env bash


gcloud config set project <project-name>
gcloud services enable cloudbuild.googleapis.com
gcloud functions deploy <cloud-function-name> \
    --entry-point <function-entrypoint> \
    --runtime python37 \
    --trigger-http \
    # or
    # --trigger-topic <TRIGGER_TOPIC> \  
    # or
    # --trigger-bucket= <TRIGGER_BUCKET>
    --service-account <service-account-to-use> \
    --verbosity debug \
    --memory 512MB   \
    --timeout 540s \
    --set-env-vars USE_WORKER_V2=TRUE