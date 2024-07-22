# -*- coding: utf-8 -*-

import requests
import os
from colorama import Fore
from urlextract import URLExtract

# ... rest of your code ...

yl = Fore.YELLOW
red = Fore.RED
gr = Fore.GREEN


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"}
def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(red + "××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
    print(gr  + "×                                                      ×")
    print(gr  + "×                   FREE REVERSE IP                    ×")
    print(gr  + "×                 CODED BY HARRY_1337                  ×")
    print(gr  + "×              TEAM - INDIAN CYBER TROOPS              ×")
    print(gr  + "×                   TG- @botmanarmy                    ×")
    print(red + "××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
    print(gr  +  "       -MASS FIND WEBSITE HOSTED ON SAME IP-\n         ")

def grab():
    sites = input("ENTER FILE OF IPS :")
    Files = open(sites)
    for i in Files.readlines():
        site = i.strip()
        try:
            site = site.strip()
            resp = requests.get('https://askdns.com/ip/' + site, headers=headers ).text
            if "Domain Neighbors" in resp:
                extractor = URLExtract()
                ext = extractor.find_urls(resp)
                ext = ext[5:-3]
                for i in ext:
                    print(i)
                    f = open("reverse.txt", 'a')
                    f.write(i + '\n')
            else:
                print("Dead IP")
        except:
            pass

banner()
grab()



