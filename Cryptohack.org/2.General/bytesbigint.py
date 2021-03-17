#!/bin/python3
import Crypto.Util.number

interger = int(input("Enter your interger here: "))

byte = interger.to_bytes(50,'big')
#we use a big value value here to avoid an overflow
flag = byte.decode("ascii")
print(flag)
