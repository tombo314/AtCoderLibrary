def _mat_mul(a, b, m) :
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= m
    return c

def mat_pow(x, n, m=998244353):
    """
    行列累乗
    x : 行列のlist
    n : 指数
    m : mod
    """
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = _mat_mul(x, y, m)
        x = _mat_mul(x, x, m)
        n //= 2

    return y