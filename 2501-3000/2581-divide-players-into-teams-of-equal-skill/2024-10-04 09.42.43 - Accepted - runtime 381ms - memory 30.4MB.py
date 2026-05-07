class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s=int(2*sum(skill)/len(skill))
        chemistry=0
        d=Counter(skill)
        
        for v,f in d.items():
            if (s-v) not in d or d[s-v]!=f:
                return -1
            else:
                chemistry+=f*v*(s-v)


        return chemistry//2