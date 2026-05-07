class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n==1: return ["0","1"]
        
        res=[]
        for i in range(1,2**n):
            F=1
            for a,b in pairwise((t:=bin(i)[2:].zfill(n))): 
                if a==b and b=="0":
                    F=0
                    break

            if F: res.append(t)


        return res