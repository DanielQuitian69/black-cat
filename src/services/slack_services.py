import slack
from src.env import env

class SlackService:

  """
  Class responsible for executing operations in the Slack service
  """
  def __init__(self):
    self.slack_client = slack.WebClient(
      token=env['SLACK_CONFIG']['slack_token']
    )
  
  """
  Method responsible for sending a message to Slack

  Args:
    channel (str): Channel identifier to which the message is required to be sent. I.e, 'U0183SFT24B'
    message(str): Message which is required to be sent in plaintext. I.e, 'Hello World!'
  """
  def sendMessage(self, channel: str, message: str) -> None:
    response = self.slack_client.chat_postMessage(channel=channel, text=message)