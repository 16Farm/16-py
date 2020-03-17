import requests
import json
import config
import utils.crypto as crypto

def validate(ver, tc, fc):
    if ver == 'gb':
        url = config.gb_url + '/auth/link_codes/' + str(tc) + '/validate'
        code = config.gb_code
    else:
        url = config.jp_url + '/auth/link_codes/' + str(tc) + '/validate'
        code = config.jp_code
    headers = {
        'Accept': '*/*',
        'X-Language': config.lang,
        'X-Platform': 'android',
        'X-ClientVersion': code,
        'Content-Type': 'application/json',
        'User-Agent': config.device_agent1
    }
    data = {'eternal': True,'user_account': {'platform': 'android','user_id': fc}}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

def use(ver, os, tc, fc):
    if os == 'android':
        dn = config.device_name1
        dm = config.device_model1
        dv = config.device_ver1
        dua = config.device_agent1
    else:
        dn = config.device_name2
        dm = config.device_model2
        dv = config.device_ver2
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/auth/link_codes/' + str(tc)
        code = config.gb_code
    else:
        url = config.jp_url + '/auth/link_codes/' + str(tc)
        code = config.jp_code
    headers = {
        'Accept': '*/*',
        'X-Language': config.lang,
        'X-Platform': os,
        'X-ClientVersion': code,
        'Content-Type': 'application/json',
        'User-Agent': dua
    }
    data = {'eternal': True,'old_user_id': '','user_account': {'device': dn,'device_model': dm,'os_version': dv,'platform': os,'unique_id': config.uuid}}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

def create(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/auth/link_codes'
        auth = crypto.mac(ver, token, secret, 'POST', '/auth/link_codes')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/auth/link_codes'
        auth = crypto.mac(ver, token, secret, 'POST', '/auth/link_codes')
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
    data = {'eternal':True}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# validate whether account is linked
def facebookValidate(ver, os, id, token):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/succeed/facebook/validate'
        code = config.gb_code
    else:
        url = config.jp_url + '/user/succeed/facebook/validate'
        code = config.jp_code

    sign = {'facebook_id': str(id),'facebook_token': str(token)}

    enc_sign = crypto.encrypt_sign(json.dumps(sign))

    headers = {
        'Accept': '*/*',
        'X-Language': config.lang,
        'X-Platform': os,
        'X-ClientVersion': code,
        'Content-Type': 'application/json',
        'User-Agent': dua
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# get identifier from sign encrypted facebook ID & OAuth token
def facebook(ver, os, id, token):
    if os == 'android':
        dn = config.device_name1
        dm = config.device_model1
        dv = config.device_ver1
        dua = config.device_agent1
    else:
        dn = config.device_name2
        dm = config.device_model2
        dv = config.device_ver2
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/succeed/facebook'
        code = config.gb_code
        sign = {'facebook_id': str(id),'facebook_token': str(token),'user_account': {'device': dn,'device_model': dm,'os_version': dv,'platform': os,'unique_id': config.uuid}}
    else:
        url = config.jp_url + '/user/succeed/facebook'
        code = config.jp_code
        sign = {'facebook_id': str(id),'facebook_token': str(token),'user_account': {'device': dn,'device_model': dm,'os_version': dv,'platform': os,'unique_id': config.uuid}}

    enc_sign = crypto.encrypt_sign(json.dumps(sign))

    headers = {
        'Accept': '*/*',
        'X-Language': config.lang,
        'X-Platform': os,
        'X-ClientVersion': code,
        'Content-Type': 'application/json',
        'User-Agent': dua
    }
    data = {'sign': enc_sign}

    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# link with a facebook account via sign encrypted facebook ID & OAuth token
def facebookLink(ver, os, fb_id, fb_token, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/link/facebook'
        auth = crypto.mac(ver, token, secret, 'POST', '/user/link/facebook')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
        sign = {'facebook_id': str(fb_id),'facebook_token': str(fb_token)}
    else:
        url = config.jp_url + '/user/link/facebook'
        auth = crypto.mac(ver, token, secret, 'POST', '/user/link/facebook')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
        sign = {'facebook_id': str(fb_id),'facebook_token': str(fb_token)}

    enc_sign = crypto.encrypt_sign(json.dumps(sign))

    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': auth,
        'User-Agent': dua
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# unlink facebook account
def facebookUnlink(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/link/facebook'
        auth = crypto.mac(ver, token, secret, 'DELETE', '/user/link/facebook')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user/link/facebook'
        auth = crypto.mac(ver, token, secret, 'DELETE', '/user/link/facebook')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2

    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': auth,
        'User-Agent': dua
    }

    r = requests.delete(url, headers=headers)
    return r.json()

# get list of linked accounts
def links(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/links'
        auth = crypto.mac(ver, token, secret, 'GET', '/user/links')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user/links'
        auth = crypto.mac(ver, token, secret, 'GET', '/user/links')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2

    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': auth,
        'User-Agent': dua
    }

    r = requests.get(url, headers=headers)
    return r.json()