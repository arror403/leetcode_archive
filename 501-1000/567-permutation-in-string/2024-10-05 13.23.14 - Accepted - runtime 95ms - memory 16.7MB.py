class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1,L2=len(s1),len(s2)
        if L2<L1: return False

        c=Counter(s1)
        l,r=0,L1-1
        s=Counter(s2[l:r])

        while r<L2:
            s[s2[r]]+=1
            if s==c:
                return True

            s[s2[l]]-=1

            if s[s2[l]]==0:
                del s[s2[l]]

            l+=1
            r+=1


        return False