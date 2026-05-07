class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a=[]
        b=[]
        
        for i in word1:
            a.append(i)
        for j in word2:
            b.append(j)
            
        a=''.join(a)
        b=''.join(b)
        
        if a==b: return 1
        else : return 0