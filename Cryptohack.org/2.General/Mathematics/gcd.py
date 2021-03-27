#!/bin/python3
def gcd(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        c = a%b
        a = b
        b = c
        #a,b = b,c
    print(a)
def test():
    gcd(12,8)
if __name__ == "__main__":
    test()
    gcd(66528,52920)
