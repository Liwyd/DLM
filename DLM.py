import os
import platform
import sys
import requests
from urllib.parse import urlparse
import time
import random


class color:
    BBlack = "\033[1;30m"       # Black
    BRed = "\033[1;31m"         # Red
    BGreen = "\033[1;32m"       # Green
    BYellow = "\033[1;33m"      # Yellow
    BBlue = "\033[1;34m"        # Blue
    BPurple = "\033[1;35m"      # Purple
    BCyan = "\033[1;36m"        # Cyan
    BWhite = "\033[1;37m"       # White
def Print():
    Cls = '\x1b[0m'
    Colors = [32, 30, 32, 30, 30, 32]
    introduce = '''  _____  _                                                  
 |  __ \| |                                                 
 | |  | | |     _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 | |  | | |    | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |__| | |____| | | | | | (_| | | | | (_| | (_| |  __/ |   
 |_____/|______|_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                             __/ |    -by cinzentoo     
                                            |___/'''
    for N, Line in enumerate(introduce.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' %
                         (random.choice(Colors), Line, Cls))
        time.sleep(0.08)
def Clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def clear():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system("cls")
    else:
        os.system("clear")
# =======================
def Download(file_name, link):
    with open(file_name, "wb") as f:
        print(color.BBlue+"[DOWNLOADING]>> %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                print(color.BGreen+"", end="")
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
                sys.stdout.flush()
            time.sleep(0.8)
while 5 > 4.99999:
    Clear();Print()
    link = input(color.BPurple+"[?] Enter download link >> "+color.BGreen)
    Clear();Print()
    file_name = urlparse(link)
    file_name = file_name.query.rsplit('/')[2]
    Download(file_name, link)
    Clear();Print()
    print(color.BGreen+f"[FINISHED]>> {file_name}\t✓")
    WhatToDo = input("[?] DO uo want to continue?:(Y/N): ")
    if WhatToDo == 'Y' or WhatToDo == "y":
        continue
    else:
        Clear()
        break
