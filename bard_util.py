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

def find_info_from_names(names):
    if isinstance(names, list):
        names = ''.join(names)
    prompt = f"""
        I am going to a meeting with these people {names}. Having in mind all their background, characters, aspirations and believes please give me
        The summary of the crowd in a very informative for me way
        A few options and approaches for me to speak so I inspire them with my idea, wish to build and help bring that future
        Idea:
        We have to build agent by agent, step by step the future where AI is efficiently and morally running the government
    """
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
        
    
        
# collect_users_info()
find_info_from_names(["Rocky Yu", "Eduardo Reis", "Robert Nowell", "Ron Bodkin", "Harrison Chase", "Alex Reibman", "Jack", "Saurabh Misra", "Div Garg", "Jackson Jesionowski", "Bill Sun", "Jazear Brooks", "Cameron mostoufi", "Lina Colucci", "greg tanaka", "Vishnu Rajan Tejus", "Lei Zhao", "Simon Suo", "Allen Liu", "Travis Cline", "Jeremy Nixon", "Gurkaran", "Mike", "Joel Alexander", "Benedict Neo", "Akhil Dhavala", "Van Nguyen", "Aditya Advani", "Sambuddha Basu", "DCsan", "Lucas Davis", "Dmitry Kozlov", "Jacob Wright", "brian kitano", "Joey Wang", "Henry Shi", "Matteo Palvarini", "Anam Hira", "Bhav Ashok", "Muneeb Saleem", "Joschka Braun", "Tony A. Liu", "Hamudi Naanaa", "Paul"])
    
