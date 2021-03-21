#!/bin/python3
from pwn import xor
import binascii
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key2_3 = bytes.fromhex(key2_key3)
key_1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1 = bytes.fromhex(key_1)
flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag_key = bytes.fromhex(flag_key123)
flag = xor(key2_3,key1,flag_key)
print(flag.decode("ascii"))
