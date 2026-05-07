class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m=[j for i in range(1,len(nums)+1) for j in combinations(nums,i)]
        k=[reduce(operator.or_ , x) for x in m]

        return k.count(max(k))