class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a,b,f=[0]*26,[0]*26,True
        for i in word1: a[ord(i)-97]+=1
        for i in word2: b[ord(i)-97]+=1
            
        for i in range(26):
            if abs(a[i]-b[i])>3:
                f=False
                break
                
        return f