#--------------------#
#                    #
#     u|n|i|k|s      #
#                    #
#--------------------#

#!/usr/bin/python



import requests
from datetime import datetime
from time import sleep


#here is where u set the stage \(o_o)/
#                                / \
requests.urllib3.disable_warnings()
client = requests.sessions()
client.verify = False


apik = input("entur ur apik boiii")


def hash_deets(apik,hash):
  url = 'https://www.virustotal.com/vtapi/v2/file/report'
  params = {'apikey' : api, 'resource' : hash, 'allinfo' : True}
  
  #call it up
  r.client.get(url, params=params)
  
  
