#!/usr/bin/python3.8
import subprocess
from urllib.parse import urlencode

# AQUIRE SHORTCUTS
# 

shortcuts = {
    'calendar': 'https://calendar.google.com/calendar/',
    'mycourses': 'https://mycourses.rit.edu/',
    'leees.store': 'https://leees.store/'
}

# PROMPT USER
#

options = "\n".join(shortcuts.keys())
selected = subprocess.check_output("echo -e '"+options+"' | bemenu -m all -p search", shell=True).decode().strip()


# DETERMINE URL
#

if selected in shortcuts:
    # go to shortcut
    url = shortcuts[selected]
else:
    # google search what was entered
    query = urlencode({"q": selected})
    url = "https://duckduckgo.com/?" + query


# OPEN BROWSER
#

subprocess.check_call("epiphany "+url, shell=True)
