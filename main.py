from functions import *

A = [[0,0,0],[0,0,0],[0,0,0]]

oudeMatricesA = []

A[0][0] = int(input('Coëfficient bij x^2? '))
A[1][1] = int(input('Coëfficient bij y^2? '))
A[2][2] = int(input('Coëfficient bij z^2? '))
A[0][1] = int(input('Coëfficient bij xy?  '))/2
A[1][0] = A[0][1]
A[0][2] = int(input('Coëfficient bij xz?  '))/2
A[2][0] = A[0][2]
A[1][2] = int(input('Coëfficient bij yz?  '))/2
A[2][1] = A[1][2]

d = det2x2([[A[0][0], A[0][1]], [A[1][0], A[1][1]]])
D = det3x3(A)

print(A[0])
print(A[1])
print(A[2])
print(d)
print(D)

aard = 0
aarden = [
    "error",                                                                    #! what the fuck
    "reële ellips",                                                             #* x^2 + y^2 = 1
    "imaginaire ellips",                                                        #* x^2 + y^2 = -1
    "ontaarde ellips",                                                          #* x^2 + y^2 = 0
    "reële hyperbool",                                                          #* x^2 - y^2 = 1
    "ontaarde hyperbool",                                                       #* x^2 - y^2 = 0
    "reële parabool",                                                           #* y = x^2
    "ontaarde parabool van 2 evenwijdige reële rechten",                        #* x^2 = 1
    "ontaarde parabool van 2 evenwijdige toegevoeg imaginaire rechten",         #* x^2 = -1
    "ontaarde parabool van 2 samenvallende rechten"                             #* x^2 = 0
]

#TODO gebruik later de aard als controle!
aard = classificeer(d,D)

print(aarden[aard])

if A[0][1] != 0:
    oudeMatricesA.append(A)
    A = xyWegwerken(A)