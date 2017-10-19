# -*- coding: cp1250 -*-
from operator import add
v1 = [1,-1]
mv1 = []
for el in v1:
    mv1.append(-1*el)
bitseq1 = "1010"
v2 = [1,1]
mv2 = []
for el in v2:
    mv2.append(-1*el)
bitseq2 = "0110"

transmittedvec1 = []
transmittedvec2 = []
print v1
print bitseq1
for char in bitseq1:
    if char == "1":
        transmittedvec1.append(v1)
    else:
        transmittedvec1.append(mv1)
print("első átviteli vektor")
print transmittedvec1

print v2
print bitseq2
for char in bitseq2:
    if char == "1":
        transmittedvec2.append(v2)
    else:
        transmittedvec2.append(mv2)
print("második átviteli vektor")
print transmittedvec2
print("együttes átviteli vektor")
finalvec = []
for l1,l2 in zip(transmittedvec1,transmittedvec2):
    finalvec.append(map(add,l1,l2))
print(finalvec)


#decode
print("dekódolás")
decode1 = []
for l in finalvec:
    s = (l[0]*v1[0])+(l[1]*v1[1])
    if s > 0:
        s = 1
    elif s < 0:
        s = 0
    decode1.append(s)
print decode1
decode2 = []
for l in finalvec:
    s = (l[0]*v2[0])+(l[1]*v2[1])
    if s > 0:
        s = 1
    elif s < 0:
        s = 0
    decode2.append(s)
print decode2
