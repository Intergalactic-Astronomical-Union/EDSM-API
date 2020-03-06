###############
#
# api.py is currently written for Python 2.x - a future update will port to Python 3.x
#
##########

from __future__ import print_function
import json
from urllib2 import urlopen
import requests
import time
import sys

# simple text file with system names, one per line
# Important note: The first line of the input file must contain a dash (see included file)
filepath = 'input-systems.txt'
system_name = 'error'
# this provides an api link, and completes the api call with system names from the text file above
baseurl = 'https://www.edsm.net/api-v1/system?showId=1&showCoordinates=1&showInformation=1&showPrimaryStar=1&systemName='

f = open('output-systems.csv', 'w')

with open(filepath) as fp:
    count = 2 
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
            #print(data)

# you could change these to any fields of interest in the EDSM API data.
            system_name = (data['name'])
            id64 = str(data['id64'])
            type = (data['primaryStar']['type'])
            spectral_class = type[0]

# Write out to standard output. Could be less lazy and write out to a .csv file.
            output = str(count) + ',' + system_name + ',' + id64

            print (output)
            print (output, file=f)
            count += 1

# sleep for 4 seconds between api calls so we don't break EDSM.
            time.sleep(4)
        except:
            pass
            output = str(count) + ',' + 'error' + ',' + '0';
            print (output)
            print (output, file=f)
            #print ("error");
            # make sure the line number is incremented so we match source .csv file line numbers
            count += 1
