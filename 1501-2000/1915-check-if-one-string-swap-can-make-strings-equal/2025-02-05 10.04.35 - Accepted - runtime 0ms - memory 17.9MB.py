class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        set1=set()
        set2=set()
        
        for a,b in zip(s1, s2):
            if a!=b:
                set1.add(a)
                set2.add(b)
                c+=1
        
        if c!=0 and c!=2: return False

        return set1==set2