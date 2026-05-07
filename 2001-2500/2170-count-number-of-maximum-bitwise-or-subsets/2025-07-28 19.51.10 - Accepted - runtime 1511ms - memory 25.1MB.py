class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m=[j for i in range(1,len(nums)+1) for j in combinations(nums,i)]
        c=-inf

        for i in m: c=max(c, reduce(lambda x,y: x|y, i))
                
                
        return sum(1 for i in m if reduce(lambda x,y: x|y, i)==c)