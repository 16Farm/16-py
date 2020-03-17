import requests
import sqlite3
import os as fs
import time
from threading import Timer
import config
import api.outgame as outgame
from pysqlsimplecipher import decryptor

def download(ver, token, secret, version):
    if ver == 'gb':
        p = config.gdb
    else:
        p = config.jdb
    print('downloading database... (this may take awhile.)')
    timer_start = int(round(time.time(), 0))
    store = outgame.getDatabase(ver, token, secret)
    url = store['url']
    r = requests.get(url, stream=True, allow_redirects=True)
    f = open('./data/enc_' + ver + '.db', 'wb')
    for chunk in r.iter_content(1024):
        f.write(chunk)
    f.close()
    timer_finish = int(round(time.time(), 0))
    timer_total = timer_finish - timer_start
    print(str(timer_total) + ' second(s) download.')
    print('decrypting... (this may take awhile.)')
    password = bytearray(p.encode('utf8'))
    timer_start = int(round(time.time(), 0))
    decryptor.decrypt_file('./data/enc_' + ver + '.db', password, './data/' + ver + '.db')
    fs.unlink('./data/enc_' + ver + '.db')
    f = open('./data/' + ver + '-data.txt', 'w')
    f.write(str(version) + '\n')
    f.close()
    timer_finish = int(round(time.time(), 0))
    timer_total = timer_finish - timer_start
    print(str(timer_total) + ' second(s) decrypt.')

def query(db, table, where, amount):
    con = sqlite3.connect('./data/' + db)
    cur = con.cursor()
    query = "SELECT * FROM " + table + " WHERE " + where
    cur.execute(query)
    if amount == 0:
        results = cur.fetchone()
    else:
        results = cur.fetchall()
    cur.close()
    con.close()
    return results

def fetch(db, table, where):
    if db == 'jp.db':
        if fs.path.isfile('./data/gb.db'):
            db = 'gb.db'
            return query(db, table, where, 0)
        else:
            return query(db, table, where, 0)
    if db == 'gb.db':
        return query(db, table, where, 0)

def fetchAll(db, table, where):
    if db == 'jp.db':
        if fs.path.isfile('./data/gb.db'):
            db = 'gb.db'
            return query(db, table, where, 1)
        else:
            return query(db, table, where, 1)
    if db == 'gb.db':
        return query(db, table, where, 1)