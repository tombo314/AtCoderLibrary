def coord_compress(l):
    """ 座標圧縮 O(len(l)) """
    sorted_l = sorted(set(l))
    ranking = {v:i for i,v in enumerate(sorted_l)}
    compressed = []
    for v in l:
        compressed.append(ranking[v])
    return compressed
