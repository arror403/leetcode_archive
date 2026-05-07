class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m=[list(j) for i in range(1,len(nums)+1) for j in itertools.combinations(nums,i)]
        k=[reduce(self.fun_or,i) for i in m]
        return k.count(max(k))
    
    
    def fun_or(self, a, b):
        return a | b