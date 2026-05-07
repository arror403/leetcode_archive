class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d,res=[0]*26,[]
        
        for i in text: d[ord(i)-97]+=1
        
            
        res.append(d[ord('b')-97])
        res.append(d[ord('a')-97])
        res.append(d[ord('l')-97]//2)
        res.append(d[ord('o')-97]//2)
        res.append(d[ord('n')-97])
        
        return min(res)