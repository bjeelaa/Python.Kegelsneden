def det2x2(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return det

def det3x3(A):
    det = A[0][0]*A[1][1]*A[2][2] + A[0][2]*A[1][0]*A[2][1] + A[0][1]*A[1][2]*A[2][0] - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1]
    return det

def wegMetDie_xy_term(A):
    pass