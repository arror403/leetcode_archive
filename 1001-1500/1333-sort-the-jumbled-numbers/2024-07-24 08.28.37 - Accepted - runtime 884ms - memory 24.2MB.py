class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        N=map(str,nums)
        d={str(k):str(v) for k,v in enumerate(mapping)}
        res=[]

        for n in N:
            tmp=''
            for c in n:
                tmp+=d[c]
            res.append(int(''.join(tmp)))


        return [x for x,_ in (sorted(zip(nums,res), key=lambda x:x[1]))]