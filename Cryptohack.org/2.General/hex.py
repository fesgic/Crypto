#!/bin/python3
import binascii
hex = input("Enter your hex here: ")
print(hex)
bytes = bytes.fromhex(hex)
print(bytes.decode("ASCII"))
#alternatively
print(binascii.unhexlify(hex))
