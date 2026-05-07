class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s=int(2*sum(skill)/len(skill))
        chemistry=0
        d=defaultdict(int)
        
        for i in skill: d[i]+=1
        
        for v,c in d.items():
            if (s-v) not in d or d[s-v]!=c:
                return -1
            else:
                chemistry+=c*v*(s-v)


        return chemistry//2