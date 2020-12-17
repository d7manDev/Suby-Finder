import requests
from os import system
from sys import argv
system("clear")
domain = input("input your Target to scan:")
file = open("sub.text")
content = file.read()
subdomains = content.splitlines()
for subdomain in subdomains:
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("subdomain found at", url)
