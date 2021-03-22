#!/bin/python3
from pwn import xor
import binascii
data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
#data_byte = bytes.fromhex(data)
byte = 0x00
print(byte)
data_byte = binascii.unhexlify(data)
for i in range(256):
    flag = xor(data_byte,byte)
    flag = flag.decode("utf-8")
    if "crypto" in flag:
        print(flag)
        break
    byte = byte+0x01
