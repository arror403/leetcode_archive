class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def factors(n):
            s=set()
            for i in range(1, int(n**0.5)+1):
                if n%i==0:
                    s.add(i)
                    s.add(n//i)

            return s

        res=0
        for v in nums:
            if len(factors(v))==4: 
                res+=sum(factors(v))

        return res