from bardapi import Bard
import os

bard_token = os.getenv('BARD_TOKEN')
bard = Bard(token=bard_token)

def ask_internet(names):
    def find_info_from_name(name: str):
        prompt = f"In order to effectively prepare for an upcoming meeting with {name}. I require a thorough and detailed analysis of this group taking into account their individual backgrounds, personalities, aspirations, and beliefs. Furthermore, I am seeking strategies and approaches to successfully communicate and inspire them with my idea, which centers around the gradual implementation of AI for efficient and ethical government management in the future."
        return bard.get_answer(prompt)['content']

    def find_info_from_names(names: str | list):
        if isinstance(names, list):
            names = ', '.join(names)
        prompt = f"In order to effectively prepare for an upcoming meeting with {names}, I require a thorough and detailed analysis of this group taking into account their individual backgrounds, personalities, aspirations, and beliefs. Furthermore, I am seeking strategies and approaches to successfully communicate and inspire them with my idea, which centers around the gradual implementation of AI for efficient and ethical government management in the future."
        return bard.get_answer(prompt)
    
    return find_info_from_names(names)