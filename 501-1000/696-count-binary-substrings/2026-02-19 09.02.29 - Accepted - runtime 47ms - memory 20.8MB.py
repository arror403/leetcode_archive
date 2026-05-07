class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # print(s.replace('01', '0 1'))
        # print(s.replace('01', '0 1').replace('10', '1 0'))
        # print(s.replace('01', '0 1').replace('10', '1 0').split())
        t = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        # print(s)
        return sum(min(t[i],t[i+1]) for i in range(len(t)-1))