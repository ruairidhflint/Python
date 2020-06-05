import os

host_path = "/private/etc/hosts"
redirect = "127.0.01"

with open('settings.txt') as settings:
    blocked_list = settings.read().splitlines()

with open(host_path, "r+") as file:
    host_content = file.read()
    for website in blocked_list:
        if website in host_content:
            pass
        else:
            file.write(f'{redirect} {website} \n')

os.system('sudo dscacheutil -flushcache')