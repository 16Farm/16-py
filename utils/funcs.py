import sys
import requests
import json
import os as fs
import re
import webbrowser
from zipfile import ZipFile
import time
from threading import Timer
from colorama import init, Fore, Back
init(autoreset=True)
import config
import utils.crypto as crypto
import utils.error as error
import utils.database as database
import api.transfer as transfer
import api.auth as auth
import api.outgame as outgame
import api.ingame as ingame

def subfolders():
    if not fs.path.isdir('../saves'):
        try:
            fs.mkdir('../saves') # outside source
            print('"saves" directory created.')
        except:
            print('unable to create "saves" directory.')
    if not fs.path.isdir('../summaries'):
        try:
            fs.mkdir('../summaries') # outside source
        except:
            print('unable to create "summaries" directory.')
    if not fs.path.isdir('./data'):
        try:
            fs.mkdir('./data') # inside source
        except:
            print('unable to create "data" directory.')

def getVersionCodes():
    try:
        r = requests.get('https://raw.githubusercontent.com/K1mpl0s/16-pc/master/versions.json')
        jso = r.json()
        if str(jso['sixteen']) != config.version:
            print(Fore.CYAN + '16 > new update! (' + config.version + '/' + str(jso['sixteen']) + ')' + Fore.LIGHTGREEN_EX + '\nwould you like to open discord? Press ENTER if so.\n\n' + Fore.RESET + str(jso['discord']))
            input()
            if jso['discord'] != None:
                webbrowser.open(str(jso['discord']), new=1, autoraise=True)
            else:
                webbrowser.open('https://discord.gg/nrjvK2J', new=1, autoraise=True)
            input()
        else:
            config.gb_code = jso['gb']
            config.jp_code = jso['jp']
    except:
        print('can\'t fetch version codes.')
        exit()

def checkServers(ver):
    try:
        if ver == 'gb':
            url = 'https://ishin-global.aktsk.com/ping'
        else:
            url = 'https://ishin-production.aktsk.jp/ping'
        headers = {
            'X-Platform': 'android',
            'X-ClientVersion': '1.0.0',
            'X-Language': 'en',
            'X-UserID': '////'
        }
        r = requests.get(url, data=None, headers=headers)
        store = r.json()
        if 'error' not in store:
            url = store['ping_info']['host']
            port = store['ping_info']['port_str']
            if ver == 'gb':
                config.gb_url = 'https://' + str(url)
                config.gb_port = str(port)
            else:
                config.jp_url = 'https://' + str(url)
                config.jp_port = str(port)
            return True
        else:
            print(Fore.RED + '[' + ver + ' server] can\'t connect.')
            return False
    except:
        print(Fore.RED + '[' + ver + ' server] can\'t connect.')
        return False

def help1():
    f = open('mainpage.txt', 'r')
    txt = f.read().replace('{CYAN}', Fore.CYAN).replace('{LTYELLOW}', Fore.LIGHTYELLOW_EX).replace('{GREEN}', Fore.LIGHTGREEN_EX).replace('{YELLOW}', Fore.YELLOW).replace('\\n', '\n')
    for match in re.findall(r'\\x[0-9A-Fa-f]{2}', txt):
        txt = txt.replace(match, chr(int(match[2:], 16)))
    print(txt)
    f.close()

def help2():
    f = open('./farming/help.txt', 'r')
    txt = f.read().replace('{CYAN}', Fore.CYAN).replace('{LTYELLOW}', Fore.LIGHTYELLOW_EX).replace('{GREEN}', Fore.GREEN).replace('{YELLOW}', Fore.YELLOW).replace('\\n', '\n')
    for match in re.findall(r'\\x[0-9A-Fa-f]{2}', txt):
        txt = txt.replace(match, chr(int(match[2:], 16)))
    print(txt)
    f.close()

def checkDatabase():
    print('checking database versions...')
    store = outgame.getDatabase(config.acc_ver, config.sess_token, config.sess_secret)
    if 'error' not in store:
        version = store['version']
        if fs.path.isfile('./data/' + config.acc_ver + '-data.txt'):
            f = open('./data/' + config.acc_ver + '-data.txt', 'r')
            ver2 = f.readline().rstrip()
            f.close()
            if str(ver2) != str(version):
                print(str(version))
                fs.unlink('./data/' + config.acc_ver + '-data.txt')
                database.download(config.acc_ver, config.sess_token, config.sess_secret, version)
                print(Fore.GREEN + 'done.')
            else:
                print('no database to download.')
        else:
            print(str(version))
            database.download(config.acc_ver, config.sess_token, config.sess_secret, version)
            print(Fore.GREEN + 'done.')
    else:
        error.Handler('DB DL', store)

def createSaveFile(iden):
    print(Fore.LIGHTYELLOW_EX + 'What would you like to name this save?')
    save = input().lower()
    if len(str(save)) >= 1:
        if fs.path.isfile('../saves/' + str(save) + '.txt'):
            print(Fore.LIGHTRED_EX + 'save name already exists!')
            createSaveFile(config.acc_ver, config.acc_os, iden)
        else:
            if ' ' not in save and '\n' not in save:
                f = open('../saves/' + str(save) + '.txt', 'w')
                f.write(config.acc_ver+':'+config.acc_os+'\n')
                f.write(str(iden.replace('\n', '')) + '\n')
                f.close()
                print(Fore.LIGHTGREEN_EX + 'saved account as "saves/' + str(save) + '.txt"\nuse "load ' + str(save) + '" to log-in anytime.')
                return save
            else:
                print(Fore.LIGHTRED_EX + 'save name must not contain spaces!')
                createSaveFile(iden)
    else:
        print(Fore.LIGHTRED_EX + 'save name is too small!')
        createSaveFile(iden)

def checkTcLoop(iden):
    store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False)
    if 'error' not in store:
        if 'reason' not in store:
            store1 = transfer.create(config.acc_ver, config.acc_os, store['access_token'], store['secret'])
            if 'error' not in store1:
                fc = '000000000'
                tc = str(store1['link_code'])
                store2 = transfer.validate(config.acc_ver, tc, fc)
                if 'error' not in store2:
                    store3 = ingame.user(config.acc_ver, config.acc_os, store['access_token'], store['secret'], False)
                    print(Fore.GREEN + '\n' + str(store3['user']['id']))
                    print(Fore.GREEN + tc + '\n')
                    return True
                else:
                    print('transfer code not found. making new code...')
                    checkTcLoop(iden)
            else:
                error.Handler('loop create', store1)
        else:
            url = store['captcha_url']
            key = store['captcha_session_key']
            webbrowser.open(url, new=1, autoraise=True)
            print('Complete CAPTCHA to login... Press ENTER when done.')
            input()
            checkTcLoop(iden)
    else:
        error.Handler('loop login', store)

def refresh():
    save = config.loaded
    store = auth.login(config.acc_ver, config.acc_os, crypto.basic(config.account), False)
    if 'error' not in store:
        config.sess_token, config.sess_secret = store['access_token'], store['secret']
        print(Fore.LIGHTGREEN_EX + 'client refreshed.')
    else:
        error.Handler('refresh', store)

'''
update version hash by downloading APK(s)
author: k1mpl0s, assistance: renzy.

this function is not recommended for use yet.
if you start automatically updating these hashes then game breaking changes can get people flagged as a bot account.
something similar happened to FlashChaser, Bot zone, & Bladefive; outdated stage clear packets sent flagged as illegal stage clear methods.
after the account(s) were flagged the owner(s) were unable to get account recovery support via email. thus losing their account.
'''
def fetchVersion(ver):
    if ver == 'gb':
        url = 'https://api.qoo-app.com/v6/apps/com.bandainamcogames.dbzdokkanww/download'
    else:
        url = 'https://api.qoo-app.com/v6/apps/com.bandainamcogames.dbzdokkan/download'
    timer_start = int(round(time.time(), 0))
    print('downloading apk...')
    r = requests.get(url, stream=True, allow_redirects=True)
    f = open('./data/' + ver + '.apk', 'wb')
    for chunk in r.iter_content(1024):
        f.write(chunk)
    f.close()
    timer_finish = int(round(time.time(), 0))
    timer_total = timer_finish - timer_start
    print(str(timer_total) + ' second(s) download.')
    # rename apk as zip & unzip contents from apk
    print('unzipping apk... (' + ver + '.apk > ' + ver + '.zip > ./' + ver + '-content)')
    fs.rename('./data/' + ver + '.apk', ver + '.zip')
    ZipFile('./data/' + ver + '.zip', 'r').extractall('./data/' + ver + '-content')
    # run grep
    print('getting version & hash from contents...')
    f = open(file='./data/' + ver + '-content/assets/crashlytics-build.properties', mode='r', encoding='cp437')
    content = f.read()
    version = re.findall('\d+\.\d+\.\d+', content)[0]
    f = open(file='./data/' + ver + '-content/lib/armeabi-v7a/libcocos2dcpp.so', mode='r', encoding='cp437')
    content = f.read()
    hash = re.findall('[0-9a-f]{64}', content)[0]
    # save new version
    if version != None and hash != None:
        print(str(version) + '-' + str(hash))
        return str(version) + '-' + str(hash)
    else:
        return False