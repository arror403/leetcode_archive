class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.q=defaultdict(list)
        for i,v in enumerate(arr):
            self.q[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return self.count_elements_in_range(self.q[value], left, right)

    def count_elements_in_range(self, sorted_list, left, right):
        return bisect.bisect_right(sorted_list, right) - bisect.bisect_left(sorted_list, left)