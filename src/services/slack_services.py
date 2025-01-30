import slack
from src.env import env

class SlackService:

  def __init__(self):
    self.slack_client = slack.WebClient(
      token=env['SLACK_CONFIG']['slack_token']
    )
  
  def sendMessage(self, channel: str, text: str):
    response = self.slack_client.chat_postMessage(channel=channel, text=text)