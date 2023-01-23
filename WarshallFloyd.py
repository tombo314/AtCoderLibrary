def warshall_floyd(N, dist):
    """
    N:頂点数
    dist:頂点間のコストが入った2次元配列（INFで初期化）
    """
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i+1][j+1] = min(dist[i+1][j+1], dist[i+1][k+1]+dist[k+1][j+1])
    return dist
