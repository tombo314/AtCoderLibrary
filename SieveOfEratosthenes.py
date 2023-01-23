import math

def sieve_of_eratosthenes(n):
    """ 
    n 以下の素数を列挙する。
    O(nloglogn)
    """
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    
    ary = []
    for i in range(len(prime)):
        if prime[i]==True:
            ary.append(i)
    return ary
