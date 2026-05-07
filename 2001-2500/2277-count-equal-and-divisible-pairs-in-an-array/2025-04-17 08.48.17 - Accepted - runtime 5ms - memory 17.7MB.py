class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d=defaultdict(list)
        res=0

        for i,v in enumerate(nums): d[v].append(i)

        for i in d.values():
            for a,b in combinations(i,2):
                if (a*b)%k==0:
                    res+=1


        return res