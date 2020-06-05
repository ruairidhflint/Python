import os

host_path = "/private/etc/hosts"
redirect = "127.0.01"
blocked_list = ["https://rory.codes", "rory.codes", "www.rory.codes"]

with open(host_path, "r+") as file:
    host_content = file.read()
    for website in blocked_list:
        if website in host_content:
            pass
        else:
            file.write(f'{redirect} {website} \n')

os.system('sudo dscacheutil -flushcache')