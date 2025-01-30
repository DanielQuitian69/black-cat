import json
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def getEnvironmentConfig():
  envars = ['GENERAL_CONFIG', 'SLACK_CONFIG']
  env_config = {}
  for envar_key in envars:
    envar = os.environ[envar_key]
    try:
      env_config[envar_key] = json.loads(envar)
    except json.JSONDecodeError as e:
      print(f'An error occurred while obtaining the $envar_key envar')
  return env_config

env = getEnvironmentConfig()