class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = deque()
        s3 = float('-inf')  # Initialize the third element as negative infinity

        for num in reversed(nums):
            if num < s3:
                return True

            while stack and num > stack[-1]:
                s3 = stack.pop()

            stack.append(num)

        return False





        # st=deque()
        # curr_min = inf
        # for i in range(len(nums)):

        #     while (st and nums[i] >= st[-1][1]):
        #         st.pop()

        #     if (st and nums[i] < st[-1][1] and nums[i] > st[-1][0]):
        #         return True
            
        #     st.append((curr_min,nums[i]))
        #     curr_min=min(curr_min,nums[i])

        # return False