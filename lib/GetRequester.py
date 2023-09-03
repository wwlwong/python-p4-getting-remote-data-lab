import requests
import json

class GetRequester:

    #url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        json_list = []
        data_dicts = json.loads(self.get_response_body())
        for data_dict in data_dicts:
            json_list.append(data_dict)
        
        return json_list
