class Solution:
    def numDecodings(self, s: str) -> int:

        ##### power by chatGPT #####

        memo = {}

        def helper(index):
            if index==len(s): return 1

            if s[index]=='0': return 0

            if index in memo: return memo[index]

            ways=helper(index+1)

            if (index+1)<len(s) and (s[index]=='1' or (s[index]=='2' and '0'<=s[index+1]<='6')):
                ways+=helper(index+2)

            memo[index]=ways
            return ways

        return helper(0)