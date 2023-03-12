import numpy as np
def matrix_exponentiation(mtx,n,M=998244353):
    """ mtx: ndarray, n: power, M: modulo """
    if n == 0: return np.eye(len(mtx), dtype='object')
    if n == 1: return mtx
    m2, p2 = mtx, 2
    while p2 < n:
        m2 = (m2.dot(m2)) % M
        p2 *= 2
    return matrix_exponentiation(mtx,(n-p2//2),M).dot(m2) % M