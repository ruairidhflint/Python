# GOAL - Write a small application to block websites being accessed by the browser

# - Find direct access to hosts file via Python
# - Use SUDO to write new line with would be blocked website to hosts file
# - Save!
# - Run the cache flush

import os

host_path = "/private/etc/hosts"

test = open(os.path.expanduser(host_path))

print(host_path)
print(test)