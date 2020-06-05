# GOAL - Write a small application to block websites being accessed by the browser

# - Find direct access to hosts file via Python
# - Use SUDO to write new line with would be blocked website to hosts file
# - Save!
# - Run the cache flush

import os
# import subprocess

host_path = "/private/etc/hosts"
redirect = "127.0.01"
blocked_list = ["https://rory.codes", "rory.codes", "www.rory.codes"]
blocked_list2 = ["this", "is", "a", "test"]

with open(host_path, "r+") as file:
    host_content = file.read()
    for website in blocked_list2:
        if website in host_content:
            pass
        else:
            file.write(f'{redirect} {website} \n')

os.system('sudo dscacheutil -flushcache')