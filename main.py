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

print(A[0])
print(A[1])
print(A[2])
print(d)
print(D)

aard = 0
alleAarden = [
    "error",
    "reële ellips",
    "imaginaire ellips",
    "ontaarde ellips",
    "reële hyperbool",
    "ontaarde hyperbool",
    "reële parabool",
    "ontaarde parabool van 2 evenwijdige reële rechten",
    "ontaarde parabool van 2 evenwijdige toegevoeg imaginaire rechten",
    "ontaarde parabool van 2 samenvallende rechten"
]

if d > 0: #ellips
    if A[0][0] * D < 0: aard = 1
    elif A[0][0] * D > 0: aard = 2
    elif D == 0: aard = 3
elif d < 0: #hyperbool
    if D != 0: aard = 4
    elif D == 0: aard = 5
elif d == 0: #parabool
    if D != 0: aard = 6
    elif D == 0: #ontaarde parabool
        if D > 0: aard = 7
        elif D < 0: aard = 8
        elif D == 0: aard = 9

print(alleAarden[aard])

wegMetDie_xy_term(A)