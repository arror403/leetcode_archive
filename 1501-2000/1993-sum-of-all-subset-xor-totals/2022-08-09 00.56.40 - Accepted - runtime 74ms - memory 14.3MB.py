class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum=0
        for i in range(1,len(nums)+1):
            tmp=list(itertools.combinations(nums,i))
            tmp=[list(i) for i in tmp]
            for j in tmp:
                sum+=reduce(xor,j)
            # print (tmp)
            
        return sum
    
    def xor(self, x, y):
        return x^y