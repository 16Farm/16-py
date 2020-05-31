import json
import requests
import datetime
import time
import os as fs
import webbrowser
from colorama import init, Fore, Style
init(autoreset=True)
import config
import utils.crypto as crypto
import utils.error as error
import utils.database as database
import api.transfer as transfer
import api.auth as auth
import api.outgame as outgame
import api.ingame as ingame
import farming.fapro as farmbot
import farming.facebook as facebook
import utils.funcs as utils
import urllib
from datetime import datetime

farm = []

def Handler(msg):
    global farm
    args = msg.split(' ')
    #===== base =====
    # new
    if args[0].lower() == 'new' and config.loaded == None:
        if len(args) == 3:
            if args[1] == 'gb' or args[1] == 'jp':
                if args[2] == 'ios' or args[2] == 'android':
                    store = auth.register(args[1], args[2])
                    if 'error' not in store:
                        url = store[0]['captcha_url']
                        key = store[0]['captcha_session_key']
                        webbrowser.open(url, new=1, autoraise=True)
                        print('Complete CAPTCHA to continue... Press ENTER when done.')
                        input()
                        store = auth.register(args[1], args[2], store[1], store[2], key)
                        if 'error' not in store:
                            store2 = auth.login(args[1], args[2], crypto.basic(store[0]['identifier']), True)
                            if 'error' not in store2:
                                farmbot.tutorial(args[1], args[2], store2['access_token'], store2['secret'], store[0]['identifier'])
                                farmbot.gifts()
                                farmbot.missions()
                                print(Fore.LIGHTYELLOW_EX + 'type "help" for a list of commands.')
                            else:
                                error.Handler('new login', store2)
                        else:
                            error.Handler('register2', store)
                    else:
                        error.Handler('register1', store)
                else:
                    print('invalid OS input.')
            else:
                print('invalid version input.')
        else:
            print('gb/jp ios/android')
        return 1
    # reroll
    if args[0].lower() == 'reroll' and config.loaded == None:
        if len(args) == 3:
            if args[1] == 'gb' or args[1] == 'jp':
                if args[2] == 'ios' or args[2] == 'android':
                    store = auth.register(args[1], args[2])
                    if 'error' not in store:
                        url = store[0]['captcha_url']
                        key = store[0]['captcha_session_key']
                        webbrowser.open(url, new=1, autoraise=True)
                        print('Complete CAPTCHA to continue... Press ENTER when done.')
                        input()
                        store = auth.register(args[1], args[2], store[1], store[2], key)
                        if 'error' not in store:
                            store2 = auth.login(args[1], args[2], crypto.basic(store[0]['identifier']), True)
                            if 'error' not in store2:
                                farmbot.tutorial(args[1], args[2], store2['access_token'], store2['secret'], store[0]['identifier'])
                                farmbot.gifts()
                                farmbot.missions()
                                farmbot.streamline('quests')
                                utils.refresh()
                                farmbot.streamline('events')
                                utils.refresh()
                                farmbot.streamline('ezas')
                                utils.refresh()
                                farmbot.gifts()
                                farmbot.missions()
                            else:
                                error.Handler('new login', store2)
                        else:
                            error.Handler('register2', store)
                    else:
                        error.Handler('register1', store)
                else:
                    print('invalid OS input.')
            else:
                print('invalid version input.')
        else:
            print('gb/jp ios/android')
        return 1
    # transfer
    if args[0].lower() == 'add' and config.loaded == None:
        try:
            iden = None
            if len(args) == 3:
                if args[1] == 'gb' or args[1] == 'jp':
                    config.acc_ver = args[1]
                    tc = args[2]
                    fc = '000000000'
                    store = transfer.validate(config.acc_ver, tc, fc)
                    if 'error' not in store:
                        if not store['platform_difference']:
                            config.acc_os = 'android'
                        else:
                            config.acc_os = 'ios'
                        store = transfer.use(config.acc_ver, config.acc_os, tc, fc)
                        if 'error' not in store:
                            iden = store['identifiers'].replace('\n', '')
                            print(Fore.YELLOW + 'identifier for recover.\n' + iden)
                            store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False)
                            if 'error' not in store:
                                if 'reason' not in store:
                                    save = utils.createSaveFile(iden)
                                    config.loaded, config.account = save, iden
                                    utils.checkDatabase()
                                    #utils.help2()
                                else:
                                    url = store['captcha_url']
                                    key = store['captcha_session_key']
                                    webbrowser.open(url, new=1, autoraise=True)
                                    print('Complete CAPTCHA to login... Press ENTER when done.')
                                    input()
                                    store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False, key)
                                    if 'error' not in store:
                                        save = utils.createSaveFile(iden)
                                        config.loaded, config.account = save, iden
                                        utils.checkDatabase()
                                        #utils.help2()
                                    else:
                                        error.Handler('add login2', store)
                            else:
                                error.Handler('add login', store)
                        else:
                            error.Handler('add use', store)
                    else:
                        error.Handler('add validate', store)
                else:
                    print('invalid version input.')
            else:
                print('gb/jp TC')
        except:
            print(Fore.LIGHTRED_EX + 'Something went wrong... use your identifier to recover.\n' + Fore.LIGHTYELLOW_EX + iden)
        return 0
    # link
    if args[0].lower() == 'link' and config.loaded == None:
        if len(args) == 3:
            if args[1] == 'gb' or args[1] == 'jp':
                if args[2] == 'ios' or args[2] == 'android':
                    url = facebook.loginPage(args[1])
                    facebook.webView(args[1], args[2], url, 1)
                else:
                    print('invalid OS input.')
            else:
                print('invalid version input.')
        else:
            print('gb/jp ios/android')
        return 1
    # load
    if args[0].lower() == 'load' and config.loaded == None:
        if len(args) == 2:
            save = args[1].lower()
            if fs.path.isfile('../saves/'+save+'.txt'):
                f = open('../saves/'+save+'.txt', 'r')
                line1 = f.readline().rstrip().split(':')
                config.acc_ver = line1[0]
                config.acc_os = line1[1]
                iden = f.readline().rstrip()
                f.close()
                store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False)
                if 'error' not in store:
                    if 'reason' not in store:
                        config.sess_token, config.sess_secret = store['access_token'], store['secret']
                        config.loaded, config.account = save, iden
                        utils.checkDatabase()
                        utils.help2()
                    else:
                        url = store['captcha_url']
                        key = store['captcha_session_key']
                        webbrowser.open(url, new=1, autoraise=True)
                        print('Complete CAPTCHA to login... Press ENTER when done.')
                        input()
                        store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False, key)
                        if 'error' not in store:
                            config.sess_token, config.sess_secret = store['access_token'], store['secret']
                            config.loaded, config.account = save, iden
                            utils.checkDatabase()
                            utils.help2()
                        else:
                            error.Handler('load login2', store)
                else:
                    error.Handler('load login', store)
            else:
                print('that save doesn\'t exist.')
        else:
            print('you didn\'t select a save.')
        return 1
    # daily
    if args[0].lower() == 'daily' and config.loaded == None:
        for i in fs.listdir('../saves'):
            save = open('../saves/' + str(i), 'r')
            txt = save.read().split('\n')
            config.acc_ver, config.acc_os, config.loaded, config.account = txt[0].split(':')[0], txt[0].split(':')[1], str(i), txt[1]
            save.close()
            try:
                store = auth.login(config.acc_ver, config.acc_os, crypto.basic(config.account), False)
                if 'error' not in store:
                    config.sess_token, config.sess_secret = store['access_token'], store['secret']
                    store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                    if 'error' not in store:
                        for i in store['events']:
                            if int(i['id']) == 111 or int(i['id']) == 116 or int(i['id']) == 120 or int(
                                    i['id']) == 130 or int(i['id']) == 131 or int(i['id']) == 132 or int(
                                    i['id']) == 134 or int(i['id']) == 135 or int(i['id']) == 177:
                                if 'quests' in i:
                                    for x in i['quests']:
                                        for j in database.fetchAll(config.acc_ver + '.db', 'sugoroku_maps', 'quest_id=' + str(x['id'])):
                                            farmbot.runStage(x['id'], j[2], None)
                    else:
                        error.Handler('daily0', store)
                    farmbot.missions()
                    farmbot.gifts()
                else:
                    print('Error with: ' + str(i))
                    error.Handler('daily(s)', store)
            except:
                print('Error with: ' + str(i))
                print('Cannot use this identifier!')
        return 0
    '''
    #output
    if args[0].lower() == 'output' and config.loaded == None:
        if len(args) == 2:
            save = args[1].lower()
            if fs.path.isfile('../saves/'+save+'.txt'):
                f = open('../saves/'+save+'.txt', 'r')
                line1 = f.readline().rstrip().split(':')
                config.acc_ver = line1[0]
                config.acc_os = line1[1]
                iden = f.readline().rstrip()
                f.close()
                utils.checkTcLoop(iden)
            else:
                print('that save doesn\'t exist.')
        else:
            print('you didn\'t select a save.')
        return 1
    '''
    # summary
    if args[0].lower() == 'summary' and config.loaded == None:
        date = str(int(time.time()))
        f = open('../summaries/' + date + '.html', 'w')
        f.write('<html><body><style>h1{text-align:center;}table{width:100%;border:0}th{font-size:15px;background-color:gray;border-width:1px;padding:8px;border-style:solid;border-color:black;text-align:left;}td{border-width:1px;padding:8px;border-style:solid;border-color:black;}</style><h1>Android 16 - Summary</h1><table><tr><th>Save, Version - OS</th><th>ID, Transfer</th><th>Information</th><th>Quests, Events, EZA</th><th>Email, password</th></tr>\n')
        for i in fs.listdir('../saves'):
            save = open('../saves/' + str(i), 'r')
            txt = save.read().split('\n')
            ver = txt[0].split(':')[0]
            os = txt[0].split(':')[1]
            iden = txt[1]
            save.close()
            try:
                store = auth.login(ver, os, crypto.basic(iden), False)
                if 'error' not in store:
                    config.sess_token, config.sess_secret = store['access_token'], store['secret']
                    store = ingame.user(ver, os, config.sess_token, config.sess_secret, False)
                    if 'error' not in store:
                        user = store['user']
                        f.write('<tr><td>' + str(i) + '<br>' + ver + ' - ' + os + '</td><td>' + str(user['id']) + '<br>' + 'None' + '</td><td>Name: ' + str(user['name']) + '<br>Rank: ' + str(user['rank']) + '<br>Stones: ' + str(user['stone']) + '<br>Zeni:' + str(user['zeni']) + '</td><td>None</td><td>None</td></tr>\n')
                    else:
                        print('Error with: ' + str(i))
                        error.Handler('summary', store)
                else:
                    print('Error with: ' + str(i))
                    error.Handler('summary', store)
            except:
                print('Error with: ' + str(i))
                print('Cannot use this identifier!')
        f.write('</table></body></html>')
        f.close()
        print(Fore.LIGHTGREEN_EX + 'Summarization complete. Saved as: summaries/' + date + '.html')
        return 1
    #===== tools =====
    '''
    # verify
    if args[0].lower() == 'verify' and config.loaded == None:
        if len(args) == 4:
            if args[1] == 'gb' or args[1] == 'jp':
                if len(args[2]) == 9 or len(args[2]) == 10:
                    store = transfer.validate(args[1], args[3], args[2])
                    if 'error' not in store:
                        if not store['platform_difference']:
                            os = 'android'
                        else:
                            os = 'iOS'
                        if store['user_is_valid']:
                            matches = 'Yes'
                        else:
                            matches = 'No'
                        if store['link_code_is_valid']:
                            valid = 'Yes'
                        else:
                            valid = 'No'
                        print(Fore.GREEN + 'FC matches TC: ' + matches + '\nValid TC: ' + valid + '\nOS: ' + os + '\nName: ' + str(store['user_name']) + '\nRank: ' + str(store['user_rank']))
                    else:
                        error.Handler('verify', store)
                else:
                    print('abnormal FC/ID size.')
            else:
                print('invalid version input.')
        else:
            print('gb/jp FC/ID TC')
        return 0
    '''
    # recover
    if args[0].lower() == 'recover' and config.loaded == None:
        if len(args) == 4:
            if args[1] == 'gb' or args[1] == 'jp':
                if args[2] == 'ios' or args[2] == 'android':
                    '''
                    if utils.checkTcLoop(args[1], args[2], args[3]) == True:
                        print('account successfully recovered.')
                    '''
                    if len(args[3]) >= 152:
                        iden = args[3]
                        store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False)
                        if 'error' not in store:
                            if 'reason' not in store:
                                save = utils.createSaveFile(iden)
                                config.loaded, config.account = save, iden
                                utils.checkDatabase()
                                # utils.help2()
                            else:
                                url = store['captcha_url']
                                key = store['captcha_session_key']
                                webbrowser.open(url, new=1, autoraise=True)
                                print('Complete CAPTCHA to login... Press ENTER when done.')
                                input()
                                store = auth.login(config.acc_ver, config.acc_os, crypto.basic(iden), False, key)
                                if 'error' not in store:
                                    save = utils.createSaveFile(iden)
                                    config.loaded, config.account = save, iden
                                    utils.checkDatabase()
                                    # utils.help2()
                                else:
                                    error.Handler('rlogin2', store)
                        else:
                            error.Handler('rlogin', store)
                    else:
                        print('not a valid identifier.')
                else:
                    print('invalid OS input.')
            else:
                print('invalid version input.')
        else:
            print('gb/jp ios/android identifier')
        return 0
    '''
    # renew
    if args[0].lower() == 'renew' and config.loaded == None:
        if len(args) == 4:
            if args[1] == 'gb':
                if len(args[2]) == 9 or len(args[2]) == 10:
                    store = transfer.validate(args[1], args[3], args[2])
                    if 'error' not in store:
                        if not store['platform_difference']:
                            os = 'android'
                        else:
                            os = 'ios'
                        store = transfer.use(args[1], os, args[3], args[2])
                        if 'error' not in store:
                            print(Fore.YELLOW + store['identifiers'].replace('\n', ''))
                            utils.checkTcLoop(args[1], os, store['identifiers'])
                        else:
                            error.Handler('renew use', store)
                    else:
                        error.Handler('renew validate', store)
                else:
                    print('abnormal FC/ID size.')
            else:
                print('invalid version input.\n(JP is no longer supported until further notice.)')
        else:
            print('gb/jp FC/ID TC')
        return 0
    '''
    # host
    if args[0].lower() == 'host' and config.loaded == None:
        if len(args) == 2:
            if args[1] == 'gb' or args[1] == 'jp':
                store = outgame.ping(args[1])
                print(Fore.GREEN + 'Host: ' + store['ping_info']['host'] + '\nPort: ' + str(store['ping_info']['port']) + '\nAPI port: ' + str(store['ping_info']['port_str']) + '\nCF URI Prefix: ' + store['ping_info']['cf_uri_prefix'])
            else:
                print('invalid version input.')
        else:
            print('gb/jp')
        return 0
    #===== other =====
    # support
    if args[0].lower() == 'support':
        url = 'https://discord.gg/nrjvK2J'
        webbrowser.open(url, new=1, autoraise=True)
        return 1
    # exit
    if args[0].lower() == 'exit':
        if config.loaded == None:
            exit()
        else:
            config.loaded = None
            utils.help1()
            return 1
    #===== farmbot =====
    # baba
    if args[0].lower() == 'baba' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                if len(args) >= 3:
                    if args[2] == 'bp':
                        store = ingame.babaItems(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret,
                                                 'exchange_point')
                        for i in store['shop_on_sale_items']:
                            if i['buyable']:
                                for j in i['shop_items']:
                                    if j['item_type'] == 'Card':
                                        try:
                                            element = ''
                                            db_ele = \
                                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(j['item_id']))[
                                                13]
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
                                            print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(j['item_id']))[1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(database.fetch(config.acc_ver + '.db', 'cards','id=' + str(j['item_id']))[24]))[1] + '] x' + str(j['quantity']) + ', ' + str(i['discount_price']) + 'bp')
                                        except:
                                            print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + 'card x' + str(j['quantity']) + ', ' + str(i['discount_price']) + 'bp')
                                    if j['item_type'] == 'SupportItem':
                                        print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + database.fetch(config.acc_ver + '.db', 'support_items', 'id=' + str(j['item_id']))[1] + ' x' + str(j['quantity']) + ', ' + str(i['discount_price']) + 'bp')
                                    if j['item_type'] == 'AwakeningItem':
                                        print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + database.fetch(config.acc_ver + '.db', 'awakening_items',
                                                             'id=' + str(j['item_id']))[1] + ' x' + str(
                                            j['quantity']) + ', ' + str(i['discount_price']) + 'bp')
                                    if j['item_type'] == 'TrainingItem':
                                        print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + database.fetch(config.acc_ver + '.db', 'training_items',
                                                             'id=' + str(j['item_id']))[1] + ' x' + str(
                                            j['quantity']) + ', ' + str(i['discount_price']) + 'bp')
                    if args[2] == 'zeni':
                        store = ingame.babaItems(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret,
                                                 'zeni')
                        for i in store['shop_on_sale_items']:
                            if i['buyable']:
                                for j in i['shop_items']:
                                    if j['item_type'] == 'Card':
                                        try:
                                            element = ''
                                            db_ele = \
                                                database.fetch(config.acc_ver + '.db', 'cards',
                                                               'id=' + str(j['item_id']))[
                                                    13]
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
                                            print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + element + ' ' +
                                                  database.fetch(config.acc_ver + '.db', 'cards',
                                                                 'id=' + str(j['item_id']))[1] + ' [' +
                                                  database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                                      database.fetch(config.acc_ver + '.db', 'cards',
                                                                     'id=' + str(j['item_id']))[24]))[1] + '] x' + str(
                                                j['quantity']) + ', ' + str(i['discount_price']) + 'zeni')
                                        except:
                                            print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' + 'card x' + str(
                                                j['quantity']) + ', ' + str(i['discount_price']) + 'zeni')
                                    if j['item_type'] == 'SupportItem':
                                        print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' +
                                              database.fetch(config.acc_ver + '.db', 'support_items',
                                                             'id=' + str(j['item_id']))[1] + ' x' + str(
                                            j['quantity']) + ', ' + str(i['discount_price']) + 'zeni')
                                    if j['item_type'] == 'AwakeningItem':
                                        print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' +
                                              database.fetch(config.acc_ver + '.db', 'awakening_items',
                                                             'id=' + str(j['item_id']))[1] + ' x' + str(
                                            j['quantity']) + ', ' + str(i['discount_price']) + 'zeni')
                                    if j['item_type'] == 'TrainingItem':
                                        print(Fore.LIGHTWHITE_EX + '#' + str(i['id']) + ', ' +
                                              database.fetch(config.acc_ver + '.db', 'training_items',
                                                             'id=' + str(j['item_id']))[1] + ' x' + str(
                                            j['quantity']) + ', ' + str(i['discount_price']) + 'zeni')
                    if args[2] == 'treasure':
                        store = ingame.babaItems(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret,
                                                 'treasure')
                        '''
                        {'shop_on_sale_treasure_items': [{'treasure_item_id': 9103, 'shop_on_sale_items': [{'id': 92000011, 'discount_price': 1, 'is_premium': False, 'buyable': True, 'currency_id': 9103, 'currency_type': 'TreasureItem', 'price': 1, 'shop_items': [{'item_id': 1008410, 'item_type': 'Card', 'quantity': 1, 'card_exp_init': 0}], 'start_at': 1511136000, 'end_at': 1924991999, 'is_display_remaining_time': False, 'buyable_num': 1},
                        '''
                        print(store)
                else:
                    print(Fore.LIGHTRED_EX + 'missing argument. - baba list <bp/zeni/treasure>')
            if args[1] == 'sell':
                print('this will be coming in a later update. Cheers!')
            if args[1] == 'buy':
                if len(args) >= 5:
                    if args[2] == 'bp':
                        store = ingame.babaBuy(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret,
                                                 'exchange_point', args[3], args[4])
                    if args[2] == 'zeni':
                        store = ingame.babaBuy(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret,
                                                 'zeni', args[3], args[4])
                    if 'error' not in store:
                        print(store)
                    else:
                        print(store)
                else:
                    print('missing argument. - baba buy <bp/zeni> <id> <amount>')
        return 0
    # banners
    if args[0].lower() == 'banners' and config.loaded != None:
        store = ingame.banners(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            for i in store['gashas']:
                print(Fore.LIGHTGREEN_EX + str(i['id']) + ' - ' + i['name'])
        else:
            error.Handler('banners', store)
        return 0
    # box
    if args[0].lower() == 'box' and config.loaded != None:
        print(Fore.LIGHTYELLOW_EX + 'gathering cards...')
        settings = utils.getSettings()
        store = ingame.cards(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            lr = []
            ur = []
            ssr = []
            sr = []
            r = []
            n = []
            if settings['display_only_ids'] != True:
                for i in store['cards']:
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] == 5:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                        lr.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[24]))[
                                1] + '] (' + str(i['card_id']) + ')\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(
                                i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, Lvl: ' +
                            str(database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['exp'])))[
                                1] + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    14]) + ', Cost: ' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    5]) + ', uid: ' + str(i['id']))
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] == 4:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                        ur.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[24]))[
                                1] + '] (' + str(i['card_id']) + ')\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(
                                i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, Lvl: ' +
                            str(database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['exp'])))[
                                1] + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    14]) + ', Cost: ' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    5]) + ', uid: ' + str(i['id']))
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] == 3:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                        ssr.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[24]))[
                                1] + '] (' + str(i['card_id']) + ')\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(
                                i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, Lvl: ' +
                            str(database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['exp'])))[
                                1] + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    14]) + ', Cost: ' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    5]) + ', uid: ' + str(i['id']))
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] == 2:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                        sr.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[24]))[
                                1] + '] (' + str(i['card_id']) + ')\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(
                                i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, Lvl: ' +
                            str(database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['exp'])))[
                                1] + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    14]) + ', Cost: ' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    5]) + ', uid: ' + str(i['id']))
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] == 1:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                        r.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[24]))[
                                1] + '] (' + str(i['card_id']) + ')\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(
                                i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, Lvl: ' +
                            str(database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['exp'])))[
                                1] + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    14]) + ', Cost: ' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    5]) + ', uid: ' + str(i['id']))
                    if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[6] == 0:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                        n.append(
                            element + ' ' + database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[24]))[
                                1] + '] (' + str(i['card_id']) + ')\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(
                                i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, Lvl: ' +
                            str(database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['exp'])))[
                                1] + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    14]) + ', Cost: ' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    5]) + ', uid: ' + str(i['id']))
                print(Fore.WHITE + '==== ==== > LR < ==== ====\n\n' + '\n'.join(
                    lr) + Fore.WHITE + '\n\n==== ==== > UR < ==== ====\n\n' + '\n'.join(
                    ur) + Fore.WHITE + '\n\n==== ==== > SSR < ==== ====\n\n' + '\n'.join(
                    ssr) + Fore.WHITE + '\n\n==== ==== > SR < ==== ====\n\n' + '\n'.join(
                    sr) + Fore.WHITE + '\n\n==== ==== > R < ==== ====\n\n' + '\n'.join(
                    r) + Fore.WHITE + '\n\n==== ==== > N < ==== ====\n\n' + '\n'.join(n))
            else:
                for i in store['cards']:
                    print(str(i['card_id']) + '\n' + 'SA: ' + str(
                        i['skill_lv']) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(
                        i['exp']) + ', uid: ' + str(i['id']))
        else:
            error.Handler('cards', store)
        return 0
    # capacity
    if args[0].lower() == 'capacity' and config.loaded != None:
        store = ingame.capacity(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            print(Fore.GREEN + 'box size increased by 5+')
        else:
            error.Handler('capacity', store)
        return 0
    # clash
    if args[0].lower() == 'clash' and config.loaded != None:
        farmbot.streamline('clash')
        return 0
    # clear
    if args[0].lower() == 'clear' and config.loaded != None:
        # quests, events, eza, clash
        if len(args) == 2:
            if args[1] == 'quests':
                farmbot.streamline('quests')
            if args[1] == 'events':
                farmbot.streamline('events')
            if args[1] == 'eza':
                farmbot.streamline('ezas')
            if args[1] == 'clash':
                farmbot.streamline('clash')
        return 0
    # dbs
    if args[0].lower() == 'dbs' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                store = ingame.dragonballs(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['dragonball_sets']:
                        if i['ball_type'] == 0:
                            print(Fore.GREEN + '==== ==== > Shenron < ==== ====\n' + Fore.WHITE)
                            for x in i['dragonballs']:
                                print(str(x['num']) + ' - collected: ' + str(x['is_got']) + ' (' + str(x['quest_id']) + ':' + str(x['difficulties'][0]) + ')')
                    for i in store['dragonball_sets']:
                        if i['ball_type'] == 1:
                            print(Fore.GREEN + '\n==== ==== > Porunga < ==== ====\n' + Fore.WHITE)
                            for x in i['dragonballs']:
                                print(str(x['num']) + ' - collected: ' + str(x['is_got']) + ' (' + str(x['description']) + ')')
                                if 'condition' in x['mission']:
                                    print(str(x['mission']['conditions']))
                else:
                    error.Handler('dragonballs', store)
            if args[1] == 'seek':
                store = ingame.dragonballs(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['dragonball_sets']:
                        if i['ball_type'] == 0:
                            for x in i['dragonballs']:
                                if x['is_got'] == False:
                                    farmbot.runStage(str(x['quest_id']), str(x['difficulties'][0]), None)
                    print(Fore.LIGHTYELLOW_EX + 'done collecting dragonballs.')
                else:
                    error.Handler('dragonballs', store)
            if args[1] == 'wish':
                if len(args) == 2:
                    store = ingame.wish(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, 1, None)
                    if 'error' not in store:
                        for i in store['dragonball_wishes']:
                            if i['is_wishable']:
                                print(Fore.LIGHTGREEN_EX + '#' + str(i['id']) + ' - ' + str(i['title']) + '\n' + Fore.LIGHTCYAN_EX + '(' + str(i['description']) + ')')
                        print(Fore.LIGHTYELLOW_EX + 'use "dbs wish <id>" to make the wish.')
                    else:
                        error.Handler('info user', store)
                else:
                    wish = []
                    wish.append(int(args[2]))
                    store = ingame.wish(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, 1, wish)
                    if 'error' not in store:
                        farmbot.gifts()
                    else:
                        error.Handler('wish', store)
        else:
            print('dbs <list/seek/wish>')
        return 0
    # event
    if args[0].lower() == 'event' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['events']:
                        try:
                            if 'quests' in i:
                                print(Fore.LIGHTRED_EX + '===> ' + str(
                                    database.fetch(config.acc_ver + '.db', 'areas', 'id=' + str(i['id']))[4]) + ' <===')
                                for x in i['quests']:
                                    difficulties = []
                                    for j in database.fetchAll(config.acc_ver + '.db', 'sugoroku_maps',
                                                               'quest_id=' + str(x['id'])):
                                        difficulties.append(str(j[2]))
                                    print(Fore.LIGHTYELLOW_EX + str(x['id']) + ' (' + ', '.join(
                                        difficulties) + ')' + Fore.LIGHTRED_EX + ' - ' + Fore.LIGHTGREEN_EX + str(
                                        x['name']))
                        except:
                            print(Fore.LIGHTRED_EX + '===> unknown <===')
                            for x in i['quests']:
                                print(Fore.LIGHTYELLOW_EX + str(
                                    x['id']) + Fore.LIGHTRED_EX + ' - ' + Fore.LIGHTGREEN_EX + str(x['name']))
                else:
                    error.Handler('events', store)
            if args[1] == 'area':
                if len(args) >= 3:
                    if len(args[2]) >= 3 and len(args[2]) <= 6:
                        store = ingame.quests(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                        if 'error' not in store:
                            maps = []
                            if len(args[2]) > 3:
                                print('you provided a stage ID not area ID; trimming stage ID...')
                                args[2] = args[2][:-3]
                            for i in store['user_areas']:
                                if int(i['area_id']) == int(args[2]):
                                    for j in i['user_sugoroku_maps']:
                                        if int(j['cleared_count']) == 0:
                                            farmbot.runStage(str(j['sugoroku_map_id'])[:-1],
                                                             str(j['sugoroku_map_id'])[-1],
                                                             None)
                        else:
                            error.Handler('quests', store)
                    else:
                        print('invalid area ID')
                else:
                    print('no area ID provided.')
            if args[1] == 'stage':
                if len(args) >= 5:
                    if len(args[3]) == 1:
                        if int(args[4]) != 0:
                            for i in range(int(args[4])):
                                farmbot.runStage(args[2], args[3], None)
                        else:
                            print('can\'t run stage 0 times!')
                    else:
                        print('difficulty is wrong.\n0=normal || 1=hard || 2=zhard || 3=super || 4=super2')
                else:
                    print('missing stage ID, difficulty, & run amount arguments.')
        return 0
    # eza
    if args[0].lower() == 'eza' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for x in store['z_battle_stages']:
                        try:
                            print(str(x['id']) + ' ' + database.fetch(config.acc_ver + '.db', 'z_battle_stage_views',
                                                                      'z_battle_stage_id=' + str(x['id']))[3] + ' - ' +
                                  database.fetch(config.acc_ver + '.db', 'z_battle_stage_views',
                                                 'z_battle_stage_id=' + str(x['id']))[2])
                        except:
                            print(str(x['id']) + ' - unknown')
                else:
                    error.Handler('events', store)
            if args[1] == 'clear':
                if len(args) >= 3:
                    store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                    if 'error' not in store:
                        eza_pool = []
                        for x in store['z_battle_stages']:
                            eza_pool.append(int(x['id']))
                        if int(args[2]) in eza_pool:
                            store = ingame.quests(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                            for x in store['user_z_battles']:
                                if x['z_battle_stage_id'] == int(args[2]):
                                    clear_count = x['max_clear_level']
                                    while int(clear_count) <= 30:
                                        farmbot.runZLvl(int(args[2]), int(clear_count))
                                        clear_count = clear_count + 1
                        else:
                            print(Fore.LIGHTRED_EX + 'EZA event ID not in active pool!')
                    else:
                        error.Handler('events', store)
                else:
                    print('missing EZA event ID.')
            if args[1] == 'level':
                if len(args) >= 3:
                    store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                    if 'error' not in store:
                        eza_pool = []
                        for x in store['z_battle_stages']:
                            eza_pool.append(int(x['id']))
                        if int(args[1]) in eza_pool:
                            if len(args[3]) == 1:
                                if int(args[3]) != 0:
                                    for i in range(int(args[3]) + 1):
                                        if int(i) != 0:
                                            farmbot.runZLvl(int(args[2]), int(args[3]))
                        else:
                            print(Fore.LIGHTRED_EX + 'EZA event ID not in active pool!')
                    else:
                        error.Handler('events', store)
                else:
                    print('missing EZA event ID, level, & run amount arguments.')
            if args[1] == 'all':
                farmbot.streamline('ezas')
        return 0
    # farm
    # added potential, zeni, dupe, & medal farming. added f2p LR farming. a
    if args[0].lower() == 'farm' and config.loaded != None:
        if len(args) == 3:
            if args[1] == 'medal':
                medals = 0
                print('this will be coming in a later update. Cheers!')
            if args[1] == 'dupe':
                dupes = 0
                print('this will be coming in a later update. Cheers!')
            if args[1] == 'zeni':
                zeni = 0
                print('this will be coming in a later update. Cheers!')
            if args[1] == 'rank':
                rank = 0
                print('this will be coming in a later update. Cheers!')
        else:
            print('missing arguments.\nfarm <medal/dupe/zeni/exp> <amount>')
        return 0
    # favorite
    if args[0].lower() == 'favorite' and config.loaded != None:
        if len(args) == 2:
            store = ingame.favorite(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, args[1])
            if 'error' not in store:
                print(Fore.LIGHTGREEN_EX + 'card has been locked.')
            else:
                error.Handler('lock', store)
        else:
            print('favorite <card uid>')
        return 0
    # friends
    if args[0].lower() == 'friends' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                store = ingame.friends(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    print(Fore.LIGHTYELLOW_EX + '==== ==== > Friends < ==== ====\n' + Fore.WHITE)
                    for i in store['friendships']:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[13]
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
                        print(str(i['id']) + ', ' + str(i['user']['name']) + ', ' + str(
                            i['user']['rank']) + '\n' + element + ' ' +
                              database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[
                                  1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[24]))[
                                  1] + '],\nSA: ' + str(i['user']['leader']['skill_lv']) + '/' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[
                                15]) + ', Potential: ' + str(i['user']['leader']['released_rate']) + '%, Lvl: ' + str(
                            database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['user']['leader']['exp'])))[
                                  1] + '/' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[14]))
                    print(Fore.LIGHTYELLOW_EX + '==== ==== > Pending < ==== ====\n' + Fore.WHITE)
                    for i in store['pending_friendships']:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[13]
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
                        print(str(i['id']) + ', ' + str(i['user']['name']) + ', ' + str(
                            i['user']['rank']) + '\n' + element + ' ' +
                              database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[
                                  1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[24]))[
                                  1] + '],\nSA: ' + str(i['user']['leader']['skill_lv']) + '/' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[
                                15]) + ', Potential: ' + str(i['user']['leader']['released_rate']) + '%, Lvl: ' + str(
                            database.fetch(config.acc_ver + '.db', 'card_exps', 'exp_total=' + str(i['user']['leader']['exp'])))[
                                  1] + '/' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['user']['leader']['card_id']))[14]))
                else:
                    error.Handler('friends', store)
            if args[1] == 'accept':
                if len(args) >= 3:
                    store = ingame.acceptFriend(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, args[1])
                    if 'error' not in store:
                        if 'accepted' in store['friendship']['status']:
                            print(Fore.GREEN + 'friend accepted.')
                        else:
                            print(Fore.RED + 'can\'t accept.')
                    else:
                        error.Handler('accept friend', store)
                else:
                    print('missing user/friend ID.')
            if args[1] == 'search':
                if len(args) >= 3:
                    store = ingame.findFriend(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, int(args[1]))
                    if 'error' not in store:
                        element = '?'
                        db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(store['user']['leader']['card_id']))[
                            13]
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
                        print(str(store['user']['id']) + ', ' + str(store['user']['name']) + ', ' + str(
                            store['user']['rank']) + '\n' + element + ' ' +
                              database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(store['user']['leader']['card_id']))[
                                  1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills', 'id=' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(store['user']['leader']['card_id']))[24]))[
                                  1] + '],\nSA: ' + str(store['user']['leader']['skill_lv']) + '/' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(store['user']['leader']['card_id']))[
                                15]) + ', Potential: ' + str(store['user']['leader']['released_rate']) + '%, Lvl: ' +
                              str(database.fetch(config.acc_ver + '.db', 'card_exps',
                                                 'exp_total=' + str(store['user']['leader']['exp'])))[1] + '/' + str(
                            database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(store['user']['leader']['card_id']))[14]))
                    else:
                        error.Handler('find friend', store)
                else:
                    print('missing user/friend ID.')
            if args[1] == 'request':
                if len(args) >= 3:
                    store = ingame.addFriend(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, args[1])
                    if 'error' not in store:
                        print(Fore.LIGHTGREEN_EX + 'request sent.')
                    else:
                        error.Handler('add friend', store)
                else:
                    print('missing user/friend ID.')
        return 0
    # gift
    if args[0].lower() == 'gift' and config.loaded != None:
        farmbot.gifts()
        farmbot.missions()
        return 0
    # help
    if args[0].lower() == 'help' and config.loaded != None:
        if config.loaded == None:
            utils.help1()
            # finally added examples cause' weyfol
        else:
            utils.help2()
        return 1
    # history
    if args[0].lower() == 'history' and config.loaded != None:
        store = ingame.history(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            print(Fore.LIGHTYELLOW_EX + '\n==== ==== > Stone < ==== ====\n')
            for i in store['histories']['stone']:
                print(Fore.LIGHTYELLOW_EX + str(i['name']) + ' - ' + str(i['price']) + ' Stone(s)\n' + Fore.CYAN + datetime.utcfromtimestamp(int(i['drawn_at'])).strftime('%m/%d/%Y %H:%M.%S') + '\n' + Fore.WHITE + str(i['card_ids']) + '\n------------------------------')
            print(Fore.LIGHTBLUE_EX + '\n==== ==== > FP < ==== ====\n')
            for i in store['histories']['point']:
                print(Fore.LIGHTBLUE_EX + str(i['name']) + ' - ' + str(i[
                    'price']) + ' FP\n' + Fore.CYAN + datetime.utcfromtimestamp(int(i['drawn_at'])).strftime(
                    '%m/%d/%Y %H:%M.%S') + '\n' + Fore.WHITE + str(i['card_ids']) + '\n------------------------------')
            print(Fore.LIGHTRED_EX + '\n==== ==== > Tickets < ==== ====\n')
            for i in store['histories']['other']:
                print(Fore.LIGHTRED_EX + str(i['name']) + ' - ' + str(i[
                    'price']) + ' Ticket(s)\n' + Fore.CYAN + datetime.utcfromtimestamp(int(i['drawn_at'])).strftime(
                    '%m/%d/%Y %H:%M.%S') + '\n' + Fore.WHITE + str(i['card_ids']) + '\n------------------------------')
        else:
            error.Handler('history', store)
        return 0
    # identifier
    if args[0].lower() == 'identifier' and config.loaded != None:
        print(config.account)
        return 0
    # info
    if args[0].lower() == 'info' and config.loaded != None:
        store = ingame.user(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, False)
        if 'error' not in store:
            user = store['user']
            store = ingame.cards(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
            box = str(len(store['cards']))
            print(Fore.YELLOW + 'Account information\nVersion: ' + config.acc_ver + '\nOS: ' + config.acc_os + '\nID: ' + str(user['id']) + '\nName: ' + user['name'] + '\nRank: ' + str(user['rank']) + '\nStones: ' + str(user['stone']) + '\nZeni: ' + str(user['zeni']) + '\nStamina: ' + str(user['act']) + '/' + str(user['act_max']) + '\nCapacity: ' + box + '/' + str(user['total_card_capacity']) + '\nTeam cost: ' + str(user['team_cost_capacity']) + '\nFriends capacity: ' + str(user['friends_capacity']))
        else:
            error.Handler('info user', store)
        return 0
    # items
    if args[0].lower() == 'items' and config.loaded != None:
        store = ingame.getItems(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            print(Fore.LIGHTYELLOW_EX + '==== ==== > Support < ==== ====\n')
            for i in store['support_items']['items']:
                try:
                    print(database.fetch(config.acc_ver + '.db', 'support_items', 'id=' + str(i['item_id']))[1] + ' x' + str(i['quantity']))
                except:
                    print('Support x' + str(i['quantity']))
            print('\n' + Fore.LIGHTYELLOW_EX + '==== ==== > Training < ==== ====\n')
            for i in store['training_items']:
                try:
                    print(database.fetch(config.acc_ver + '.db', 'training_items', 'id=' + str(i['training_item_id']))[1] + ' x' + str(i['quantity']))
                except:
                    print('Training x' + str(i['quantity']))
            print('\n' + Fore.LIGHTYELLOW_EX + '==== ==== > Potential < ==== ====\n')
            for i in store['potential_items']['user_potential_items']:
                try:
                    print(database.fetch(config.acc_ver + '.db', 'potential_items', 'id=' + str(i['potential_item_id']))[1] + ' x' + str(i['quantity']))
                except:
                    print('Orb x' + str(i['quantity']))
            print('\n' + Fore.LIGHTYELLOW_EX + '==== ==== > Treasure < ==== ====\n')
            for i in store['treasure_items']['user_treasure_items']:
                try:
                    print(database.fetch(config.acc_ver + '.db', 'treasure_items', 'id=' + str(i['treasure_item_id']))[1] + ' x' + str(i['quantity']))
                except:
                    print('Treasure x' + str(i['quantity']))
            print('\n' + Fore.LIGHTYELLOW_EX + '==== ==== > Special < ==== ====\n')
            for i in store['special_items']:
                try:
                    print(database.fetch(config.acc_ver + '.db', 'special_items', 'id=' + str(i['special_item_id']))[1] + ' x' + str(i['quantity']))
                except:
                    print('Special x' + str(i['quantity']))
        else:
            error.Handler('items', store)
        return 0
    # legend
    if args[0].lower() == 'legend' and config.loaded != None:
        print('this will be coming in a later update. Cheers!')
    # link
    if args[0].lower() == 'link' and config.loaded != None:
        if len(args) == 2:
            if args[1] == 'list' or args[1] == 'fb' or args[1] == 'unlink':
                if args[1] == 'list':
                    store = transfer.links(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                    if 'error' not in store:
                        print(Fore.LIGHTYELLOW_EX + 'Facebook: ' + store['external_links']['facebook'] + '\nGame center: ' + store['external_links']['game_center'] + '\nGoogle play: ' + store['external_links']['google'] + '\nApple: ' + store['external_links']['apple'] + '\nTransfer code: ' + store['external_links']['link_code'])
                    else:
                        error.Handler('link-list', store)
                if args[1] == 'fb':
                    url = facebook.loginPage(config.acc_ver)
                    facebook.webView(config.acc_ver, config.acc_os, url, 2, config.sess_token, config.sess_secret)
                if args[1] == 'unlink':
                    store = transfer.facebookUnlink(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                    if 'error' not in store:
                        print(Fore.LIGHTGREEN_EX + 'account unlinked.')
                    else:
                        error.Handler('unlink', store)
            else:
                print('link <list/fb/unlink>')
        else:
            print('link <list/fb/unlink>')
        return 1
    # medals
    if args[0].lower() == 'medals' and config.loaded != None:
        store = ingame.getMedals(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            for i in store['awakening_items']:
                try:
                    print(database.fetch(config.acc_ver + '.db', 'awakening_items', 'id=' + str(i['awakening_item_id']))[1] + ' x' + str(i['quantity']))
                except:
                    print('unknown medal x' + str(i['quantity']))
        else:
            error.Handler('medals', store)
        return 0
    # name
    if args[0].lower() == 'name' and config.loaded != None:
        if len(args) == 2:
            if len(args[1]) > 0 and len(args[1]) <= 10:
                name = str(args[1])
                store = ingame.changeName(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, name)
                if 'error' not in store:
                    print(Fore.GREEN + 'name set as: ' + str(name))
                else:
                    error.Handler('name', store)
            else:
                print('name too long! (' + str(len(args[1])) + '/10)')
        else:
            print('no name provided.')
        return 0
    # news
    if args[0].lower() == 'news' and config.loaded != None:
        store = ingame.news(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
        if 'error' not in store:
            for i in store['announcements']:
                print(i['title'] + ' - ' + str(i['id']))
        else:
            error.Handler('news', store)
        return 0
    # omega
    if args[0].lower() == 'omega' and config.loaded != None:
        farmbot.gifts()
        farmbot.missions()
        farmbot.streamline('quests')
        utils.refresh()
        farmbot.streamline('events')
        utils.refresh()
        farmbot.streamline('ezas')
        utils.refresh()
        farmbot.gifts()
        farmbot.missions()
        return 0
    # sell
    if args[0].lower() == 'sell' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'quick':
                farmbot.sellUseless()
            else:
                farmbot.sellSpecific(args[2])
        else:
            print('sell <card uid/quick>')
        return 0
    # refresh
    if args[0].lower() == 'refresh' and config.loaded != None:
        utils.refresh()
        return 0
    # run
    if args[0].lower() == 'run' and config.loaded != None:
        if len(args) == 2:
            if args[1] == '1':
                #daily
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['events']:
                        if int(i['id']) == 111 or int(i['id']) == 116 or int(i['id']) == 120 or int(i['id']) == 130 or int(i['id']) == 131 or int(i['id']) == 132 or int(i['id']) == 134 or int(i['id']) == 135 or int(i['id']) == 177:
                            if 'quests' in i:
                                for x in i['quests']:
                                    for j in database.fetchAll(config.acc_ver + '.db', 'sugoroku_maps', 'quest_id=' + str(x['id'])):
                                        farmbot.runStage(x['id'], j[2], None)
                else:
                    error.Handler('daily1', store)
                farmbot.missions()
                farmbot.gifts()
            if args[1] == '2':
                #bossrush
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['events']:
                        if int(i['id']) == 701:
                            if 'quests' in i:
                                for x in i['quests']:
                                    for j in database.fetchAll(config.acc_ver + '.db', 'sugoroku_maps',
                                                               'quest_id=' + str(x['id'])):
                                        farmbot.runStage(x['id'], j[2], None)
                else:
                    error.Handler('bossrush', store)
            if args[1] == '3':
                #hercule punch
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['events']:
                        if int(i['id']) == 711:
                            if 'quests' in i:
                                for x in i['quests']:
                                    for j in database.fetchAll(config.acc_ver + '.db', 'sugoroku_maps',
                                                               'quest_id=' + str(x['id'])):
                                        farmbot.runStage(x['id'], j[2], None)
                else:
                    error.Handler('herculeP', store)
            if args[1] == '4':
                #sbr
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['events']:
                        if int(i['id']) == 710:
                            if 'quests' in i:
                                for x in i['quests']:
                                    for j in database.fetchAll(config.acc_ver + '.db', 'sugoroku_maps', 'quest_id=' + str(x['id'])):
                                        farmbot.runStage(x['id'], j[2], None)
                else:
                    error.Handler('sbr', store)
            if args[1] == '5':
                #potential
                store = ingame.events(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                if 'error' not in store:
                    for i in store['events']:
                        if i['id'] >= 140 and i['id'] < 145:
                            try:
                                stage = \
                                database.fetch(config.acc_ver + '.db', 'sugoroku_maps', 'quest_id=' + str(i['quests'][0]['id']))[0]
                                farmbot.runStage(str(stage)[0:-1], str(stage)[-1], None)
                            except:
                                print('stage does not exist.')
                else:
                    error.Handler('potential', store)
        return 0
    # stam
    if args[0].lower() == 'stam' and config.loaded != None:
        farmbot.restore()
        return 0
    # summon
    if args[0].lower() == 'summon' and config.loaded != None:
        if len(args) == 3:
            if args[2] == 's' or args[2] == 'm':
                if args[2] == 's': course = 1
                if args[2] == 'm': course = 2
                farmbot.summon(args[1], course)
                farmbot.gifts()
            else:
                print('invalid single/multi input.')
        else:
            print('ID s/m')
        return 0
    # team
    if args[0].lower() == 'team' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                one = []
                two = []
                three = []
                four = []
                five = []
                six = []
                store = ingame.cards(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                store2 = ingame.getTeams(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                print('Current team: ' + str(store2['selected_team_num']))
                for i in store['cards']:
                    if i['id'] in store2['user_card_teams'][0]['user_card_ids']:
                        element = ''
                        try:
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                            one.append(element + ' ' +
                                       database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                           1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills',
                                                                      'id=' + str(database.fetch(config.acc_ver + '.db',
                                                                                                 'cards', 'id=' + str(
                                                                              i['card_id']))[24]))[
                                           1] + '],\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(i['exp']))
                        except:
                            one.append('not in database. ' + str(i['card_id']))
                    if i['id'] in store2['user_card_teams'][1]['user_card_ids']:
                        element = ''
                        try:
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                            two.append(element + ' ' +
                                       database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                           1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills',
                                                                      'id=' + str(database.fetch(config.acc_ver + '.db',
                                                                                                 'cards', 'id=' + str(
                                                                              i['card_id']))[24]))[
                                           1] + '],\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(i['exp']))
                        except:
                            two.append('not in database. ' + str(i['card_id']))
                    if i['id'] in store2['user_card_teams'][2]['user_card_ids']:
                        element = ''
                        try:
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                            three.append(element + ' ' +
                                       database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                           1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills',
                                                                      'id=' + str(database.fetch(config.acc_ver + '.db',
                                                                                                 'cards', 'id=' + str(
                                                                              i['card_id']))[24]))[
                                           1] + '],\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(i['exp']))
                        except:
                            three.append('not in database. ' + str(i['card_id']))
                    if i['id'] in store2['user_card_teams'][3]['user_card_ids']:
                        element = ''
                        try:
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                            four.append(element + ' ' +
                                       database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                           1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills',
                                                                      'id=' + str(database.fetch(config.acc_ver + '.db',
                                                                                                 'cards', 'id=' + str(
                                                                              i['card_id']))[24]))[
                                           1] + '],\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(i['exp']))
                        except:
                            four.append('not in database. ' + str(i['card_id']))
                    if i['id'] in store2['user_card_teams'][4]['user_card_ids']:
                        element = ''
                        try:
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                            five.append(element + ' ' +
                                       database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                           1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills',
                                                                      'id=' + str(database.fetch(config.acc_ver + '.db',
                                                                                                 'cards', 'id=' + str(
                                                                              i['card_id']))[24]))[
                                           1] + '],\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(i['exp']))
                        except:
                            five.append('not in database. ' + str(i['card_id']))
                    if i['id'] in store2['user_card_teams'][5]['user_card_ids']:
                        element = ''
                        try:
                            db_ele = database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13]
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
                            six.append(element + ' ' +
                                       database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                           1] + ' [' + database.fetch(config.acc_ver + '.db', 'leader_skills',
                                                                      'id=' + str(database.fetch(config.acc_ver + '.db',
                                                                                                 'cards', 'id=' + str(
                                                                              i['card_id']))[24]))[
                                           1] + '],\n' + Fore.LIGHTWHITE_EX + 'SA: ' + str(i['skill_lv']) + '/' + str(
                                database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                    15]) + ', Potential: ' + str(i['released_rate']) + '%, EXP: ' + str(i['exp']))
                        except:
                            six.append('not in database. ' + str(i['card_id']))
                print(Fore.WHITE + '==== ==== > #1 < ==== ====\n' + ',\n'.join(one))
                print(Fore.WHITE + '\n==== ==== > #2 < ==== ====\n' + ',\n'.join(two))
                print(Fore.WHITE + '\n==== ==== > #3 < ==== ====\n' + ',\n'.join(three))
                print(Fore.WHITE + '\n==== ==== > #4 < ==== ====\n' + ',\n'.join(four))
                print(Fore.WHITE + '\n==== ==== > #5 < ==== ====\n' + ',\n'.join(five))
                print(Fore.WHITE + '\n==== ==== > #6 < ==== ====\n' + ',\n'.join(six))
            if args[1] == 'set':
                if len(args) >= 3:
                    if int(args[2]) >= 1 and int(args[2]) <= 6:
                        store = ingame.getTeams(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
                        if 'error' not in store:
                            teams = []
                            for x in store['user_card_teams']:
                                teams.append(x)
                            store2 = ingame.setTeam(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, args[2], teams)
                            if 'error' not in store2:
                                print(Fore.GREEN + 'set to deck #' + str(args[2]))
                            else:
                                error.Handler('teams set', store2)
                        else:
                            error.Handler('teams', store)
                    else:
                        print('invalid team number.')
                else:
                    print('no deck number provided.')
            if args[1] == 'build':
                print('this will be coming in a later update. Cheers!')
        else:
            print('team <list/set/build>')
        return 0
    #
    if args[0].lower() == 'toggle' and config.loaded != None:
        if len(args) == 2:
            if args[1] == 'stone':
                settings = utils.getSettings()
                settings['stam_use_stone'] ^= True
                utils.saveSettings(settings)
                print(Ftoggleore.LIGHTGREEN_EX + 'Stone usage: ' + str(settings['stam_use_stone']))
            if args[1] == 'tb':
                settings = utils.getSettings()
                settings['team_builder'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Team builder: ' + str(settings['team_builder']))
            if args[1] == 'drops':
                settings = utils.getSettings()
                settings['display_drops'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Drops: ' + str(settings['display_drops']))
            if args[1] == 'ids':
                settings = utils.getSettings()
                settings['display_ids'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Card IDs: ' + str(settings['display_ids']))
            if args[1] == 'cards':
                settings = utils.getSettings()
                settings['display_only_ids'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Only card IDs: ' + str(settings['display_only_ids']))
            if args[1] == 'names':
                settings = utils.getSettings()
                settings['display_stage_names'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Stage names: ' + str(settings['display_stage_names']))
            if args[1] == 'bonus':
                settings = utils.getSettings()
                settings['drop_bonus'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Drop bonus: ' + str(settings['drop_bonus']))
            if args[1] == 'dupe':
                settings = utils.getSettings()
                settings['potential_node'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Feed dupes: ' + str(settings['potential_node']))
            if args[1] == 'item':
                settings = utils.getSettings()
                settings['stam_use_item'] ^= True
                utils.saveSettings(settings)
                print(Fore.LIGHTGREEN_EX + 'Item usage: ' + str(settings['stam_use_item']))
        else:
            print(Fore.LIGHTRED_EX + 'toggle <stone/tb>')
        return 0
    # train
    if args[0].lower() == 'train' and config.loaded != None:
        if len(args) == 3:
            if ',' in str(args[2]):
                cards = []
                spl = str(args[2]).split(',')
                for i in spl:
                    cards.append(int(i))
            else:
                cards = [int(args[2])]
            items = []
            store = ingame.train(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, args[1], cards, 1, items)
            if 'error' not in store:
                print(Fore.GREEN + 'S U C C E S S !')
            else:
                error.Handler('train', store)
        else:
            print('train <card uid> <card uid,card uid,card uid>')
        return 0
    '''
    #transfer
    if args[0].lower() == 'transfer' and config.loaded != None:
        if config.acc_ver == 'gb':
            utils.refresh()
            utils.checkTcLoop(config.account)
        else:
            print('this can\'t be used on JP.')
        return 0
    '''
    # wallpaper
    if args[0].lower() == 'wallpaper' and config.loaded != None:
        if len(args) >= 2:
            if args[1] == 'list':
                d = database.fetchAll(config.acc_ver + '.db', 'wallpaper_items', None)
                if d != None and len(d) != 0:
                    for i in d:
                        print(Fore.LIGHTGREEN_EX + '#' + str(i[0]) + ' - ' + str(i[1]) + '\n' + Fore.LIGHTCYAN_EX + i[2])
                else:
                    print(Fore.LIGHTRED_EX + 'no wallpapers in database!')
            if args[1] == 'set':
                if len(args) == 3:
                    store = ingame.setWallpaper(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, args[2])
                    if 'error' not in store:
                        wallname = database.fetch(config.acc_ver + '.db', 'wallpaper_items', 'id=' + str(args[2]))
                        if wallname != None:
                            print(Fore.GREEN + 'set as: ' + str(args[2]) + ' - ' + str(wallname[1]))
                        else:
                            print(Fore.GREEN + 'set as: ' + str(args[2]))
                    else:
                        error.Handler('wallpaper', store)
                else:
                    print(Fore.LIGHTRED_EX + 'missing wallpaper ID.')
        else:
            print(Fore.LIGHTRED_EX + 'wallpaper <list/set>')
        return 0