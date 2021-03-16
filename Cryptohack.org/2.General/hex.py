#!/bin/python3
import binascii
hex = input("Enter your hex here: ")
print(hex)
print(binascii.unhexlify(hex))
