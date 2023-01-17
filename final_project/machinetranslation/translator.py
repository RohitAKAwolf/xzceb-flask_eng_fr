import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_Text):
    french_text=language_translator.translate(text=english_Text,source='en',target='fr').get_result()
    return french_text


english_input=input("ENTER English:")
print(english_to_french(english_input)['translations'][0]['translation'])


def french_to_english(french):
    english_text=language_translator.translate(text=french,source='fr',target='en').get_result()
    return english_text


french_input=input("ENTER French:")
print(french_to_english(french_input)['translations'][0]['translation'])