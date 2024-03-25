#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    # Added to support Interaction with Azure AI Language API
    ENDPOINT_URL = os.environ.get("MicrososftAIServiceEndpoint", "https://lang-s01.cognitiveservices.azure.com/")
    print(f"ENDPOINT_URL = {ENDPOINT_URL}")
    API_KEY = os.environ.get("MicrosoftAPIKey","d8c4f1a683a345428afbbad03de671cf")
    #SET MicrosoftAIServiceEndpoint=https://t6languageservice.cognitiveservices.azure.com/
    
