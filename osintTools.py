#--------------------#
#                    #
#     u|n|i|k|s      #
#                    #
#--------------------#

#!/usr/bin/python



import requests
from datetime import datetime
from time import sleep

print('.\n')
print('.\n')
print('.\n')
print('.\n')
#lame banner
print('-' *50)
print("starttime: "+str(datetime.now()))
print('-'*50)
print('.\n')
print('.\n')
print('.\n')
print('.\n')
#here is where u set the stage \(o_o)/
#                                / \
requests.urllib3.disable_warnings()
client = requests.session()
client.verify = False

#first t.liner
apik = input("entur ur apik boiii")

#setup the api and parametrzz
def hash_deets(apik,hash):
  url = 'https://www.virustotal.com/vtapi/v2/file/report'
  params = {'apikey' : api, 'resource' : hash, 'allinfo' : True}
  
  #call it up
  r.client.get(url, params=params)
  
  #if its successful, then great
  if r.status_code == 200:
    resp = r.json()
    parse_results(resp)
#if u get smt back; yay  
def parse_results(resp):
  if resp >= 1:
    scan_zults = resp['scans']
    #tell me wat i got back
    print('\nMalware Name, AV Name, Definitions Name, Last Updated\n')
    print('endtime: 'str(datetime.now()))
  else: #otherwise, i guess iz gud in tha hood
    print('nun found...\n')
    print('endtime: '+str(datetime.now()))
    
while True:
  hash = input('entur ur hash: \n')
  hash_deets(apik,hash)
    
  
