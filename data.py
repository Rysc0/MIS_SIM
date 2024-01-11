# Generator dolazaka
# -----------------------------------------------------------------------------------------------
# Generira se random broj dolazaka koji se prikazuje kao timestamp unutar 5-minutnog razdoblja. 
# Promatrano vrijeme je zadano kao dictionary 'dolasci' u koji se dodaju timestampovi. Tako će 
# npr za razdoblje od 11:00 - 11:05 biti generirano 15 dolazaka koji će biti prikazani kao vremena 
# 0:58, 1:25, 4:32 -> to znači da je prvi dolazak u 11:58, drugi 11:25 itd.
# Nakon što je dictionary popunjen zapisuje se u json file.
# -----------------------------------------------------------------------------------------------
import random
import json

# Definiranje raspona za broj dolazaka
MIN_ARRIVAL = 10
MAX_ARRIVAL = 20

dolasci = {
    "11:00":"",
    "11:05":"",
    "11:10":"",
    "11:15":"",
    "11:20":"",
    "11:25":"",
    "11:30":"",
    "11:35":"",
    "11:40":"",
    "11:45":"",
    "11:50":"",
    "11:55":"",
    "12:00":"",
    "12:05":"",
    "12:10":"",
    "12:15":"",
    "12:20":"",
    "12:25":"",
    "12:30":"",
    "12:35":"",
    "12:40":"",
    "12:45":"",
    "12:50":"",
    "12:55":"",
    "13:00":"",
    "13:05":"",
    "13:10":"",
    "13:05":"",
    "13:20":"",
    "13:25":"",
    "13:30":"",
    "13:35":"",
    "13:40":"",
    "13:45":"",
    "13:50":"",
    "13:55":"",
    "14:00":"",
    "14:05":"",
    "14:10":"",
    "14:15":"",
    "14:20":"",
    "14:25":"",
    "14:30":"",
    "14:35":"",
    "14:40":"",
    "14:45":"",
    "14:50":"",
    "14:55":"",
    "15:00":""
}


br = dolasci.copy()

for timestamp in dolasci:
    _timeArray = []
    for x in range(random.randrange(MIN_ARRIVAL,MAX_ARRIVAL)): 
        _timestamp = ""
        minute = '0' + str(random.randrange(0,4))
        seconds = str(random.randrange(0,59))

        if len(seconds) < 2:
            seconds = '0' + seconds 
        
        _timestamp = minute + ':' + seconds
        _timeArray.append(_timestamp)
    br[timestamp] = len(_timeArray)
    dolasci[timestamp] = sorted(_timeArray)

with open('data.json', 'w') as f:
    json.dump(dolasci, f)

with open('arrivals.json', 'w') as f:
    json.dump(br, f)

# print(dolasci)
# print(br)
