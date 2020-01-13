#--------------------#
#                    #
#     u|n|i|k|s      #
#                    #
#--------------------#

#!/usr/bin/python



import requests
from datetime import datetime
from time import sleep

print('-' *50)
print("starttime: "+str(datetime.now()))
print('-'*50)

#here is where u set the stage \(o_o)/
#                                / \
requests.urllib3.disable_warnings()
client = requests.session()
client.verify = False


apik = input("entur ur apik boiii")


def hash_deets(apik,hash):
  url = 'https://www.virustotal.com/vtapi/v2/file/report'
  params = {'apikey' : api, 'resource' : hash, 'allinfo' : True}
  
  #call it up
  r.client.get(url, params=params)
  
  if r.status_code == 200:
    resp = r.json()
    parse_results(resp)
  
def parse_results(resp):
  if resp >= 1:
    scan_zults = resp['scans']
    
    print('\nMalware Name, AV Name, Definitions Name, Last Updated\n')
  else:
    print('nun found...')
    
while True:
  hash = input('entur ur hash: \n')
  hash_deets(apik,hash)
    
  
