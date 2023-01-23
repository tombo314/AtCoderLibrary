import heapq

class DoubleHeap:
    def __init__(self):
        self.minh = []
        self.maxh = []
        self.d = dict()
        self.size = 0
        self.total = 0

    def push(self, x):
        self.size += 1
        self.total += x
        heapq.heappush(self.minh, x)
        heapq.heappush(self.maxh, -x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def get_min(self):
        return self.minh[0]

    def get_max(self):
        return -self.maxh[0]

    def pop_min(self):
        n = self.get_min()
        self.discard(n)
        return n

    def pop_max(self):
        n = self.get_max()
        self.discard(n)
        return n

    def discard(self, x):
        if self.is_exist(x):
            self.size -= 1
            self.total -= x
            self.d[x] -= 1
            if self.d[x] == 0:
                del self.d[x]

            while len(self.minh) != 0 and self.minh[0] not in self.d:
                heapq.heappop(self.minh)
            while len(self.maxh) != 0 and -self.maxh[0] not in self.d:
                heapq.heappop(self.maxh)
            return True
        return False

    def erase(self, x, n=10 ** 18):
        if self.is_exist(x):
            if self.d[x] < n:
                n = self.d[x]
            self.size -= n
            self.total -= x * n
            self.d[x] -= n
            if self.d[x] == 0:
                del self.d[x]

            while len(self.minh) != 0 and self.minh[0] not in self.d:
                heapq.heappop(self.minh)
            while len(self.maxh) != 0 and -self.maxh[0] not in self.d:
                heapq.heappop(self.maxh)
            return n
        return 0

    def is_exist(self, x):
        if x in self.d:
            return True
        else:
            return False

    def __len__(self, x):
        return self.size

    def len(self):
        return self.size

    def types(self):
        return len(self.d)

    def sum(self):
        return self.total

    def count(self, x):
        if self.is_exist(x):
            return self.d[x]
        return 0