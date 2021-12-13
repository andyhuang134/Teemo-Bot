from riotwatcher import LolWatcher
from riotwatcher.exceptions import ApiError
import json


class JsonTools:
    def __init__(self):
        self.token_path = r"E:\Teemo-Bot-Private\token.json"
        self.summoner_path = r"E:\Teemo-Bot-Private\summoner.json"

    def json_save(self, summoner_name, summoner_info):
        self.json_format = {"username": summoner_name,
                            "user_data": summoner_info}

        with open(self.summoner_path, "r") as f:
            read_file = f.read()
            json_dict = json.loads(read_file)
            json_dict.append(self.json_format)

        with open(self.summoner_path, "w") as f:
            json.dump(json_dict, f, indent=4)

    def summoner_file(self):
        with open(self.summoner_path, "r") as f:
            read_file = f.read()
            json_dict = json.loads(read_file)
        return json_dict

    def token_file(self):
        with open(self.token_path, "r") as f:
            read_file = f.read()
            json_dict = json.loads(read_file)
        return json_dict


class Watcher:
    def __init__(self):
        self.summoner_file = JsonTools().summoner_file()
        self.key = JsonTools().token_file()[0]["riot_token"]
        self.region = "na1"
        self.watcher = LolWatcher(str(self.key))

    def check_summoner(self, summoner_name):
        for i in range(len(self.summoner_file)):
            if summoner_name == self.summoner_file[i]["username"]:
                return False
        return True

    def register_summoner(self, summoner_name):
        try:
            summoner = self.watcher.summoner.by_name(
                self.region, summoner_name)
            if self.check_summoner(summoner["name"]):
                JsonTools().json_save(summoner["name"], summoner)

            print(f'Summoner "{summoner_name}" already exists.')

        except ApiError as err:
            if err.response.status_code == 429:
                print('We should retry in {} seconds.'.format(
                    err.headers['Retry-After']))
                print(
                    'this retry-after is handled by default by the    RiotWatcher library')
                print('future requests wait until the retry-after time  passes')
            elif err.response.status_code == 404:
                print('Summoner with that ridiculous name not found.')
            else:
                raise

    def summoner_info(self, summoner_name):
        pass


lol = Watcher()
lol.register_summoner('lil weenie')
# lol.summoner_info('edigreg')
