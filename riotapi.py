from riotwatcher import LolWatcher
from riotwatcher.exceptions import ApiError

# variables
key = 'RGAPI-88c82941-3c96-4e4c-9dbd-0fd435f487b2'
watcher = LolWatcher(key)
summoner_names = []
visible_summoner_names = []
visible_stats = []
champion_id = []
available_chests = []

# Functions


def register_summoner(summonerName):
    global current_summoner
    try:
        summoner = watcher.summoner.by_name('na1', summonerName)
        summoner_names.append(summoner['name'].lower())
        visible_summoner_names.append(summoner['name'])
    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(
                err.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise


# prints out summoner stats

def print_stats(summonerName):
    summoner = watcher.summoner.by_name('na1', summonerName)
    stats = watcher.league.by_summoner('na1', summoner['id'])

    print(stats)  # used to check more info

    if not stats:  # if they don't have ranked games in any gamemodes
        stats_1 = f"{summoner['name']}\nRanked Solo: None\nRanked Flex: None"
        visible_stats.append(stats_1)
        print(stats_1)

    if stats:
        print(stats[0]['summonerName'])
        for i in range(len(stats)):

            # gets the rank info of solo q and flex q
            tier = stats[i]['tier']
            rank = stats[i]['rank']
            lp = stats[i]['leaguePoints']

            wins = int(stats[i]['wins'])
            losses = int(stats[i]['losses'])
            winrate = int((wins / (wins + losses)) * 100)
            total = wins + losses

            ranked_type = ''
            if stats[i]['queueType'] == 'RANKED_FLEX_SR':
                ranked_type = 'Ranked Flex'
            if stats[i]['queueType'] == 'RANKED_SOLO_5x5':
                ranked_type = 'Ranked Solo'

            stats_2 = f'{ranked_type}: {tier} {rank} {lp}LP | {winrate}% Winrate {wins}W {losses}L ({total} Total)'
            visible_stats.append(stats_2)
            print(stats_2)


def hextech_chest(summonerName):

    watcher.data_dragon.champions

    summoner = watcher.summoner.by_name('na1', summonerName)
    champion_mastery = watcher.champion_mastery.by_summoner(
        'na1', summoner['id'])
    # gets champion id of champions without a chest
    for i in range(len(champion_mastery)):
        if champion_mastery[i]['chestGranted'] == False:
            champion_id.append(str(champion_mastery[i]['championId']))
        if champion_mastery[i]['chestGranted'] == True:
            continue

    champions()


def champions():
    versions = watcher.data_dragon.versions_for_region('na1')
    champions_version = versions['n']['champion']
    current_champ_list = watcher.data_dragon.champions(champions_version)
    champion_list = current_champ_list['data']

    # gets the correct champions correspoding with the champion id and gets the name of the champion
    for i in champion_list:
        if champion_list[i]['key'] in champion_id:
            available_chests.append(champion_list[i]['name'])
        elif champion_list[i]['key'] not in champion_id:
            continue

    # print(available_chests)
    # print(champion_id)
    # print(len(available_chests))
