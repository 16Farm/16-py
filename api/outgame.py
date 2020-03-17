import requests
import json
import time
import config
import utils.crypto as crypto

# dokkan ping
def ping(ver):
    dua = config.device_agent1
    if ver == 'gb':
        url = config.gb_url + '/ping'
        code = config.gb_code
    else:
        url = config.jp_url + '/ping'
        code = config.jp_code
    headers = {
        'X-Platform': 'android',
        'X-ClientVersion': code,
        'X-Language': config.lang,
        'X-UserID': '////',
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# title screen ads
def ads(ver):
    dua = config.device_agent1
    if ver == 'gb':
        url = config.gb_url + '/title/banners'
        code = config.gb_code
    else:
        url = config.jp_url + '/title/banners'
        code = config.jp_code
    headers = {
        'X-Platform': 'android',
        'X-ClientVersion': code,
        'X-Language': config.lang,
        'Content-Type': 'application/json',
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# assets for the tutorial to function visually
def tutorialAssets(ver, os):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/tutorial/assets'
        code = config.gb_code
    else:
        url = config.jp_url + '/tutorial/assets'
        code = config.jp_code
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': '0',
        'X-DatabaseVersion': '',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# check asset version & files
def getAsset(ver, token, secret, ts):
    dua = config.device_agent1
    if ver == 'gb':
        url = config.gb_url + '/client_assets'
        auth = crypto.mac(ver, token, secret, 'GET', '/client_assets')
        code = config.gb_code
    else:
        url = config.jp_url + '/client_assets'
        auth = crypto.mac(ver, token, secret, 'GET', '/client_assets')
        code = config.jp_code
    if ts != None:
        asset = ts
        db = ts
    else:
        asset = '0'
        db = ''
    headers = {
        'X-Platform': 'android',
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

# check past & future db versions
def getDatabase(ver, token, secret):
    dua = config.device_agent1
    if ver == 'gb':
        url = config.gb_url + '/client_assets/database'
        auth = crypto.mac(ver, token, secret, 'GET', '/client_assets/database')
        code = config.gb_code
    else:
        url = config.jp_url + '/client_assets/database'
        auth = crypto.mac(ver, token, secret, 'GET', '/client_assets/database')
        code = config.jp_code
    headers = {
        'X-Platform': 'android',
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': '0',
        'X-DatabaseVersion': '',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
    }
    r = requests.get(url, data=None, headers=headers)
    return r.json()