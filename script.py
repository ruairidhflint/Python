import os
import time
from datetime import datetime as dt


# host_oath = Absolute path to hosts file on Mac and redirect = default local host file address
host_path = "/private/etc/hosts"
redirect = "127.0.0.1"

while True:
    # Default host is a file containing the original host file contents without any additions
    with open('default.txt') as default:
        default_host = default.read()
    # If the time is between 9am and 5pm:
    if 9 < dt.today().hour < 17:
        # Open settings file while contains list of blocked URLs
        with open('settings.txt') as settings:
            blocked_list = settings.read().splitlines()

        with open(host_path, "r+") as file:
            # Open host file,
            # Seek the beginning,
            # Delete everything currently there
            # Add the default contents to start fresh
            file.seek(0)
            file.truncate()
            file.write(default_host)
            host_content = file.read()
            # Loop through settings content list of blocked sites adding redirect address + the URL of the blocked site
            for website in blocked_list:
                file.write(f'{redirect} {website} \n')
    else:
        # If the time is outside of the 9-5 window, reset the host file to default.
        with open(host_path, "r+") as file:
            file.seek(0)
            file.truncate()
            file.write(default_host)
    # Flush the cache to ensure the sites are correctly blocked
    os.system('sudo dscacheutil -flushcache')
    # Wait 5 seconds and then restart
    time.sleep(5)
