# 1-indexed
class UnionFind:
    def __init__(self, n):
        """ 0 から n までの要素を作成 """
        self.ary = list(range(n+1))
    
    def two_to_onedem(self, h, w, W):
        """ 現在の座標 (h, w)、横の長さ W """
        return (h-1)*W + w
    
    def find(self, x):
        """ 根を見つける """
        if self.ary[x]==x:
            return x
        else:
            self.ary[x] = self.find(self.ary[x])
            return self.ary[x]

    def same(self, x, y):
        """ 根が同じか判別する """
        return self.find(x)==self.find(y)

    def unite(self, x, y):
        """ 新たに素集合に要素を追加する """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        self.ary[x] = y