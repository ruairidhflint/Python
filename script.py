import os
import time

host_path = "/private/etc/hosts"
redirect = "127.0.01"

while True:
    print('running...')
    with open('default.txt') as default:
        default_host = default.read()

    with open('settings.txt') as settings:
        blocked_list = settings.read().splitlines()

    with open(host_path, "r+") as file:
        file.seek(0)
        file.truncate()
        file.write(default_host)
        host_content = file.read()
        for website in blocked_list:
            if website in host_content:
                pass
            else:
                file.write(f'{redirect} {website} \n')

    os.system('sudo dscacheutil -flushcache')
    time.sleep(5)
