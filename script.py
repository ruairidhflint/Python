# GOAL - Write a small application to block websites being accessed by the browser

# - Find direct access to hosts file via Python
# - Use SUDO to write new line with would be blocked website to hosts file
# - Save!
# - Run the cache flush

import os

host_path = "/private/etc/hosts"
redirect = "127.0.01"
blocked_list = ["https://rory.codes", "rory.codes", "www.rory.codes"]

host_file = open(os.path.expanduser(host_path))

host_content = host_file.read()

print(host_path)
print(host_content)