# トポロジカルソート
def topological_sort(g, n):
    """ 
    g : ソートするグラフ
    n : 頂点数
    """
    from collections import deque
    l = deque([])
    seen = [False]*(n+1)
    def __dfs__(v):
        if seen[v]==False:
            seen[v] = True
            for w in g[v]:
                __dfs__(w)
            l.appendleft(v)
    for i in range(1, n+1):
        __dfs__(i)
    return list(l)
