""" This module facilitates language translation fro english to french and french to english"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')


def english_to_french(english_text):
    """ This function translates english text to french"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    json_translation=json.dumps(translation, indent=2, ensure_ascii=False)
    french_text=json_translation['translations']['translations']
    return french_text

def french_to_english(french_text):
    """ This function translates french text to english"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    json_translation=json.dumps(translation, indent=2, ensure_ascii=False)
    english_text=json_translation['translations']['translations']
    return english_text
