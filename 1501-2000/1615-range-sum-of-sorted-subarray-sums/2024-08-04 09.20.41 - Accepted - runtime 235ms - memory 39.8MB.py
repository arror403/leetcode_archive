class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        all_sums=[]

        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum+=nums[j]
                all_sums.append(curr_sum)
        
        all_sums.sort()

        return sum(all_sums[left-1:right])%(10**9+7)