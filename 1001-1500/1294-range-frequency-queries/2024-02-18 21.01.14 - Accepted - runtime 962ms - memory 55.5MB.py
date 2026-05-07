class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.q=defaultdict(list)
        for i,v in enumerate(arr):
            self.q[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.q[value],right)-bisect_left(self.q[value],left)