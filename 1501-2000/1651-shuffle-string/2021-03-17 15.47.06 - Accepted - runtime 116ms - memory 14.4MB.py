class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        b=[]
        for i in range(0,len(s)):
            for j in range(0,len(indices)):
                if(indices[j]==i):
                    b.append(s[j])
                    
        b=''.join(b)
        return b