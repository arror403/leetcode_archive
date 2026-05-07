class Solution:
    def smallestNumber(self, s):
        res, pool = [], list('987654321')
        for k in map(len,s.split('I')):
            res += [pool.pop() for _ in range(k + 1)][::-1]
        return ''.join(res)