'''
fapro.py is functions for farming/farmbot processes without cluttering up commands.py
some processes require extensive handling of API errors etc.
'''
import requests
import json
import random
import time
from threading import Timer
from colorama import init, Fore
init(autoreset=True)
import config
import utils.crypto as crypto
import utils.error as error
import utils.database as database
import api.ingame as ingame
import api.transfer as transfer
import api.auth as auth
import utils.funcs as funcs
import farming.autoteam as autoteam

# tutorial
def tutorial(ver, os, token, secret, iden):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        code = config.gb_code
    else:
        code = config.jp_code
    names = ['Abra', 'Armadillo', 'Beat', 'Berserker', 'Erito', 'Forte', 'Froze', 'Kabra', 'Kagyu', 'Mirego', 'Mizore', 'Nico', 'Nimu', 'Note', 'Pokoh', 'Rezok', 'Salaga', 'Tsumuri', 'Viola']
    if ver == 'gb':
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 10}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 20}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 30}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-global.aktsk.com/tutorial/gasha'
        auth = crypto.mac(ver, token, secret, 'POST', '/tutorial/gasha')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        requests.post(url, data=None, headers=headers)
        print('Tutorial 1/7 - Summon')
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 40}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-global.aktsk.com/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        name = random.randint(0, len(names) - 1)
        data = {'user': {'name': names[name]}}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 2/7 - Set name as "' + str(names[name]) + '"')
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 50}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 60}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 70}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 77}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 3/7 - Dragonball #3 / Defeat hercule')
        #######################
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 80}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-global.aktsk.com/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'user': {'is_ondemand': True}}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 4/7 - Update user')
        #######################
        url = 'https://ishin-global.aktsk.com/tutorial/finish'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial/finish')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        requests.put(url, data=None, headers=headers)
        print('Tutorial 5/7 - Finish battle')
        #######################
        url = 'https://ishin-global.aktsk.com/missions/put_forward'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/put_forward')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        requests.post(url, data=None, headers=headers)
        print('Tutorial 6/7 - Update missions')
        #######################
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 90}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-global.aktsk.com/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 999}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 7/7 - Tutorial complete')
        #######################
        url = 'https://ishin-global.aktsk.com/apologies/accept'
        auth = crypto.mac(ver, token, secret, 'PUT', '/apologies/accept')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        requests.put(url, data=None, headers=headers)
        print('Making gifts available...')
        #######################
        config.acc_ver, config.acc_os, config.sess_token, config.sess_secret = ver, os, token, secret
        save = funcs.createSaveFile(iden)
        config.loaded, config.account = save, iden
        funcs.checkDatabase()
    else:
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 10}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 20}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 30}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-production.aktsk.jp/tutorial/gasha'
        auth = crypto.mac(ver, token, secret, 'POST', '/tutorial/gasha')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        requests.post(url, data=None, headers=headers)
        print('Tutorial 1/7 - Summon')
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 40}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-production.aktsk.jp/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        name = random.randint(0, len(names) - 1)
        data = {'user': {'name': names[name]}}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 2/7 - Set name as "' + str(names[name]) + '"')
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 50}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 60}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 70}
        requests.put(url, data=json.dumps(data), headers=headers)
        #######################
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 77}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 3/7 - Dragonball #3 / Defeat hercule')
        #######################
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 80}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-production.aktsk.jp/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'user': {'is_ondemand': True}}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 4/7 - Update user')
        #######################
        url = 'https://ishin-production.aktsk.jp/tutorial/finish'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial/finish')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        requests.put(url, data=None, headers=headers)
        print('Tutorial 5/7 - Finish battle')
        #######################
        url = 'https://ishin-production.aktsk.jp/missions/put_forward'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/put_forward')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        requests.post(url, data=None, headers=headers)
        print('Tutorial 6/7 - Update missions')
        #######################
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 90}
        requests.put(url, data=json.dumps(data), headers=headers)
        url = 'https://ishin-production.aktsk.jp/tutorial'
        auth = crypto.mac(ver, token, secret, 'PUT', '/tutorial')
        headers = {'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua}
        data = {'progress': 999}
        requests.put(url, data=json.dumps(data), headers=headers)
        print('Tutorial 7/7 - Tutorial complete')
        #######################
        url = 'https://ishin-production.aktsk.jp/apologies/accept'
        auth = crypto.mac(ver, token, secret, 'PUT', '/apologies/accept')
        headers = { 'X-Platform': os, 'X-ClientVersion': code, 'X-AssetVersion': '////', 'X-DatabaseVersion': '////', 'Content-Type': 'application/json', 'Accept': '*/*', 'Authorization': auth, 'User-Agent': dua }
        requests.put(url, data=None, headers=headers)
        print('Making gifts available...')
        #######################
        config.acc_ver, config.acc_os, config.sess_token, config.sess_secret = ver, os, token, secret
        save = funcs.createSaveFile(iden)
        config.loaded, config.account = save, iden
        funcs.checkDatabase()
        print(Fore.LIGHTYELLOW_EX + 'type "help" for a list of commands.')

# card selling
def sellSpecific(uniqueCard):
    ids = []
    ids.append(int(uniqueCard))
    store = ingame.sell(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, ids)
    if 'error' not in store:
        print(Fore.GREEN + 'sold ' + str(len(ids)) + ' cards!')
    else:
        error.Handler('sold', store)

failed_sell_attempts = 0
def sellUseless():
    global failed_sell_attempts
    store = ingame.cards(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
    if 'error' not in store:
        print('gathering cards to sell...')
        store2 = ingame.getTeams(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        teams = []
        for x in store2['user_card_teams']:
            for j in x['user_card_ids']:
                teams.append(j)
        ids = []
        for i in store['cards']:
            if len(ids) <= 98 and i['id'] not in teams and i['is_favorite'] == False:
                # all N
                try:
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id'])) != None:
                        # all N
                        if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] is 0:
                            ids.append(i['id'])
                        # all R
                        if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] is 1:
                            ids.append(i['id'])
                    else:
                        print('card not in database.')
                except:
                    print('does the database exist?')
                # hercule statues
                statues = ['1002630', '1002640', '1002650', '1005480', '1011480', '1011481']
                if str(i['card_id']) in statues:
                    ids.append(i['id'])
        if len(ids) != 0:
            store = ingame.sell(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, ids)
            if 'error' not in store:
                print(Fore.GREEN + 'sold ' + str(len(ids)) + ' cards!')
            else:
                error.Handler('sold', store)
                failed_sell_attempts = failed_sell_attempts + 1
        else:
            if failed_sell_attempts > 0:
                ingame.capacity(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                print(Fore.GREEN + 'increased box capacity by 5+')
                failed_sell_attempts = 0
            else:
                print('no cards to sell.')
    else:
        error.Handler('sell', store)

def babaUseless():
    pass

# gift accept
def gifts():
    print('apologies/comeback/hercule gifts...')
    store = ingame.homeResources(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
    if 'error' not in store:
        presents = []
        # TODO comback
        # hercule
        if len(store['random_login_bonuses']) != 0:
            for i in store['random_login_bonuses']:
                if 'random_login_bonus' in i and 'token' in i:
                    store = ingame.claimRandomLogin(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, i['random_login_bonus']['elapsed_days'], i['expire'], i['random_login_bonus']['id'], i['token'])
                    if 'error' not in store:
                        print(Fore.LIGHTGREEN_EX + '\"' + str(i['announcement']['title']) + '\" claimed!')
                    else:
                        error.Handler('randomClaim', store)
                else:
                    print('no bonus or token.')
        else:
            print('none to claim.')
        # TODO apologies
    else:
        error.Handler('gift2', store)
    print('cumulative/consecutive/celebration gifts...')
    store = ingame.gifts(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
    if 'error' not in store:
        presents = []
        for i in store['gifts']:
            presents.append(i['id'])
        if len(presents) != 0:
            store2 = ingame.acceptGifts(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, presents)
            if 'error' not in store2:
                print(Fore.GREEN + 'accepted ' + str(len(presents)) + ' gifts.')
            else:
                error.Handler('gAccept1', store2)
        else:
            print('no gifts to accept!')
    else:
        error.Handler('gift1', store)

# mission claim
def missions():
    store = ingame.missions(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
    if 'error' not in store:
        missions = []
        db_ids = []
        accepted = []
        for i in store['missions']:
            if i['completed_at'] != None and i['accepted_reward_at'] == None:
                missions.append(i['id'])
                db_ids.append(i['mission_id'])
        if len(missions) != 0:
            store2 = ingame.acceptMissions(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, missions)
            if 'error' not in store2:
                print(Fore.GREEN + 'claimed ' + str(len(missions)) + ' missions.')
                for i in db_ids:
                    try:
                        accepted.append(database.fetch(config.acc_ver + '.db', 'missions', 'id=' + str(i))[3] + '\n' +
                                        database.fetch(config.acc_ver + '.db', 'mission_rewards', 'id=' + str(i))[3] + ' x' + str(
                            database.fetch(config.acc_ver + '.db', 'mission_rewards', 'id=' + str(i))[4]))
                    except:
                        accepted.append('unknown mission ID: ' + str(i))
                print(Fore.CYAN + ',\n'.join(accepted))
            else:
                error.Handler('mission accept', store2)
        else:
            print('no missions to claim!')
    else:
        error.Handler('mission', store)

# summon
def summon(bannerId, course):
    settings = funcs.getSettings()
    store = ingame.summon(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, bannerId, course)
    if 'error' not in store:
        cards = []
        element = '?'
        rarity = '?'
        if settings['display_only_ids'] != True:
            for i in store['gasha_items']:
                try:
                    db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[13]
                    if db_ele is 0 or db_ele is 10 or db_ele is 20:
                        element = Fore.CYAN + 'AGL'
                    if db_ele is 1 or db_ele is 11 or db_ele is 21:
                        element = Fore.GREEN + 'TEQ'
                    if db_ele is 2 or db_ele is 12 or db_ele is 22:
                        element = Fore.MAGENTA + 'INT'
                    if db_ele is 3 or db_ele is 13 or db_ele is 23:
                        element = Fore.RED + 'STR'
                    if db_ele is 4 or db_ele is 14 or db_ele is 24:
                        element = Fore.YELLOW + 'PHY'
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[6] is 0:
                        rarity = 'N'
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[6] is 1:
                        rarity = 'R'
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[6] is 2:
                        rarity = 'SR'
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[6] is 3:
                        rarity = 'SSR'
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[6] is 4:
                        rarity = 'UR'
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[6] is 5:
                        rarity = 'LR'
                    if settings['display_ids']:
                        cardId = ' (' + str(i['item_id']) + ')'
                    else:
                        cardId = ''
                    cards.append(
                        element + ' ' + rarity + ' ' +
                        database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[
                            1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['item_id']))[24]))[
                            1] + '] x' + str(
                            i['quantity']) + cardId)
                except:
                    if settings['display_ids']:
                        cardId = ' (' + str(i['item_id']) + ')'
                    else:
                        cardId = ''
                    cards.append('unknown (' + str(i['item_id']) + ') x' + str(i['quantity']) + cardId)
        else:
            for i in store['gasha_items']:
                cards.append(str(i['item_id']) + ' x' + str(i['quantity']))
        print(',\n'.join(cards))
        if settings['potential_node'] != True:
            pass
            # sort box for already existing id / awakening id with most dupes
            # if none do nothing
            # if exists if awakening id then reverse
            # else unlock node w/ dupe & not reverse
    else:
        error.Handler('summon', store)

# stam restore
def restore():
    settings = funcs.getSettings()
    if settings['stam_use_stone'] == True:
        store = ingame.user(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, False)
        if int(store['user']['stone']) >= 1:
            print('refilling stamina...')
            store = ingame.actRefill(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
            if 'error' not in store:
                print(Fore.GREEN + 'stamina restored.')
            else:
                error.Handler('restore', store)
        else:
            print('not enough stones.')
    else:
        print(Fore.LIGHTRED_EX + 'Use stones is set to "OFF"')

# reward organize
def rewards(which, drops):
    rewards = []
    settings = funcs.getSettings()
    if which == 'stage':
        if settings['display_drops'] == True:
            if 'zeni' in drops:
                rewards.append('Zeni: ' + str(drops['zeni']))
            if 'gasha_point' in drops:
                rewards.append('FP: ' + str(drops['gasha_point']))
            if 'quest_clear_rewards' in drops:
                for x in drops['quest_clear_rewards']:
                    if x['item_type'] == 'Point::Stone':
                        rewards.append('Stone x' + str(x['amount']))
            if 'items' in drops:
                for x in drops['items']:
                    if x['item_type'] == 'SupportItem':
                        try:
                            rewards.append(
                                database.fetch(config.acc_ver + '.db', 'support_items', 'id=' + str(x['item_id']))[
                                    1] + ' x' + str(
                                    x['quantity']))
                        except:
                            rewards.append('support x' + str(x['quantity']))
                    if x['item_type'] == 'PotentialItem':
                        try:
                            rewards.append(
                                database.fetch(config.acc_ver + '.db', 'potential_items', 'id=' + str(x['item_id']))[
                                    1] + ' x' + str(
                                    x['quantity']))
                        except:
                            rewards.append('orb x' + str(x['quantity']))
                    if x['item_type'] == 'TrainingItem':
                        try:
                            rewards.append(
                                database.fetch(config.acc_ver + '.db', 'training_items', 'id=' + str(x['item_id']))[
                                    1] + ' x' + str(
                                    x['quantity']))
                        except:
                            rewards.append('training item x' + str(x['quantity']))
                    if x['item_type'] == 'AwakeningItem':
                        try:
                            rewards.append(
                                database.fetch(config.acc_ver + '.db', 'awakening_items', 'id=' + str(x['item_id']))[
                                    1] + ' x' + str(
                                    x['quantity']))
                        except:
                            rewards.append('medal x' + str(x['quantity']))
                    if x['item_type'] == 'TreasureItem':
                        try:
                            rewards.append(
                                database.fetch(config.acc_ver + '.db', 'treasure_items', 'id=' + str(x['item_id']))[
                                    1] + ' x' + str(
                                    x['quantity']))
                        except:
                            rewards.append('treasure x' + str(x['quantity']))
                    if x['item_type'] == 'Card':
                        try:
                            element = ''
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(x['item_id']))[13]
                            if db_ele is 0 or db_ele is 10 or db_ele is 20:
                                element = 'AGL'
                            if db_ele is 1 or db_ele is 11 or db_ele is 21:
                                element = 'TEQ'
                            if db_ele is 2 or db_ele is 12 or db_ele is 22:
                                element = 'INT'
                            if db_ele is 3 or db_ele is 13 or db_ele is 23:
                                element = 'STR'
                            if db_ele is 4 or db_ele is 14 or db_ele is 24:
                                element = 'PHY'
                            rewards.append(
                                element + ' ' +
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(x['item_id']))[1] + ' [' +
                                database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                    database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(x['item_id']))[24]))[
                                    1] + '] x' + str(
                                    x['quantity']))
                        except:
                            rewards.append('card x' + str(x['quantity']))
            if 'dragonballs' in drops:
                for x in drops['dragonballs']:
                    rewards.append('Dragonball #' + str(x['num']))
        else:
            if 'zeni' in drops:
                rewards.append('Zeni: ' + str(drops['zeni']))
            if 'gasha_point' in drops:
                rewards.append('FP: ' + str(drops['gasha_point']))
            if 'quest_clear_rewards' in drops:
                for x in drops['quest_clear_rewards']:
                    if x['item_type'] == 'Point::Stone':
                        rewards.append('Stone x' + str(x['amount']))
            if 'items' in drops:
                for x in drops['items']:
                    if x['item_type'] == 'SupportItem':
                        rewards.append('support x' + str(x['quantity']))
                    if x['item_type'] == 'PotentialItem':
                        rewards.append('orb x' + str(x['quantity']))
                    if x['item_type'] == 'TrainingItem':
                        rewards.append('training item x' + str(x['quantity']))
                    if x['item_type'] == 'AwakeningItem':
                        rewards.append('medal x' + str(x['quantity']))
                    if x['item_type'] == 'TreasureItem':
                        rewards.append('treasure x' + str(x['quantity']))
                    if x['item_type'] == 'Card':
                        rewards.append('card x' + str(x['quantity']))
            if 'dragonballs' in drops:
                for x in drops['dragonballs']:
                    rewards.append('Dragonball #' + str(x['num']))
    if which == 'eza':
        if settings['display_drops']:
            if 'user' in drops:
                if 'zeni' in drops['user']:
                    rewards.append('Zeni: ' + str(drops['user']['zeni']))
                if 'gasha_point' in drops['user']:
                    rewards.append('FP: ' + str(drops['user']['gasha_point']))
                if 'exchange_point' in drops['user']:
                    rewards.append('BP: ' + str(drops['user']['exchange_point']))
                if 'stone' in drops['user']:
                    rewards.append('Stones: ' + str(1))
            if 'cards' in drops:
                for x in drops['cards']:
                    try:
                        element = ''
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(x['card_id']))[13]
                        if db_ele is 0 or db_ele is 10 or db_ele is 20:
                            element = 'AGL'
                        if db_ele is 1 or db_ele is 11 or db_ele is 21:
                            element = 'TEQ'
                        if db_ele is 2 or db_ele is 12 or db_ele is 22:
                            element = 'INT'
                        if db_ele is 3 or db_ele is 13 or db_ele is 23:
                            element = 'STR'
                        if db_ele is 4 or db_ele is 14 or db_ele is 24:
                            element = 'PHY'
                        rewards.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(x['card_id']))[
                                1] + ' [' +
                            database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(x['card_id']))[24]))[
                                1] + '] x1')
                    except:
                        rewards.append('card x1')
            if 'awakening_items' in drops:
                for x in drops['awakening_items']:
                    try:
                        rewards.append(database.fetch(config.acc_ver + '.db', 'awakening_items',
                                                      'id=' + str(x['awakening_item_id']))[
                                           1] + ' x' + str(x['quantity']))
                    except:
                        rewards.append('medal x' + str(x['quantity']))
            if 'potential_items' in drops:
                for x in drops['potential_items']:
                    try:
                        rewards.append(database.fetch(config.acc_ver + '.db', 'potential_items',
                                                      'id=' + str(x['potential_item_id']))[
                                           1] + ' x' + str(x['quantity']))
                    except:
                        rewards.append('orb x' + str(x['quantity']))
        else:
            if 'user' in drops:
                if 'zeni' in drops['user']:
                    rewards.append('Zeni: ' + str(drops['user']['zeni']))
                if 'gasha_point' in drops['user']:
                    rewards.append('FP: ' + str(drops['user']['gasha_point']))
                if 'exchange_point' in drops['user']:
                    rewards.append('BP: ' + str(drops['user']['exchange_point']))
                if 'stone' in drops['user']:
                    rewards.append('Stones: ' + str(1))
            if 'cards' in drops:
                for x in drops['cards']:
                    rewards.append('card x1')
            if 'awakening_items' in drops:
                for x in drops['awakening_items']:
                    rewards.append('medal x' + str(x['quantity']))
            if 'potential_items' in drops:
                for x in drops['potential_items']:
                    rewards.append('orb x' + str(x['quantity']))
    if which == 'clash':
        if settings['display_drops']:
            if 'items' in drops:
                for x in drops['items']:
                    if x['item_type'] == 'Point::Stone':
                        rewards.append('Stone x' + str(x['quantity']))
                    if x['item_type'] == 'TreasureItem':
                        try:
                            rewards.append(
                                database.fetch(config.acc_ver + '.db', 'treasure_items', 'id=' + str(x['item_id']))[
                                    1] + ' x' + str(x['quantity']))
                        except:
                            rewards.append('treasure x' + str(x['quantity']))
        else:
            if 'items' in drops:
                for x in drops['items']:
                    if x['item_type'] == 'Point::Stone':
                        rewards.append('Stone x' + str(x['quantity']))
                    if x['item_type'] == 'TreasureItem':
                        rewards.append('treasure x' + str(x['quantity']))
    print(Fore.CYAN + ',\n'.join(rewards))

# pick support & build team according to conditions
def handleCondition(limits, cards, stage):
    friend = cards[0]['id']
    friend_card = cards[0]['leader']['card_id']
    if limits != None:
        settings = funcs.getSettings()
        if settings['team_builder'] == True:
            built = autoteam.build(limits, cards, stage)
            if built[0] != None and built[1] != None:
                friend = built[0]
                friend_card = built[1]
    return [friend, friend_card]

# generate simulated map movement
def simulateMap(sugoroku, which, enemies = None):
    if which == 'stage':
        # 5010:0
        paces = []
        defeated = []
        for i in sugoroku['events'].keys():
            paces.append(int(i))
        for i in sugoroku['events']:
            if 'battle_info' in sugoroku['events'][i]['content']:
                for j in sugoroku['events'][i]['content']['battle_info']:
                    defeated.append(j['round_id'])
        return [paces, defeated]
    if which == 'round':
        dice = random.randint(0, 6)

# run stage
def runStage(stage, difficulty, kagi):
    # stage information
    settings = funcs.getSettings()
    if settings['display_stage_names']:
        try:
            if len(str(stage)) == 4:
                area = database.fetch(config.acc_ver + '.db', 'areas', 'id=' + str(stage)[0:1])[4]
                name = database.fetch(config.acc_ver + '.db', 'quests', 'id=' + str(stage))[2]
            if len(str(stage)) == 5:
                area = database.fetch(config.acc_ver + '.db', 'areas', 'id=' + str(stage)[0:2])[4]
                name = database.fetch(config.acc_ver + '.db', 'quests', 'id=' + str(stage))[2]
            if len(str(stage)) == 6:
                area = database.fetch(config.acc_ver + '.db', 'areas', 'id=' + str(stage)[0:3])[4]
                name = database.fetch(config.acc_ver + '.db', 'quests', 'id=' + str(stage))[2]
            match = str(area) + ' - ' + str(name) + ' (' + str(stage) + ':' + str(difficulty) + ')'
        except:
            area = 'unknown'
            name = 'unknown'
            match = str(name) + ' (' + str(stage) + ':' + str(difficulty) + ')'
    else:
        match = str(stage) + ':' + str(difficulty)
        name = match
    print(Fore.LIGHTYELLOW_EX + match)
    # support
    store = ingame.getSupports(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, stage, difficulty)
    if 'error' not in store:
        difficulties = ['normal', 'hard', 'very_hard', 'super_hard1', 'super_hard2', 'super_hard3']
        friend = None
        friend_card = None
        if len(str(stage)) == 4 or len(str(stage)) == 5:
            supports = handleCondition(None, store['supporters'], stage)
            friend = supports[0]
            friend_card = supports[1]
        else:
            if int(database.fetch(config.acc_ver + '.db', 'sugoroku_maps', 'quest_id=' + str(stage))[17]) == 1:
                events = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                for event in events['events']:
                    if str(event['id']) == str(stage)[0:3]:
                        for i in event['quests']:
                            if 'limitations' in i and len(i['limitations']) != 0:
                                supports = handleCondition(i['limitations'], store['cpu_supporters'][str(difficulties[int(difficulty)])]['cpu_friends'], stage)
                                friend = supports[0]
                                friend_card = supports[1]
                                break
                            else:
                                supports = handleCondition(None, store['cpu_supporters'][str(difficulties[int(difficulty)])]['cpu_friends'], stage)
                                friend = supports[0]
                                friend_card = supports[1]
                                break
            else:
                events = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                for event in events['events']:
                    if str(event['id']) == str(stage)[0:3]:
                        for i in event['quests']:
                            if 'limitations' in i and len(i['limitations']) != 0:
                                supports = handleCondition(i['limitations'], store['supporters'], stage)
                                friend = supports[0]
                                friend_card = supports[1]
                                break
                            else:
                                supports = handleCondition(None, store['supporters'], stage)
                                friend = supports[0]
                                friend_card = supports[1]
                                break
        # start
        timer_start = int(round(time.time(), 0))
        store = ingame.startStage(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, stage, difficulty, friend, friend_card)
        if 'error' not in store:
            data = crypto.decrypt_sign(store['sign'])
            stoken = data['token']
            mapData = simulateMap(data['sugoroku'], 'stage', None)
            paces, defeated = mapData[0], mapData[1]
            # finish
            store = ingame.finishStage(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, stage, difficulty, paces, defeated, stoken)
            if 'error' not in store:
                # rewards
                timer_finish = int(round(time.time(), 0))
                timer_total = timer_finish - timer_start
                print(Fore.GREEN + 'completed: ' + name + ' in ' + str(timer_total) + ' seconds.')
                data = crypto.decrypt_sign(store['sign'])
                rewards('stage', data)
            else:
                error.Handler('finish', store)
        else:

            error.Handler('start', store)

            if store['error']['code'] == 'act_is_not_enough':
                restore()
                runStage(stage, difficulty, kagi)
            if 'the_number_of_cards_must_be_less_than_or_equal_to_the_capacity' in store['error']['code']:
                sellUseless()
                runStage(stage, difficulty, kagi)
    else:
        error.Handler('support', store)
        if 'invalid_token' in store['error']:
            funcs.refresh()
            runStage(stage, difficulty, kagi)

# run eza level
def runZLvl(eza, level):
    # level information
    settings = funcs.getSettings()
    if settings['display_stage_names']:
        if len(str(eza)) >= 1:
            try:
                area = database.fetch(config.acc_ver + '.db', 'z_battle_stage_views', 'z_battle_stage_id=' + str(eza))[3]
            except:
                area = 'unknown #' + str(eza)
    else:
        area = str(eza)
    print(Fore.LIGHTYELLOW_EX + str(area) + ' EZA - Level ' + str(level))
    em_hp = []
    em_atk = 0
    # support
    store = ingame.zSupports(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, eza)
    if 'error' not in store:
        friend = store['supporters'][0]['id']
        friend_card = store['supporters'][0]['leader']['card_id']
        timer_start = int(round(time.time(), 0))
        # start
        store = ingame.zStart(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, eza, level, friend, friend_card)
        if 'error' not in store:
            dec_sign = crypto.decrypt_sign(store['sign'])
            for i in dec_sign['enemies'][0]:
                em_hp.append(i['hp'])
                em_atk = int(em_atk) + int(i['attack'])
            stoken = dec_sign['token']
            # end
            store = ingame.zFinish(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, eza, level, stoken, em_atk, em_hp)
            if 'error' not in store:
                # rewards
                timer_finish = int(round(time.time(), 0))
                timer_total = timer_finish - timer_start
                print(Fore.GREEN + 'completed level: ' + str(level) + ' in ' + str(timer_total) + ' seconds.')
                dec_sign = crypto.decrypt_sign(store['sign'])
                rewards('eza', dec_sign['user_items'])
            else:
                error.Handler('zfinish', store)
        else:
            error.Handler('zstart', store)
    else:
        error.Handler('zsupport', store)
        if 'invalid_token' in store['error']:
            funcs.refresh()
            runZLvl(eza, level)

# run clash level
def runClashLvl(clash, level, cards, begin):
    # level information
    print(Fore.LIGHTYELLOW_EX + 'starting Clash #' + str(clash) + ' - lvl. ' + str(level) + '...')
    leader = cards[0]
    cards.remove(cards[0])
    sub = cards[1]
    cards.remove(cards[1])
    team = []
    for i in cards:
        if len(team) < 5:
            team.append(i)
        else:
            break
    # start
    store = ingame.clashStart(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, clash, level, begin, leader, sub, team)
    if 'error' not in store:
        data = crypto.decrypt_sign(store['sign'])
        hp = data['continuous_info']['remaining_hp']
        round = data['continuous_info']['round']
        stoken = data['token']
        # end
        store = ingame.clashEnd(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, clash, hp, round, stoken)
        if 'error' not in store:
            # rewards
            print(Fore.GREEN + 'completed: lvl. ' + str(level))
            if 'sign' in store:
                data = crypto.decrypt_sign(store['sign'])
                rewards('clash', data)
            else:
                #print(store)
                rewards('clash', store)
        else:
            error.Handler('bfEnd', store)
    else:
        error.Handler('bfStart', store)
        print(str(clash) + ' - ' + str(level))
        # "{'error': {'code': 'stage_not_found_in_current_rmbattle_level'}}"

# streamline - from last to finish
def streamline(which):
    if which == 'quests':
        user = ingame.user(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, False)
        if 'error' not in user:
            if int(user['user']['stone']) >= 1:
                areas = ingame.quests(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                # user_areas -> area_id -> user_sugoroku_maps -> sugoroku_map_id, cleared_count
                maps = []
                for i in areas['user_areas']:
                    if i['area_id'] <= 27:
                        for j in i['user_sugoroku_maps']:
                            if j['cleared_count'] == 0:
                                maps.append(j['sugoroku_map_id'])
                if len(maps) == 0:
                    print('no quests to complete.')
                else:
                    f = open('./farming/quests.txt', 'r')
                    content = f.read()
                    f.close()
                    quests = content.split('\n')
                    print('getting last stage cleared...')
                    for i in quests:
                        if int(i) >= int(maps[0]):
                            runStage(str(i)[:-1], str(i)[-1], None)
            else:
                print('not enough stones.')
        else:
            error.Handler('qUser', user)
    if which == 'events':
        user = ingame.user(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, False)
        if 'error' not in user:
            if int(user['user']['stone']) >= 1:
                events = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                event_ids = []
                for event in events['events']:
                    event_ids.append(event['id'])
                    event_ids = sorted(event_ids)
                    try:
                        event_ids.remove(135)
                    except:
                        None
                # Complete areas if they are in the current ID pool
                areas = ingame.quests(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                i = 1
                for area in areas['user_areas']:
                    if area['area_id'] in event_ids:
                        for stage in area['user_sugoroku_maps']:
                            if stage['cleared_count'] == 0:
                                runStage(str(stage['sugoroku_map_id'])[:-1], str(stage['sugoroku_map_id'])[-1], None)
                    if i % 30 == 0:
                        funcs.refresh()
            else:
                print('not enough stones.')
        else:
            error.Handler('eUser', user)
    if which == 'ezas':
        store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            eza_pool = []
            for x in store['z_battle_stages']:
                eza_pool.append(int(x['id']))
            store = ingame.quests(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
            for i in eza_pool:
                for x in store['user_z_battles']:
                    if int(x['z_battle_stage_id']) == int(i):
                        clear_count = int(x['max_clear_level'])
                        if clear_count == 0:
                            clear_count = clear_count + 1
                        if clear_count < 30:
                            while int(clear_count) <= 30:
                                if clear_count != 0:
                                    runZLvl(int(i), int(clear_count))
                                    clear_count = clear_count + 1
                        else:
                            print(Fore.LIGHTCYAN_EX + 'This EZA has already been cleared.')
        else:
            error.Handler('eza-events', store)
    if which == 'clash':
        # current clash
        store = ingame.homeResources(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            if 'id' in store['rmbattles']:
                clash = store['rmbattles']['id']
                # current lvl
                store = ingame.clashInfo(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, clash)
                if 'error' not in store:
                    # {'defeated_stages_count': 0, 'max_defeated_stages_count': 10, 'rmbattle_bgm_pattern_id': 1, 'level_stages': {'1': [{'id': 15010, 'position': 1, 'is_boss': False, 'total_hp': 5000000, 'remaining_hp': 5000000, 'card_id': 51003531, 'element': 10, 'enemy_skill_ids': [50000, 50030]}, {'id': 15011, 'position': 5, 'is_boss': True, 'total_hp': 6000000, 'remaining_hp': 6000000, 'card_id': 54000201, 'element': 24, 'enemy_skill_ids': [50000, 50030, 50040, 50120]}], '2': [{'id': 15020, 'position': 1, 'is_boss': False, 'total_hp': 8000000, 'remaining_hp': 8000000, 'card_id': 53006361, 'element': 21, 'enemy_skill_ids': [50010, 50030, 50040, 50050]}, {'id': 15021, 'position': 2, 'is_boss': False, 'total_hp': 16000000, 'remaining_hp': 16000000, 'card_id': 55010991, 'element': 13, 'enemy_skill_ids': [50010, 50050]}, {'id': 15022, 'position': 5, 'is_boss': True, 'total_hp': 9250000, 'remaining_hp': 9250000, 'card_id': 53009111, 'element': 22, 'enemy_skill_ids': [50010, 50030, 50040, 50050]}], '3': [{'id': 15030, 'position': 1, 'is_boss': False, 'total_hp': 8500000, 'remaining_hp': 8500000, 'card_id': 57011071, 'element': 13, 'enemy_skill_ids': [50020, 50030, 50050]}, {'id': 15031, 'position': 2, 'is_boss': False, 'total_hp': 7400000, 'remaining_hp': 7400000, 'card_id': 53011391, 'element': 12, 'enemy_skill_ids': [50020, 50030, 50040, 4470]}, {'id': 15032, 'position': 3, 'is_boss': False, 'total_hp': 11000000, 'remaining_hp': 11000000, 'card_id': 51011011, 'element': 21, 'enemy_skill_ids': [50020, 50030, 50040, 50050, 50130]}, {'id': 15033, 'position': 4, 'is_boss': False, 'total_hp': 15000000, 'remaining_hp': 15000000, 'card_id': 57014011, 'element': 14, 'enemy_skill_ids': [50020, 50040, 50060]}, {'id': 15034, 'position': 5, 'is_boss': True, 'total_hp': 15750000, 'remaining_hp': 15750000, 'card_id': 51005001, 'element': 20, 'enemy_skill_ids': [50020, 50030, 50100, 50110]}]}}
                    if 'current_level_info' in store:
                        currentLvl = int(store['current_level_info']['level'])
                    else:
                        currentLvl = 1
                    # usable lvl cards
                    cards = ingame.clashCards(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, 1)
                    #print(cards)
                    if 'sortiable_user_card_ids' in cards:
                        team = cards['sortiable_user_card_ids']
                        begin = False
                    elif 'user_card_ids' in cards:
                        team = cards['user_card_ids']
                        begin = True
                    elif 'current_level_info' in cards:
                        team = cards['current_level_info']['sortiable_user_card_ids']
                    # loop levels
                    for i in store['level_stages'].keys():
                        # if begin == False and currentLvl == int(i):
                        #   i = currentLvl
                        for x in store['level_stages'][i]:
                            if int(x['remaining_hp']) != 0:
                                if 'sortiable_user_card_ids' in x:
                                    team = x['sortiable_user_card_ids']
                                    begin = False
                                runClashLvl(clash, x['id'], team, begin)
                else:
                    error.Handler('clashInfo', store)
            else:
                print(Fore.LIGHTRED_EX + 'clash isn\'t active!')
        else:
            error.Handler('resources1', store)
    # area streamline
    if isinstance(which, int) and len(which) == 3:
        pass