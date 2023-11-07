p=61
q=53
n=p*q
fi=(p-1)*(q-1)
e=7
d=0
for d in range(100000):
    if((e*d)%fi==1 and d<n):
        print(d)

def fnRSA(besedilo,kljuc,n):
    sifropis=""
    for char in besedilo:
        codec=chr(((ord(char))**kljuc)%n)
        sifropis+=codec
    return sifropis


sifropis=fnRSA("Preizkus delovanja",7,143)
print(sifropis)
print(fnRSA(sifropis,103,143))

import codecs
import numpy as np
file= codecs.open('sifropis-RSA.txt','r','utf-8')
sifropis=file.read()
n=527

for i in range(int(np.sqrt(n))+1):
    p=i
    if i!=0:
        if n%p==0:
            q=n/p
            if p>1 and q>1:
                for d in range(n):
                    e=13
                    if e*d%((p-1)*(q-1))==1:
                        print(p,q)
                        print(d)
                        a=fnRSA(sifropis,d,n)
                        print(a)
