from colorama import init, Fore
init(autoreset=True)
import config
import utils.database as database
import api.ingame as ingame

def build(limits, cards, stage):
    friend = cards[0]['id']
    friend_card = cards[0]['leader']['card_id']
    condits = ['forbid_card_ids', 'only_elements', 'requiring_elements', 'allowed_category_ids', 'only_card_ids']
    plucked = []
    print(Fore.CYAN + 'building team...')

    box = ingame.cards(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)

    teams = ingame.getTeams(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret)
    decks = teams['user_card_teams']
    decks.remove(decks[0])
    if str(stage)[0:3] != '710':
        for j in limits:
            for x in j['conditions'].keys():
                if x in condits:
                    if x == 'forbid_card_ids':
                        for i in cards:
                            if i['leader']['card_id'] not in j['conditions']['forbid_card_ids']:
                                friend = i['id']
                                friend_card = i['leader']['card_id']
                                break
                            else:
                                continue
                        for i in box['cards']:
                            if i['card_id'] not in j['conditions']['forbid_card_ids']:
                                if len(plucked) < 1:
                                    plucked.append(int(i['id']))
                                else:
                                    break
                            else:
                                continue
                    if x == 'only_elements':
                        for i in cards:
                            #print(j)
                            #print(i)
                            if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] in j['conditions']['only_elements']:
                                friend = i['id']
                                friend_card = i['leader']['card_id']
                                break
                            else:
                                continue
                        for i in box['cards']:
                            if 'awakening_element_types' in j['conditions']:
                                elements = []
                                for k in j['conditions']['only_elements']:
                                    elements.append(k)
                                if j['conditions']['awakening_element_types'][0] in [1, 2]:
                                    elements.remove(0)
                                    elements.remove(1)
                                    elements.remove(2)
                                    elements.remove(3)
                                    elements.remove(4)
                            if len(elements) == 0:
                                elements = j['conditions']['only_elements']
                            if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[
                                13] in elements:
                                if len(plucked) < 1:
                                    plucked.append(int(i['id']))
                                else:
                                    break
                            else:
                                continue
                    if x == 'requiring_elements':
                        for i in cards:
                            if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[
                                13] in j['conditions']['requiring_elements']:
                                friend = i['id']
                                friend_card = i['leader']['card_id']
                                break
                            else:
                                continue
                        for i in box['cards']:
                            if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] in \
                                    j['conditions']['requiring_elements']:
                                if len(plucked) < len(j['conditions']['requiring_elements']):
                                    plucked.append(int(i['id']))
                                else:
                                    break
                            else:
                                continue
                    if x == 'allowed_category_ids':
                        for i in cards:
                            for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                                       'card_id=' + str(i['leader']['card_id'])):
                                if k[2] in j['conditions']['allowed_category_ids']:
                                    friend = i['id']
                                    friend_card = i['leader']['card_id']
                                    break
                                else:
                                    continue
                        for i in box['cards']:
                            for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                                       'card_id=' + str(i['card_id'])):
                                if k[2] in j['conditions']['allowed_category_ids']:
                                    if len(plucked) < 1:
                                        plucked.append(int(i['id']))
                                    else:
                                        break
                                else:
                                    continue
                    if x == 'only_card_ids':
                        for i in cards:
                            if i['leader']['card_id'] in j['conditions']['only_card_ids']:
                                friend = i['id']
                                friend_card = i['leader']['card_id']
                                break
                            else:
                                continue
                        for i in box['cards']:
                            if i['card_id'] in j['conditions']['only_card_ids']:
                                if len(plucked) < 1:
                                    plucked.append(int(i['id']))
                                else:
                                    break
                            else:
                                continue
    else:
        # vs. ext agl - 11
        if stage == '710001':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 11:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                print('checking cards... ' + str(i['card_id']))
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 11:
                    print('yes element')
                    if len(plucked) < 6:
                        print(str(i['card_id']))
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. s agl - 21
        if stage == '710002':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 21:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 21:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. ext teq - 12
        if stage == '710003':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 12:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 12:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. s teq - 22
        if stage == '710004':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 22:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 22:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. ext int - 14
        if stage == '710005':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 14:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 14:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. s int - 24
        if stage == '710006':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 24:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 24:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. ext str - 10
        if stage == '710007':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 10:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 10:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. s str - 20
        if stage == '710008':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 20:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 20:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. ext phy - 13
        if stage == '710009':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 13:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 13:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # vs. s phy - 23
        if stage == '710010':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] == 23:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] == 23:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # super class - 10, 11, 12, 13, 14
        if stage == '710011':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] in [10, 11,
                                                                                                                12, 13,
                                                                                                                14]:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] in [10, 11, 12, 13,
                                                                                                      14]:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # extreme class - 20, 21, 22, 23, 24
        if stage == '710012':
            for i in cards:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['leader']['card_id']))[13] in [20, 21,
                                                                                                                22, 23,
                                                                                                                24]:
                    friend = i['id']
                    friend_card = i['leader']['card_id']
                    break
                else:
                    continue
            for i in box['cards']:
                if database.fetch(config.acc_ver + '.db', 'cards', 'id=' + str(i['card_id']))[13] in [20, 21, 22, 23,
                                                                                                      24]:
                    if len(plucked) < 6:
                        plucked.append(int(i['id']))
                    else:
                        break
                else:
                    continue
        # fusion - 1
        if stage == '710013':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 1:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 1:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # shadow - 2
        if stage == '710014':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 2:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 2:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # peppy - 4
        if stage == '710015':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 4:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 4:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # hybrid - 5
        if stage == '710016':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 5:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 5:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # resurrected - 7
        if stage == '710017':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 7:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 7:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # ROG - 8
        if stage == '710018':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 8:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 8:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # majin - 9
        if stage == '710019':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 9:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 9:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # potara - 10
        if stage == '710020':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 10:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 10:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # universe - 6
        if stage == '710021':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 6:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 6:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # SSJ3 - 12
        if stage == '710022':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 12:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 12:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # giant - 13
        if stage == '710023':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 13:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 13:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # transformation - 23
        if stage == '710024':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 23:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 23:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # ginyu force - 15
        if stage == '710025':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 15:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 15:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # movie bosses - 16
        if stage == '710026':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 16:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 16:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # pure - 17
        if stage == '710027':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 17:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 17:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # future - 19
        if stage == '710028':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 19:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 19:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # full power - 20
        if stage == '710029':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 20:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 20:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
        # androids - 21
        if stage == '710030':
            for i in cards:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['leader']['card_id'])):
                    if k[2] == 21:
                        friend = i['id']
                        friend_card = i['leader']['card_id']
                        break
                    else:
                        continue
            for i in box['cards']:
                for k in database.fetchAll(config.acc_ver + '.db', 'card_card_categories',
                                           'card_id=' + str(i['card_id'])):
                    if k[2] == 21:
                        if len(plucked) < 6:
                            plucked.append(int(i['id']))
                        else:
                            break
                    else:
                        continue
    if len(plucked) > 0:
        if len(plucked) != 6:
            while len(plucked) < 6:
                plucked.append(0)
        new_decks = [{'num': 1, 'user_card_ids': plucked}]
        for i in decks:
            new_decks.append(i)
        store = ingame.setTeam(config.acc_ver, config.acc_os, config.sess_token, config.sess_secret, '1', new_decks)
        if 'error' not in store:
            print(new_decks[0])
            print(Fore.LIGHTGREEN_EX + 'team built - deck #1!')
        else:
            print(store)
    return [friend, friend_card]