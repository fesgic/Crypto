#!/bin/python3
import Crypto.Util.number

interger = int(input("Enter your interger here: "))

byte = interger.to_bytes(50,'big')
flag = byte.decode("ascii")
print(flag)
