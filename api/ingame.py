import requests
import config
import crypto
import json
import time
import random
from random import choice
from random import randint
from string import ascii_uppercase

# account information
def user(ver, os, token, secret, first):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user'
        auth = crypto.mac(ver, token, secret, 'GET', '/user')
        if first == False:
            code = '////'
        else:
            code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user'
        auth = crypto.mac(ver, token, secret, 'GET', '/user')
        if first == False:
            code = config.jp_code
        else:
            code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# box contents
def cards(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/cards'
        auth = crypto.mac(ver, token, secret, 'GET', '/cards')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/cards'
        auth = crypto.mac(ver, token, secret, 'GET', '/cards')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# current news
def news(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/announcements?display=home'
        auth = crypto.mac(ver, token, secret, 'GET', '/announcements?display=home')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/announcements?display=home'
        auth = crypto.mac(ver, token, secret, 'GET', '/announcements?display=home')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# current banners
def banners(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gashas'
        auth = crypto.mac(ver, token, secret, 'GET', '/gashas')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gashas'
        auth = crypto.mac(ver, token, secret, 'GET', '/gashas')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# current events
def events(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/events'
        auth = crypto.mac(ver, token, secret, 'GET', '/events')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/events'
        auth = crypto.mac(ver, token, secret, 'GET', '/events')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# change account name
def changeName(ver, os, token, secret, name):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'user':{'name': name}}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# increase box size by 5
def capacity(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/capacity/card'
        auth = crypto.mac(ver, token, secret, 'POST', '/user/capacity/card')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user/capacity/card'
        auth = crypto.mac(ver, token, secret, 'POST', '/user/capacity/card')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.post(url, data=None, headers=headers)
    return r.json()

# starter banner status
def dashStatus(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/start_dash_gasha_status'
        auth = crypto.mac(ver, token, secret, 'GET', '/start_dash_gasha_status')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/start_dash_gasha_status'
        auth = crypto.mac(ver, token, secret, 'GET', '/start_dash_gasha_status')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# summon on a banner
def summon(ver, os, token, secret, id, course):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gashas/' + str(id) + '/courses/' + str(course) + '/draw'
        auth = crypto.mac(ver, token, secret, 'POST', '/gashas/' + str(id) + '/courses/' + str(course) + '/draw')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gashas/' + str(id) + '/courses/' + str(course) + '/draw'
        auth = crypto.mac(ver, token, secret, 'POST', '/gashas/' + str(id) + '/courses/' + str(course) + '/draw')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.post(url, data=None, headers=headers)
    return r.json()

# list of gifts
def gifts(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gifts'
        auth = crypto.mac(ver, token, secret, 'GET', '/gifts')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gifts'
        auth = crypto.mac(ver, token, secret, 'GET', '/gifts')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# accept gifts
def acceptGifts(ver, os, token, secret, gift):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gifts/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/gifts/accept')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gifts/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/gifts/accept')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'gift_ids': gift}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# list of missions
def missions(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/missions'
        auth = crypto.mac(ver, token, secret, 'GET', '/missions')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/missions'
        auth = crypto.mac(ver, token, secret, 'GET', '/missions')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# accept missions
def acceptMissions(ver, os, token, secret, mission):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/missions/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/accept')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/missions/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/accept')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'mission_ids': mission}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# stone stamina refill
def actRefill(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/recover_act_with_stone'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user/recover_act_with_stone')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user/recover_act_with_stone'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user/recover_act_with_stone')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.put(url, data=None, headers=headers)
    return r.json()

# sell cards
def sell(ver, os, token, secret, card):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/cards/sell'
        auth = crypto.mac(ver, token, secret, 'POST', '/cards/sell')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/cards/sell'
        auth = crypto.mac(ver, token, secret, 'POST', '/cards/sell')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'card_ids': card}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# set wallpaper
def setWallpaper(ver, os, token, secret, wallpaper):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'user': {'wallpaper_item_id': wallpaper}}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# story stages
def quests(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user_areas'
        auth = crypto.mac(ver, token, secret, 'GET', '/user_areas')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user_areas'
        auth = crypto.mac(ver, token, secret, 'GET', '/user_areas')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# stage supports
def getSupports(ver, os, token, secret, stage, difficulty):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/quests/' + str(stage) + '/supporters'
        auth = crypto.mac(ver, token, secret, 'GET', '/quests/' + str(stage) + '/supporters')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/quests/' + str(stage) + '/supporters'
        auth = crypto.mac(ver, token, secret, 'GET', '/quests/' + str(stage) + '/supporters')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all medals
def getMedals(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/awakening_items'
        auth = crypto.mac(ver, token, secret, 'GET', '/awakening_items')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/awakening_items'
        auth = crypto.mac(ver, token, secret, 'GET', '/awakening_items')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all items (orbs, training, support, treasure, special)
def getItems(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all potential orbs
def getOrbs(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=true&training_items=false&support_items=false&treasure_items=false&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=true&training_items=false&support_items=false&treasure_items=false&special_items=false')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=true&training_items=false&support_items=false&treasure_items=false&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=true&training_items=false&support_items=false&treasure_items=false&special_items=false')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all training items
def getTrainingItems(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=false&training_items=true&support_items=false&treasure_items=false&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=true&support_items=false&treasure_items=false&special_items=false')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=false&training_items=true&support_items=false&treasure_items=false&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=true&support_items=false&treasure_items=false&special_items=false')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all support items
def getSupportItems(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=false&training_items=false&support_items=true&treasure_items=false&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=false&support_items=true&treasure_items=false&special_items=false')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=false&training_items=false&support_items=true&treasure_items=false&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=false&support_items=true&treasure_items=false&special_items=false')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all treasure
def getTreasureItems(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=true&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=true&special_items=false')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=true&special_items=false'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=true&special_items=false')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all special items (tickets etc)
def getSpecialItems(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=false&special_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=false&special_items=true')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=false&special_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=false&training_items=false&support_items=false&treasure_items=false&special_items=true')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

def getTeams(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'GET', '/teams')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'GET', '/teams')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

def setTeam(ver, os, token, secret, team, cards):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'POST', '/teams')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'POST', '/teams')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'selected_team_num': int(team), 'user_card_teams': cards}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# start a stage by ID & difficulty
def startStage(ver, os, token, secret, stage, difficulty, friend, friend_card):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/quests/' + str(stage) + '/sugoroku_maps/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/start')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/quests/' + str(stage) + '/sugoroku_maps/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/start')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2

    APIToken = ''.join(random.choice(list('abcdefghijklmnopqrstuvwxyzBCDEFGHIKLMNOPQRUVWXYZ123456789-_')) for i in range(63))

    decks = getTeams(ver, os, token, secret)

    if len(str(friend)) >= 4:
        sign = json.dumps({'difficulty': int(difficulty), 'friend_id': int(friend), 'is_playing_script': True, 'selected_team_num': int(decks['selected_team_num']), 'support_leader': {'card_id': int(friend_card), 'exp': 0, 'optimal_awakening_step': 0, 'released_rate': 0}})
        enc_sign = crypto.encrypt_sign(sign)
    else:
        sign = json.dumps({'difficulty': int(difficulty), 'cpu_friend_id': int(friend), 'is_playing_script': True, 'selected_team_num': int(decks['selected_team_num'])})
        enc_sign = crypto.encrypt_sign(sign)

    headers = {
        'User-Agent': dua,
        'Accept': '*/*',
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Platform': os,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'X-ClientVersion': code
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# finish stage by ID & difficulty
def finishStage(ver, os, token, secret, stage, difficulty, paces, defeated, stoken):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/quests/' + str(stage) + '/sugoroku_maps/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/finish')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/quests/' + str(stage) + '/sugoroku_maps/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/finish')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
        
    steps = []
    for x in paces:
        steps.append(x)

    finish = int(round(time.time(), 0) + 90)
    start = finish - randint(6200000, 8200000)
    damage = randint(500000, 1000000)

    # Hercule punching bag event damage
    if str(stage)[0:3] in ('711', '185'):
        damage = randint(100000000, 101000000)

    sign = {
        'actual_steps': steps,
        'difficulty': difficulty,
        'elapsed_time': finish - start,
        'energy_ball_counts_in_boss_battle': [4, 6, 0, 6, 4, 3, 0, 0, 0, 0, 0, 0, 0, ],
        'has_player_been_taken_damage': False,
        'is_cheat_user': False,
        'is_cleared': True,
        'is_defeated_boss': True,
        'is_player_special_attack_only': True,
        'max_damage_to_boss': damage,
        'min_turn_in_boss_battle': len(defeated),
        'passed_round_ids': defeated,
        'quest_finished_at_ms': finish,
        'quest_started_at_ms': start,
        'steps': steps,
        'token': stoken
    }

    enc_sign = crypto.encrypt_sign(json.dumps(sign))

    headers = {
        'User-Agent': dua,
        'Accept': '*/*',
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Platform': os,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'X-ClientVersion': code
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()