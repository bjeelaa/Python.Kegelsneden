def det2x2(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return det

def det3x3(A):
    det = A[0][0]*A[1][1]*A[2][2] + A[0][2]*A[1][0]*A[2][1] + A[0][1]*A[1][2]*A[2][0] - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1]
    return det

def mult3x3(A,B):
    AxB = [[0,0,0],[0,0,0],[0,0,0]]
    AxB[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0]
    AxB[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1]
    AxB[0][2] = A[0][0]*B[0][2] + A[0][1]*B[1][2] + A[0][2]*B[2][2]
    AxB[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0]
    AxB[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1]
    AxB[1][2] = A[1][0]*B[0][2] + A[1][1]*B[1][2] + A[1][2]*B[2][2]
    AxB[2][0] = A[2][0]*B[0][0] + A[2][1]*B[1][0] + A[2][2]*B[2][0]
    AxB[2][1] = A[2][0]*B[0][1] + A[2][1]*B[1][1] + A[2][2]*B[2][1]
    AxB[2][2] = A[2][0]*B[0][2] + A[2][1]*B[1][2] + A[2][2]*B[2][2]
    return AxB

def transponeer3x3(A):
    return list(zip(*A))

def KgsnNaarMatrix(K):
    a, a1, a2, b2, b1, b = list(K.values())
    A = [
        [a,b2,b1],
        [b2,a1,b],
        [b1,b,a2]
    ]
    return A

def classificeer(a, d, D):
    aard = 0
    if d > 0: #ellips
        if a * D < 0: aard = 1
        elif a * D > 0: aard = 2
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
    return aard

def xyWegwerken(K):
    a, a1, a2, b2, b1, b = list(K.values())
    
    if a!=0:
        # m1=0 is asympt. dus geen optie
        m1Optie = int(input('1. m1 = 0\n2. m1 invoeren\n3. m1*m2 = -1'))
        while m1Optie not in [1,2]:
            m1Optie = int(input('1. m1 = 0\n2. m1 invoeren\n3. m1*m2 = -1\n'))
        if m1Optie == 1:
            # m1 = 0 -> m2 = a/b2
            m1 = 0
            
            T = [[1,b2,0],[0,0-a,0],[0,0,1]]
            
            nieuweA = mult3x3(mult3x3(transponeer3x3(T),KgsnNaarMatrix(K)),T)
            
            pass
        elif m1Optie == 2:
            # m1 invoeren
            m1 = int(input('m1 = '))
            
            T = [[1,(a1*m1+b2),0],[0,(0-a-b2*m1),0],[0,0,1]]
            
            nieuweA = mult3x3(mult3x3(transponeer3x3(T),KgsnNaarMatrix(K)),T)
            
            pass
        elif m1Optie == 3:
            # m1*m2 = -1
            pass
    else:
        # m1 kan best veel zijn
        pass
    return