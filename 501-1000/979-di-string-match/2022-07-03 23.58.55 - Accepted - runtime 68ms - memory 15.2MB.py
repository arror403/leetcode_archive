class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        b=[]
        n=0
        m=len(s)
        if s[-1]=="I":
            s+="I"
        elif s[-1]=="D":
            s+="D"
            
        
        for i in s:
            if i == "D":
                b.append(m)
                m-=1
            elif i == "I":
                b.append(n)
                n+=1
        return b