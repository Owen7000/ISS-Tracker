from github import Github
import urllib.request, json, time, os
from secrets import token 


g = Github(token)
lat = []
lon = []
loops = 0
while loops < 7200:
    req = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
    obj = json.loads(req.read())
    lat.append(obj['iss_position']['latitude'])
    lon.append(obj['iss_position']['longitude'])
    print(obj['iss_position']['latitude'])
    print(obj['iss_position']['longitude'])
    loops = loops + 1
    time.sleep(5)
    try:
        os.system("cls")
    except:
        os.system("clear")

body = ''

for x in lat:
    body = body + lat[x] + "\t" + lon[x]

repo = g.get_repo("Owen7000/ISS-Tracker")
repo.create_pull(title="Data Dump", body=body)

