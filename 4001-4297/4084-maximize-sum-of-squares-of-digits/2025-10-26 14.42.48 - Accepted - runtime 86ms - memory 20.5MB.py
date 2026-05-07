class Solution:
    def maxSumOfSquares(self, e: int, s: int) -> str:
        if s > 9*e: return ""

        a, b = divmod(s, 9)

        if b == 0:
            res = ''.join('9'*a + '0'*(e-a))
        else:
            res = ''.join('9'*a + str(b) + '0'*(e-a-1)) 


        return res

        # res = {}

        # for x in range(10**(e-1), 10**e):
        #     tmp = list(map(int, str(x)))
        #     if sum(tmp) == s:
        #         res[x] = sum(d**2 for d in tmp)

        # if res:
        #     res = sorted(res.items(), key = lambda x:(x[1], x[0]))
        #     return str(res[-1][0])


        # return ""