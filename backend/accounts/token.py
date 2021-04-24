import requests
import json
from environs import Env

env = Env()
env.read_env()

"""
DJANGO_URL_PRODUCTION: only for production

"""

def getToken( data, endpoint ):
    header = {"content-type": "application/json"}
    payload = data
    token = requests.post(env('DJANGO_URL_PRODUCTION') + endpoint + '/', json.dumps(payload), headers=header)

    return token.json()

