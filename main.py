from functions import *

A = [[0,0,0],[0,0,0],[0,0,0]]

oudeMatricesA = []

K = {
    "a": int(input('Coëfficient bij x^2? ')),
    "a1": int(input('Coëfficient bij y^2? ')),
    "a2": int(input('Coëfficient bij z^2? ')),
    "b2": int(input('Coëfficient bij xy?  '))/2,
    "b1": int(input('Coëfficient bij xz?  '))/2,
    "b": int(input('Coëfficient bij yz?  '))/2
}

a, a1, a2, b2, b1, b = list(K.values())

A = [
    [a,b2,b1],
    [b2,a1,b],
    [b1,b,a2]
]

d = det2x2([[a, b2], [a1, b2]])
D = det3x3(A)

print('D =')
print('  ' + str(A[0]))
print('  ' + str(A[1]))
print('  ' + str(A[2]))
print('δ = ' + str(d))
print('Δ = ' + str(D))

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
aard = classificeer(a, d, D)

print('De kegelsnede is een prachtige ' + aarden[aard])

if b2 != 0:
    oudeMatricesA.append(A)
    A = xyWegwerken(A)