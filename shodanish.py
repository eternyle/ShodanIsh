#!/usr/bin/env python
# Shodan Favicon MurmurHash Converter
# pip install mmh3

import sys
import requests, mmh3
import argparse

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


def print_banner():
    banner = """
     __ _               _              _____     _     
    / _\ |__   ___   __| | __ _ _ __   \_   \___| |__  
    \ \| '_ \ / _ \ / _` |/ _` | '_ \   / /\/ __| '_ \ 
    _\ \ | | | (_) | (_| | (_| | | | /\/ /_ \__ \ | | |
    \__/_| |_|\___/ \__,_|\__,_|_| |_\____/ |___/_| |_|
                                                                                                                                                      
    """

    print(banner)
    print("\t\tShodan Favicon MurmurHash Converter")
    print("\t\tCoded with <3 By Aziz Hakim @eternyle\n")


def get_target(unprocessed_target):
    if unprocessed_target.startswith('http'):
        if unprocessed_target.endswith('favicon.ico'):
            # Input https://github.com/favicon.ico -> https://github.com/favicon.ico
            return unprocessed_target
        else:
            if unprocessed_target.endswith('/'):
                # Input https://github.com/ -> https://github.com/favicon.ico
                return '%sfavicon.ico' % unprocessed_target
            else:
                # Input https://github.com -> https://github.com/favicon.ico
                return '%s/favicon.ico' % unprocessed_target
    else:
        return 'http://%s/favicon.ico' % unprocessed_target


def run(arguments):
    if arguments.url is None or arguments.url.strip() == '':
        target = get_target(get_input("Enter Domain/URL : "))
    else:
        target = get_target(arguments.url)

    var = requests.get(target, verify=False)
    shodan_img_hash = get_hash(var.content)
    print("\nShodan Dork : http.favicon.hash:%s" % shodan_img_hash)
    print("\nVisit this URL : https://www.shodan.io/search?query=http.favicon.hash:%s" % shodan_img_hash)
    print("\n\t\t\tHave a nice day 1337")


if __name__ == '__main__':
    print_banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=False, help='The url of the favicon to process')
    args = parser.parse_args()
    run(args)
