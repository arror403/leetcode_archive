class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        N=map(str,nums)
        d={str(k):str(v) for k,v in enumerate(mapping)}

        res=[int(''.join([d[c] for c in n])) for n in N]


        return [x for x,_ in sorted(zip(nums,res), key=lambda x:x[1])]