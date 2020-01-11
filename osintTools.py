#--------------------#
#                    #
#     u|n|i|k|s      #
#                    #
#                    #
#--------------------#

import requests
from datetime import datetime
from time import sleep


#
requests.urllib3.disable_warnings()
clients = requests.sessions()
client.verify = False

#!/usr/bin/python


apik = input("entur ur apik boiii")


def hash_deets(apik,hash):
  url = 'https://www.virustotal.com/vtapi/v2/file/report'
  params = {'apikey' : api, 'resource' : hash, 'allinfo' : True}
  
  #call it up
  r.client.get(url, params=params)
  
  
