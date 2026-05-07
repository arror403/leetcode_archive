class Solution:
    def decodeMessage(self,key : str, message: str) -> str:
        val = 'abcdefghijklmnopqrstuvwxyz'
        mp = {}
        ans = ''
        c = 0
        for i in key:
            if i!=" " and i not in mp  :
                mp[i] = val[c]
                c += 1
        for i in message:
            if i != " ":
                ans += mp[i]
            else:
                ans += i
        return ans