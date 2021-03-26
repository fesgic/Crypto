#!/bin/python3
def gcd(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        c = a%b
        a = b
        b = c
    print(a)

if __name__ == "__main__":
    gcd(66528,52920)
