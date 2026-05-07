class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        s = [5,13,17,25,29,37,41,53,61,65,65,73,85,85,89,97,101,109,113,125,137,145,145,149,157,169,173,181,185,185,193,197,205,205,221,221,229,233,241]
        
        for x in s:
            tmp=1
            while tmp*x <= n:
                tmp += 1
                res += 2
                

        return res