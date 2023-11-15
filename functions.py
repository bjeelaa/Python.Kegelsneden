def det2x2(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return det

def det3x3(A):
    det = A[0][0]*A[1][1]*A[2][2] + A[0][2]*A[1][0]*A[2][1] + A[0][1]*A[1][2]*A[2][0] - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1]
    return det

def classificeer(A, d, D):
    aard = 0
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
    return aard

def xyWegwerken(A):
    nieuweA = A
    return nieuweA