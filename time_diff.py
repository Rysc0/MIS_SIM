# Kalkulator vremena između dolazaka
# ---------------------------------------------------------------------------------
# Ova skripta koristi podatke o dolascima kako bi izračunala vremenski razmak
# između dolazaka (u sekundama). To znači da ukoliko u terminu 11:00 - 11:05 imamo 
# ovako zadane dolaske:
#       0:58, 1:25, 4:32
# skripta će kao rezultat dati:
#       58, 27, 187
# Što bi značilo da je od početka razdoblja do prvog dolaska prošlo 58 sekundi,
# od prvog do drugog dolaska je prošlo 27 sekundi a između drugog i trećeg dolaska
# prošlo je 187 sekundi (3 min i 7 sekundi).
# ---------------------------------------------------------------------------------
# FILE_NAME -> json datoteka koju je generirao generator dolazaka
# OUTPUT -> json datoteka sa izračunatim razmacima između dolazaka
# -----------------------------------------------------------------------

outData = {}

from datetime import datetime, timedelta
import json

FILE_NAME = "data.json"
OUTPUT = "time_diff.json"
# Open the JSON file
with open(FILE_NAME, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

    # Now 'data' contains the content of the JSON file
print(data)

ostatak = 0
previous = None

for TIME in data:

    base_time = datetime.strptime(TIME, "%H:%M")
    times = []

    # dobiti sva vremena
    allTimes = []
    razlika = 0
    for x in data[TIME]:


        if base_time not in allTimes:
            allTimes.append(base_time)

        vrijeme = datetime.strptime(x, '%M:%S')
        increment = timedelta(minutes=vrijeme.minute, seconds=vrijeme.second)

        # ovdje dodaj
        if previous != None:
            # dobiješ u sekundama
            razlika = int((base_time - previous).total_seconds())

        result_time = base_time + increment
        allTimes.append(result_time)
        


        # ako je dodan i zadnji timestamp za trenutno razdoblje
        if len(data[TIME])-1 == data[TIME].index(x):
            # kalkuliraj razmake
            for t in range(len(allTimes)):
                try:
                    if t == 0 and razlika > 0:
                        difference = int((allTimes[t+1] - allTimes[t]).total_seconds()) + razlika
                        razlika = 0
                    else:
                        difference = int((allTimes[t+1] - allTimes[t]).total_seconds())
                    times.append(difference)
                except:
                    print("Out of reach, got the final one")
            previous = allTimes[-1]
           
 
            

     
    outData[TIME] = times


with open(OUTPUT, 'w') as json_file:
    json.dump(outData, json_file, indent=4)


print(outData)





