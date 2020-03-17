import time

version = '0'

# request defaults
gb_url = 'https://ishin-global.aktsk.com'
gb_port = '443'
jp_url = 'https://ishin-production.aktsk.jp'
jp_port = '443'

# version code
gb_code = '4.8.4-1fb3f1ffd7246672eab0056822a42360a9cf779441b51cb16c2558f9919b0bd4'
jp_code = '4.8.4-9f306810d506afe6b9fefeb102164e903c390000bd97169f7431c70af98a08c1'

# account defaults
lang = 'en'
country = 'US'
currency = 'USD'
uuid = '0f97df48-01e3-4d8f-8ba0-a1e8cced278c:5bf18553fe25d277'
ad = '95c27e08-72bb-4760-83e8-9e878d1999f8'

# cached account config
loaded = None #save file
account = '' #identifier
acc_os = '' #platform
acc_ver = '' #game version
sess_token = '' #session token
sess_secret = '' #session secret

#android
device_name1 = 'SM'
device_model1 = 'SM-S10'
device_ver1 = '9.0'
device_agent1 = 'Dalvik/2.1.0 (Linux; Android 9.0; SM-S10)'
#ios
device_name2 = 'iPhone'
device_model2 = 'iPhone XR'
device_ver2 = '13.0'
device_agent2 = 'CFNetwork/808.3 Darwin/16.3.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X)'

# client data
asset_ts = str(int(round(time.time(), 0))) #asset
db_ts = str(int(round(time.time(), 0))) #database
file_ts1 = str(int(round(time.time(), 0)))
db_ts1 = str(int(round(time.time(), 0)))
file_ts2 = str(int(round(time.time(), 0)))
db_ts2 = str(int(round(time.time(), 0)))

# database keys
gdb = '9bf9c6ed9d537c399a6c4513e92ab24717e1a488381e3338593abd923fc8a13b'
jdb = '2db857e837e0a81706e86ea66e2d1633'

# preferences
use_stone = True