#!/usr/bin/env python
# Shodan Favicon MurmurHash Converter
# pip install mmh3

import sys
import requests, mmh3

if sys.version_info[0] < 3:
    # Python 2
    get_input = raw_input


    def get_hash(content):
        return mmh3.hash(content.encode('base64'))
else:
    # Python 3
    import codecs

    get_input = input


    def get_hash(content):
        return mmh3.hash(codecs.encode(content, 'base64'))

banner = """
 __ _               _              _____     _     
/ _\ |__   ___   __| | __ _ _ __   \_   \___| |__  
\ \| '_ \ / _ \ / _` |/ _` | '_ \   / /\/ __| '_ \ 
_\ \ | | | (_) | (_| | (_| | | | /\/ /_ \__ \ | | |
\__/_| |_|\___/ \__,_|\__,_|_| |_\____/ |___/_| |_|
                                                                                                                                                  
"""

print(banner)
print("\t\tShodan Favicon MurmurHash Hashes Converter")
print("\t\tCoded with <3 By Aziz Hakim aka @4z1zu\n")

target = get_input("Enter Domain : ")
var = requests.get('http://%s/favicon.ico' % target, verify=False)
shodan_img_hash = get_hash(var.content)
print("\nShodan Dork : http.favicon.hash:%s" % shodan_img_hash)
print("\nVisit this URL : https://www.shodan.io/search?query=http.favicon.hash:%s" % shodan_img_hash)
print("\n\t\t\tHave a nice day 1337")
