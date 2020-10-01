#!/usr/bin/python3.8
import subprocess
from urllib.parse import urlencode

# AQUIRE SHORTCUTS
# 

shortcuts = {
    'calendar': 'https://calendar.google.com/calendar',
    'drive': 'https://drive.google.com',
    'drive-aaa': 'https://drive.google.com/drive/folders/1fJBEA4yA_VNvV-AKSPH-QvNHm-g0S9S8',
    'gmail': 'https://mail.google.com',
    'mycourses': 'https://mycourses.rit.edu/d2l/home',
    'youtube': 'https://youtube.com',
    'netflix': 'https://netflix.com',
    'twitch': 'https://twitch.tv',
    'trello': 'https://trello.com',
    'trello-aaa': 'https://trello.com/b/WZER6Q69/art-auth-ai',
    'trello-todo': 'https://trello.com/b/FxkBaoik/todo',
    'github': 'https://github.com/lxk1170',
    'quizlet': 'https://quizlet.com',
    'color-picker': 'https://color.adobe.com/create/color-wheel',
    'aws': 'https://console.aws.amazon.com',
    'aws-db': 'https://console.aws.amazon.com/dynamodb',
    'yellowdig': 'https://rit-saunders.yellowdig.app',
    'swen': 'http://www.se.rit.edu/~swen-561/CourseInformation/ProjectTimeline-FallSpring.html',
    'aaa-project': 'http://artauthai.github.io',
    'leonkuhne.com': 'https://leonkuhne.com',
    'career-fair': "https://rit-csm.symplicity.com/",
    'amazon': "https://amazon.com/",
    'vanguard': "https://personal.vanguard.com/us/faces/XHTML/prospecthome/welcomecenter.xhtml",
}

media = ["youtube", "netflix", "mycourses", "twitch"]

# PROMPT USER
#

options = "\n".join(shortcuts.keys())
selected = subprocess.check_output(f"echo -e '{options}' | bemenu -m all -p search", shell=True).decode().strip()


# DETERMINE URL
#

browser = "epiphany"

if selected in shortcuts:
    # if its media; firefox
    if selected in media:
        browser = "firefox"

    # go to shortcut
    url = shortcuts[selected]
else:
    # google search what was entered
    query = urlencode({"q": selected})
    url = f"https://duckduckgo.com/?{query}"


# OPEN BROWSER
#

subprocess.check_call(f"{browser} {url}", shell=True)
