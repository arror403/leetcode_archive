class Solution:
    def robotWithString(self, s: str) -> str:
        def low(freq):
            for i in range(26):
                if freq[i]:
                    return 97+i
            return 97
    
        t=[]
        res=""
        freq=[0]*26
        for c in s: freq[ord(c)-97]+=1            
        
        for c in s:
            t.append(ord(c))
            freq[ord(c)-97]-=1
            while t and t[-1]<=low(freq):
                tmp=t.pop()
                res+=chr(tmp)
        
        while t: 
            tmp=t.pop()
            res+=chr(tmp)


        return res