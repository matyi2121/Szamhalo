# -*- coding: cp1250 -*-
from operator import add
v1 = [6,-4,-12]
mv1 = []
for el in v1:
    mv1.append(-1*el)
bitseq1 = "1110"
v2 = [-4,12,-6]
mv2 = []
for el in v2:
    mv2.append(-1*el)
bitseq2 = "1010"
v3 = [-12,-6,-4]

transmittedvec1 = []
transmittedvec2 = []

for char in bitseq1:
    if char == "1":
        transmittedvec1.append(v1)
    else:
        transmittedvec1.append(mv1)
print("első átviteli vektor")
print transmittedvec1


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
    s = (l[0]*v1[0])+(l[1]*v1[1])+(l[2]*v1[2])
    if s > 0:
        s = 1
    elif s < 0:
        s = 0
    elif s == 0:
        continue
    decode1.append(s)
print decode1
decode2 = []
for l in finalvec:
    s = (l[0]*v2[0])+(l[1]*v2[1])+(l[2]*v2[2])
    if s > 0:
        s = 1
    elif s < 0:
        s = 0
    elif s == 0:
        continue
    decode2.append(s)
print decode2
decode3 = []
for l in finalvec:
    s = (l[0]*v3[0])+(l[1]*v3[1])+(l[2]*v3[2])
    if s > 0:
        s = 1
    elif s < 0:
        s = 0
    elif s == 0:
        continue
    decode3.append(s)
print decode3
