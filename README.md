
# ShodanIsh
Shodan Favicon Murmur Hash Converter By Aziz Hakim @eternyle

This script retrieves the decimal hash that corresponds to an image,
the hash can be used on [shodan.io](https://shodan.io).

# mmh3 Installation

python get-pip.py install mmh3

get-pip.py ( https://bootstrap.pypa.io/get-pip.py )

# USAGE
- Interactive
```
$ python shodanish.py
....
Enter Domain/URL : azizhakim.com
```
- Non-Interactive
```
$ python shodanish.py --url azizhakim.com
$ python shodanish.py --url https://azizhakim.com
$ python shodanish.py --url https://azizhakim.com
$ python shodanish.py --url https://azizhakim.com/favicon.ico
```

The input can be given in one of the following formats:
- hostname, http is used: `azizhakim.com` 
- base url: `https://azizhakim.com` or `https://azizhakim.com/`
- full url: `https://azizhakim.com/favicon.ico`

# Resources
- https://www.azizhakim.com/2020/05/shodan-favicon-hash-filter-to-get-juicy.html
- https://medium.com/@Asm0d3us/weaponizing-favicon-ico-for-bugbounties-osint-and-what-not-ace3c214e139

# Author
www.twitter.com/eternyle - www.azizhakim.com

# Contributors

[Melardev](https://github.com/melardev)
