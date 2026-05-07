class Solution:
    def countLargestGroup(self, n: int) -> int:
        d=Counter()
        res=0

        for i in range(1, n+1): d[sum(map(int, str(i)))]+=1
        m=max(d.values())


        return list(d.values()).count(m)