class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d=[[0]*26 for _ in range(26)]
        res=0

        for w in words:
            a, b = ord(w[0])-97, ord(w[1])-97
            if d[b][a]:
                res+=4
                d[b][a]-=1
            else: 
                d[a][b]+=1
    
        for i in range(26):
            if d[i][i]:
                res+=2
                break


        return res