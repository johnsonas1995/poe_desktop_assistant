import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

class APIs:
    def __init__(self, app):
        self.app = app
        
        
        
    def getStashTabs(self, league, tab_index):
        stash_token = os.environ.get("STASH_TOKEN", None)
        endpoint = 'https://www.pathofexile.com/character-window/get-stash-items'
        data = {
            'accountName': 'DarthValdo',
            'league': league,
            'realm': 'pc',
            'tabIndex': tab_index,
            'tabs': 1,
        }
        headers = {
            'user-agent': 'School API Project/0.0.1 (contact: toxicity.aj@gmail.com)',
            'Authorization': 'Bearer ' + stash_token,
        }
        response = requests.post(endpoint, headers=headers, data=data)
        response = response.text
        
        parsed = json.loads(response)
        print(parsed)
        return parsed