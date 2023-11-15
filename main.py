from functions import *

A = [[0,0,0],[0,0,0],[0,0,0]]

A[0][0] = int(input('Coëfficient bij x^2? '))
A[1][1] = int(input('Coëfficient bij y^2? '))
A[2][2] = int(input('Coëfficient bij z^2? '))
A[0][1] = int(input('Coëfficient bij xy? '))/2
A[1][0] = A[0][1]
A[0][2] = int(input('Coëfficient bij xz? '))/2
A[2][0] = A[0][2]
A[1][2] = int(input('Coëfficient bij yz? '))/2
A[2][1] = A[1][2]

d = det2x2([[A[0][0], A[0][1]], [A[1][0], A[1][1]]])
D = det3x3(A)

print(A)
print(d)
print(D)