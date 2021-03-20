#!/bin/python3
import Crypto.Util.number
string= input("Enter your string here: ")
numbers = int(input("Enter number to XOR with here: "))
for x in string:
    xor = ord(x)^13
    print(chr(xor),end="")
