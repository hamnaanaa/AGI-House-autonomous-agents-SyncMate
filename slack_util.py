import os
import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime
import pandas as pd
import constants
import file_util

# create a slack client
slack_token = os.getenv("SLACK_BOT_TOKEN")

client = WebClient(token=slack_token)

channel_id = constants.HACKATHON_CHANNEL_ID # Replace with your channel id


user_cache = {} # user_id -> user_name


# def get_paginaged_chat_history(channel_id: str) -> list[dict]:
#     try:
#         cursor = None

#         while True:
#             # Call the conversations.history method using the WebClient
#             # conversations.history returns the first 100 messages by default
#             # You can increase or decrease this count in the API call
#             result = client.conversations_history(channel=channel_id, cursor=cursor)

#             # Get the message data from the response
#             messages = result.data.get('messages')

#             for message in messages:
#                 user = client.users_info(user=message.get('user')).data.get('user', {})
#                 print(f"{user.get('real_name')}: {message.get('text')}")

#             cursor = result.data.get('response_metadata', {}).get('next_cursor')
#             if not cursor:
#                 break

                
#     except SlackApiError as e:
#         print(f"Error: {e.response['error']}")


def get_chat_history(channel_id: str) -> list[str]:
    
    message_results = []
    try:
        cursor = None
        db_entries = pd.DataFrame({
            'user':[],
            'text': [],
            'ts': []
        })
        while True:
            count = 0
            # Call the conversations.history method using the WebClient
            # conversations.history returns the first 100 messages by default
            # You can increase or decrease this count in the API call
            result = client.conversations_history(channel=channel_id, cursor=cursor)

            # Get the message data from the response
            messages = result.data.get('messages')
            print(f'pulled {len(messages)} messages')
            count += len(messages)
            for message in messages:
                timestamp = datetime.datetime.fromtimestamp(round(float(message.get('ts'))))
                entry = {
                    'user': get_username_from_id(message.get('user')),
                    'text': message.get('text'),
                    'ts': timestamp
                }
                db_entries = db_entries.append(pd.DataFrame(entry, index=[0]), ignore_index=True)
            # print(db_entries)
            cursor = result.data.get('response_metadata', {}).get('next_cursor')
            # print(f'cursor: {cursor}, count: {count}')
            if not cursor or count > 10:
                break
        db_entries.to_csv('database/hackathon_channel.csv', index=False)
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
    
    return message_results

def send_message(user_name, user_id, message_text:str="do you like to grab a coffee sometime."):
    try:
        # Open a direct message channel to the user
        response = client.conversations_open(users=user_id)
        dm_channel = response["channel"]["id"]
        message_text = f'hi {user_name}, {message_text}'
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=dm_channel,
            text=message_text
        )

        assert result["message"]["text"] == message_text

    except SlackApiError as e:
        print(f"Error: {e}")



def get_username_from_id(user_id: str) -> str:
    if user_id not in user_cache:
        user_name = client.users_info(user=user_id).data.get('user', {}).get('real_name', 'name not found')
        user_cache.update({user_id: user_name})
    
    return user_cache[user_id]



def list_all_memberids_from_channel(channel_id: str, store: bool = False): 
    cursor_id = None
    while True:
        try:
            users = []
            # Call the conversations.members method using the WebClient
            result = client.conversations_members(channel=channel_id, cursor=cursor_id)
            # Get the members data from the response
            member_ids = result.data.get('members')
            cursor_id = result.data.get('response_metadata', {}).get('next_cursor')
            for member_id in member_ids:
                user = client.users_info(user=member_id).data.get('user', {})
                user_info = {
                    'name':user.get('real_name'), 
                    'id': user.get('id')
                }
                print(f'got {user_info}')
                users.append(user_info)
            if not cursor_id:
                break
        except SlackApiError as e:
            print(f"Error: {e.response['error']}")
        if store:
            cur_time = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")
            write_to_csv(users, f'database/users_{cur_time}.csv', field_name=list(users[0]))
    return users


def write_to_csv(data, filename, field_name):
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer
        csvwriter = csv.DictWriter(csvfile, fieldnames=field_name)

        # Write each row from the list to the CSV
        for row in data:
            csvwriter.writerow(row)


# for user in users:
#     send_message()

print(file_util.read_csv('database/users_20230722_18:12:50.csv'))
