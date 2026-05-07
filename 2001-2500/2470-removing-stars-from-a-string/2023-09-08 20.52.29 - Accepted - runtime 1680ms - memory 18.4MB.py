class Solution:
    def removeStars(self, s: str) -> str:
        return self.newString(s)


    def newString(self, S):
        
        q = []
    
        for i in range(len(S)):
            if S[i] != '*':
                q.append(S[i])
            elif len(q) != 0:
                q.pop()
    
        # Build final string
        ans = ""
    
        while len(q) != 0:
            ans += q[0]
            q.pop(0)
    
        # return final string
        return ans