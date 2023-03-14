from math import sqrt, ceil
from operator import itemgetter
class Mo:
    def __init__(self, ls):
        self.ls = ls
        self.n = len(ls)
        self.b = ceil(sqrt(self.n))  # bukectのサイズ及び個数

    def _init_states(self):
        ########################################
        # その時点における状態
        self.ans = 0
        self.cnt = [0]*(N+1)
        ########################################

        # [l,r)の半開区間で考える
        self.l = 0
        self.r = 0

        # queryを格納する用
        self.bucket = [[] for _ in range((self.b+1))]

    def _add(self, i):
        # i番目の要素を含めて考えるときへstatesを更新
        # O(1)で区間を伸縮する
        if self.cnt[self.ls[i]]==0:
            self.ans += 1
        self.cnt[self.ls[i]] += 1

    def _delete(self, i):
        # i番目の要素を削除して考えるときへstatesを更新
        # O(1)で区間を伸縮する
        if self.cnt[self.ls[i]]==1:
            self.ans -= 1
        self.cnt[self.ls[i]] -= 1

    def _one_process(self, l, r):
        # クエリ[l,r)に対してstatesを更新する
        for i in range(self.r, r):  # rまで伸長
            self._add(i)
        for i in range(self.r-1, r-1, -1):  # rまで短縮
            self._delete(i)
        for i in range(self.l, l):  # lまで短縮
            self._delete(i)
        for i in range(self.l-1, l-1, -1):  # lまで伸長
            self._add(i)

        self.l = l
        self.r = r

    def process(self, queries):
        self._init_states()

        for i, (l, r) in enumerate(queries):  # queryをbucketに格納
            self.bucket[l//self.b].append((l, r, i))

        for i in range(len(self.bucket)):
            self.bucket[i].sort(key=itemgetter(1))

        ret = [-1]*len(queries)
        for b in self.bucket:
            for l, r, i in b:  # クエリに答えていく
                self._one_process(l, r)
                ########################################
                # クエリに答える作業をここで書く
                ret[i] = self.ans
                ########################################
        return ret

N,Q = map(int, input().split())
C = list(map(int, input().split()))
queries = []
for _ in range(Q):
    l, r = list(map(int, input().split()))
    queries.append((l - 1, r))

mo = Mo(C)
ans = mo.process(queries)
print(*ans, sep='\n')