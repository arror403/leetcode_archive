class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c=nums[0]%2
        odd=even=both=0

        for v in nums:
            if v%2: odd+=1
            else: even+=1
            
            if v%2==c: 
                both+=1
                c=1-c  # Toggle the parity


        return max(both, max(even, odd))


        # m=[v%2 for v in nums]

        # return max(len(m)-sum(m), sum(m))