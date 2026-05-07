class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2: return True

        c=0
        set1=set()
        set2=set()
        
        for a,b in zip(s1,s2):
            if a!=b:
                set1.add(a)
                set2.add(b)
                c+=1
        
        return False if c!=2 else set1==set2