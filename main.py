import slack_util
import constants
from dotenv import load_dotenv

load_dotenv()
# for channel in constants.channels:
#     slack_util.get_chat_history(channel['id'], channel['name'])


print(slack_util.list_all_memberids_from_channel(constants.HACKATHON_CHANNEL_ID, store=True))
# slack_util.send_message('U05J2G1KVV4', 'hi??')
# slack_util.get_chat_history(constants.HACKATHON_CHANNEL_ID)
