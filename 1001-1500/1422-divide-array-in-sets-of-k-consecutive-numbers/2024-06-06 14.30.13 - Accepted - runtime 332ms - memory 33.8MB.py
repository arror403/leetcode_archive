class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d=Counter(nums)
        m=d.keys()

        for v in sorted(m):
            if d[v]>0:
                for i in range(1, k):
                    next_num = v+i
                    if (next_num not in m) or (d[next_num] < d[v]): return False
                    d[next_num] -= d[v]

        return True