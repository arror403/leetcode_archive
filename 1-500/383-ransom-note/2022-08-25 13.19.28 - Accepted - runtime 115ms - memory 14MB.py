class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m,n=[0]*26,[0]*26
        for i in ransomNote: m[ord(i)-97]+=1
            
        for i in magazine: n[ord(i)-97]+=1
            
            
        for i in range(26):
            if n[i]>=m[i]: continue
            else: return False
        
        return True