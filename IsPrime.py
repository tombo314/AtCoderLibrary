def is_prime(n):
    """ 
    n が素数ならTrue、素数でなければFalseを返す
    時間計算量 O(√n)
    """
    if n<=1 or type(n)!=int:
        print(1)
        return False
    i = 2
    while i**2<=n:
        if n%i==0: return False
        i += 1
    return True
