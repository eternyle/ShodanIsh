#!/bin/python2.7
#Shodan Favicon MurmurHash Converter
#pip install mmh3

import requests, mmh3

banner = """
 __ _               _              _____     _     
/ _\ |__   ___   __| | __ _ _ __   \_   \___| |__  
\ \| '_ \ / _ \ / _` |/ _` | '_ \   / /\/ __| '_ \ 
_\ \ | | | (_) | (_| | (_| | | | /\/ /_ \__ \ | | |
\__/_| |_|\___/ \__,_|\__,_|_| |_\____/ |___/_| |_|
                                                                                                                                                  
"""

print banner
print "\t\tShodan Favicon MurmurHash Hashes Converter"
print "\t\tCoded with <3 By Aziz Hakim aka @4z1zu\n"


target = raw_input("Enter Domain : ")
var = requests.get('http://%s/favicon.ico' % (target))
b64_encode = var.content.encode('base64')
encrypt = mmh3.hash(b64_encode)
print "\nShodan Dork : http.favicon.hash:%s" % (encrypt)
print "\nVisit this URL : https://www.shodan.io/search?query=http.favicon.hash:%s" % (encrypt)
exit ("\n\t\t\tHave a nice day 1337")
