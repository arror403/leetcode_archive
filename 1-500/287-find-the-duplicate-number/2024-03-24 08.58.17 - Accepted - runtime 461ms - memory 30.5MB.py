class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

# solution from https://www.youtube.com/watch?v=pKO9UjSeLew

        tortoise=nums[0]
        hare=nums[0]

        while 1:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]
            if tortoise==hare:
                break
        
        ptr1=nums[0]
        ptr2=tortoise

        while ptr1!=ptr2:
            ptr1=nums[ptr1]
            ptr2=nums[ptr2]

        return ptr1