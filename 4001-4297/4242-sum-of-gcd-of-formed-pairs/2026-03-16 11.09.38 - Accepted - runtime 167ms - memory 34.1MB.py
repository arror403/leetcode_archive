class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        m=[]
        lm=-inf

        for v in nums:
            if v>lm: lm=v
            m.append(gcd(v, lm))

        res=0
        m=deque(sorted(m))
        while len(m)>1:
            a,b=m.popleft(),m.pop()
            res+=gcd(a, b)
        # print(m)

        return res