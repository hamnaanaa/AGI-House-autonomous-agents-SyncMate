from bardapi import Bard
import os
from dotenv import load_dotenv
import file_util
load_dotenv()

user_csv_file = 'database/users_20230722_18:12:50.csv'
bard_token = os.getenv('BARD_TOKEN')
bard = Bard(token=bard_token)


def find_info_from_name(name: str):
    # prompt = 
    return bard.get_answer(f"help me search some key information about a person named {name}")['content']



def collect_users_info():
    user_infos = []
    users = file_util.read_csv(user_csv_file)
    for user in users:
        response = find_info_from_name(user.get('name'))
        print(response)
    
        
        