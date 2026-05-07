class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=Counter(s)
        res=""
        res+=(c['1']-1)*'1'
        res+=(c['0'])*'0'
        res+='1'

        return res