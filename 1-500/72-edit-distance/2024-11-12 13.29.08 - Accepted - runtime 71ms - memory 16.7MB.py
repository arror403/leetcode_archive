class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        cur=[0]*(n+1)

        for j in range(1,n+1): cur[j]=j

        for i in range(1,m+1):
            pre=cur[0]
            cur[0]=i
            for j in range(1,n+1):
                tmp=cur[j]
                if word1[i-1]==word2[j-1]:
                    cur[j]=pre
                else:
                    cur[j] = min(pre, min(cur[j-1], cur[j])) + 1
                
                pre=tmp


        return cur[n]