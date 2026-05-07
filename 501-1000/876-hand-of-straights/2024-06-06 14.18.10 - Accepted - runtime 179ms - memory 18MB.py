class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        d=Counter(nums)

        for v in sorted(d.keys()):
            if d[v]>0:
                for i in range(1, k):
                    next_num = v + i
                    if next_num not in d.keys() or d[next_num]<d[v]:
                        return False
                    d[next_num] -= d[v]
                    
                    if d[next_num]==0: del d[next_num]

        return True