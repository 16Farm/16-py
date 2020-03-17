import sys
import os as fs
from colorama import init, Fore
init(autoreset=True)
from farming.commands import Handler
import utils.funcs as funcs

funcs.subfolders()

def getInput():
    while True:
        if Handler(input()) == 0:
            print(Fore.LIGHTYELLOW_EX + 'type "help" for a list of commands.')
            getInput()
        if Handler(input()) == 1:
            getInput()

print(Fore.YELLOW + 'fetching version(s)...')
funcs.getVersionCodes()
print(Fore.YELLOW + 'connecting to server(s)...')
if funcs.checkServers('gb') and funcs.checkServers('jp'):
    funcs.help1()
    getInput()
else:
    print('can\'t reach servers. check your connection.')