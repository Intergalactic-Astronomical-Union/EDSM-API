from __future__ import print_function
import json
from urllib2 import urlopen
import requests
import time
import sys

# simple text file with system names, one per line
filepath = 'input-systems.txt'

# this provides an api link, and completes the api call with system names from the text file above
baseurl = 'https://www.edsm.net/api-v1/system?showId=0&showCoordinates=0&showInformation=0&showPrimaryStar=1&systemName='

f = open('output-systems.csv', 'w')

with open(filepath) as fp:
    count = 1
    line = fp.readline()


    while line :

        try:
            line = fp.readline()
            stripline = format(line.strip())
            url = baseurl + stripline
            #print(format(line.strip()))

# get api call response and make is json
            response = requests.get(url=url)
            data = response.json()

# you could change these to any fields of interest in the EDSM API data.
#I was interested in Stellar Classes of primary stars.
            system_name = (data['name'])
            type = (data['primaryStar']['type'])
            spectral_class = type[0]

# Write out to standard output. Could be less lazy and write out to a .csv file.
            output = str(count) + ',' + system_name + ',' + spectral_class

            print (output)
            print (output, file=f)
            count += 1

# sleep for 4 seconds between api calls so we don't break EDSM.
            time.sleep(4)
        except:
            pass
