class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        
        for v,f in Counter(answers).items():
            # We need ceiling(f/(v+1)) groups of this color
            groups=ceil(f/(v+1))
            # Each group has (v+1) rabbits
            res+=groups*(v+1)
        

        return res


        # res=0
        # d=Counter(answers)

        # for v,f in d.items():
        #     if f==1:
        #         res+=(v+1)
        #     else:
        #         res+=v


        # return res+1+d[0]