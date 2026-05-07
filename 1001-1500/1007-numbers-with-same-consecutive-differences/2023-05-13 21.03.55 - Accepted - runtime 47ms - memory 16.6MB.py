class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        
        # initialize the result list with single-digit numbers
        res = list(range(1, 10))
        
        # loop over the remaining digits to build the numbers of length n
        for i in range(n-1):
            new_res = []
            for x in res:
                last_digit = x % 10
                if last_digit + k < 10:
                    new_res.append(x*10 + last_digit + k)
                if k != 0 and last_digit - k >= 0:
                    new_res.append(x*10 + last_digit - k)
            res = new_res
            
        return res