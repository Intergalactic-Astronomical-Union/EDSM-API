###############
#
# api.py is updated to work on Python 3.x
#
##########

import requests
import time

# simple text file with system names, one per line
# Important note: The first line of the input file must contain a dash (see included file)
filepath = 'input.txt'
system_name = 'error'
# this provides an api link, and completes the api call with system names from the text file above
baseurl = 'https://www.edsm.net/api-v1/system?showId=1&showCoordinates=1&showInformation=1&showPrimaryStar=1&systemName='

f = open('output.csv', 'w')

with open(filepath) as fp:
    count = 2 
    line = fp.readline()


    while line :

        try:
            line = fp.readline()
            print(line)
            stripline = line.strip()
            url = baseurl + stripline

# get api call response and make it json
            response = requests.get(url=url)
            data = response.json()
            #print(data)

# you could change these to any fields of interest in the EDSM API data.
            system_name = (data['name'])
            system_id64 = str(data['id64'])
            star_type = (data['primaryStar']['type'])
            spectral_class = star_type[0]

# Write out to standard output. Could be less lazy and write out to a .csv file.
            # output write ID64 value.
            output = str(count) + ',' + system_name + ',' + system_id64
            # output write stellar class
            #output = str(count) + ',' + system_name + ',' + type

            print (output)
            print (output, file=f)
            count += 1

# sleep for 4 seconds between api calls so we don't break EDSM.
            time.sleep(4)
        except:
            output = str(count) + ',' + 'error' + ',' + '0'
            print (output)
            print (output, file=f)
            #print ("error");
            # make sure the line number is incremented so we match source .csv file line numbers
            count += 1
