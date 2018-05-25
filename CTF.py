import sys
#Author: Samuel Lin
#This program is for Pactf 2018 Hash master. It is a brute force program.


Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)

hasha=0

for a in range(0, 25):
    for b in range(0, 25):
        for c in range(0, 25):
            for d in range(0, 25):
                for e in range(0, 25):
                    for f in range(0, 25):
                         l6 = (Letters[a]+Letters[b]+Letters[c]+Letters[d]+Letters[e]+Letters[f])
                         #print (l6)
                         hasha = hash_it(l6)
                         if hasha == 293366475:
                             print(l6)
                         
