# GOAL - Write a small application to block websites being accessed by the browser

# - Find direct access to hosts file via Python
# - Use SUDO to write new line with would be blocked website to hosts file
# - Save!
# - Run the cache flush

import os

host_path = "/private/etc/hosts"
redirect = "127.0.01"
blocked_list = ["https://rory.codes", "rory.codes", "www.rory.codes"]

with open(host_path, "r+") as file:
    host_content = file.read()
    for website in blocked_list:
        if website in host_path:
            pass
        else:
            file.write(f'{redirect} {website} \n')