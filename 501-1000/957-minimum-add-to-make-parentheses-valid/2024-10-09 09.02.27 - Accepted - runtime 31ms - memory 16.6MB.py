class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left=right=0

        for c in s:
            if right==0 and c==')':
                left+=1
            else:
                right+=1 if c=='(' else -1


        return left+right