class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l, r = deque([nums[0]]), deque(nums[1:])
        l_max, r_min = nums[0], min(nums[1:])

        for i in range(1, len(nums)-1):
            if l_max > r_min:
                l.append(nums[i])
                if nums[i] > l_max: 
                    l_max = nums[i]
                if r.popleft() == r_min: 
                    r_min = min(r)
            else:
                break
                
        
        return len(l)