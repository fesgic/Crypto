#!/bin/python

from telnetlib import Telnet
import json

HOST = "socket.cryptohack.org"
port = 11112

command = {"buy":"flag"}
jsn = json.dumps(command).encode()

with Telnet (HOST,port) as tn:
    tn.write(jsn)
    tn.interact() 
