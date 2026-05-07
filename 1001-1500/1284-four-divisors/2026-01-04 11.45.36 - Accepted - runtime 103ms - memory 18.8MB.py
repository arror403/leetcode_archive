class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            last_d = 0
            for i in range(2, int(n**(0.5))+1):
                if n%i == 0:
                    if last_d == 0:
                        last_d = i
                    else:
                        last_d = 0
                        break
            
            if last_d > 0 and last_d != n//last_d:
                res += 1 + n + last_d + n//last_d
        

        return res