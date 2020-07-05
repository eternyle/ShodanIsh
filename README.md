
# ShodanIsh
Shodan Favicon MurmurHash Hash Converter By Aziz Hakim

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
Enter Domain/URL : azizu.me
```
- Non-Interactive
```
$ python shodanish.py --url azizu.me
$ python shodanish.py --url https://azizu.me
$ python shodanish.py --url https://azizu.me/
$ python shodanish.py --url https://azizu.me/favicon.ico
```

The input can be given in one of the following formats:
- hostname, http is used: `azizu.me` 
- base url: `https://azizu.me` or `https://azizu.me/`
- full url: `https://azizu.me/favicon.ico`

# Resources
- https://www.azizu.me/2020/05/shodan-favicon-hash-filter-to-get-juicy.html
- https://medium.com/@Asm0d3us/weaponizing-favicon-ico-for-bugbounties-osint-and-what-not-ace3c214e139

# Author
www.twitter.com/4z1zu - www.azizu.me

# Contributors

[Melardev](https://github.com/melardev)
