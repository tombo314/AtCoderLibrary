from collections import deque

def euler_tour(G, root=1):
    n = len(G)
    euler = []
    dq = deque([root])
    dq2 = deque()
    visited = [0] * n
    while dq:
        u = dq.pop()
        euler += [u]
        if visited[u]:
            continue
        for v in G[u]:
            if visited[v]:
                dq += [v]
            # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
            else:
                dq2 += [v]
        dq.extend(dq2)
        dq2 = deque()
        visited[u] = 1
    return euler
