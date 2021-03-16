#!/bin/python3
import binascii
import base64

hex = input("Enter your hex here: ")

bytes = bytes.fromhex(hex)
message = base64.b64encode(bytes)
flag = message.decode("ascii")
print(flag)
