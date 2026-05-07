class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # // Decreasing stack with (n1, n2) pair
        st=deque()
        curr_min = inf
        # for (int i=0; i<nums.size(); i++)
        for i in range(len(nums)):

            while (st and nums[i] >= st[-1][1]):
                st.pop()

            if (st and nums[i] < st[-1][1] and nums[i] > st[-1][0]):
                return True
            
            st.append((curr_min,nums[i]))
            curr_min=min(curr_min,nums[i])

        return False