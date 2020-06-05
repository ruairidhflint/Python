import os
import time
from datetime import datetime as dt

host_path = "/private/etc/hosts"
redirect = "127.0.0.1"

while True:
    with open('default.txt') as default:
        default_host = default.read()
    if 9 < dt.today().hour < 17:
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
    else:
        with open(host_path, "r+") as file:
            file.seek(0)
            file.truncate()
            file.write(default_host)

    os.system('sudo dscacheutil -flushcache')
    time.sleep(5)
