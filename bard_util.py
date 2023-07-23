from bardapi import Bard
import os
from dotenv import load_dotenv
import file_util
import time
load_dotenv()

user_csv_file = 'database/users_20230722_18:12:50.csv'
bio_store = 'database/bio.csv'
bard_token = os.getenv('BARD_TOKEN')
bard = Bard(token=bard_token)


def find_info_from_name(name: str):
    # prompt = 
    return bard.get_answer(f"help me search some key information about a person named {name}. If it's a common name, just return one of them.")['content']

def find_info_from_names(names: str | list):
    if isinstance(names, list):
        names = ''.join(names)
    prompt = ""
    return bard.get_answer(prompt)



def collect_users_info():
    user_bios = []
    users = file_util.read_csv(user_csv_file)
    count = 0
    for user in users:
        count += 1
        name = user.get('name')
        response = find_info_from_name(name)
        bio = {
            "name": name,
            "bio": response
        }
        user_bios.append(bio)
        print(bio)
        if count == 10:
            count = 0
            file_util.write_to_csv(user_bios, bio_store, list(bio))
            time.sleep(5)
            user_bios = []
        
    
        
collect_users_info()
    
