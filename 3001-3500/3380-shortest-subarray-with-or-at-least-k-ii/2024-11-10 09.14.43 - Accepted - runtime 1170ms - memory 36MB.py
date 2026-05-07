class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def perform_or_operation(bit_count, or_val, num):
            """Helper function to perform OR operation and update bit counts"""
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] += 1
                    if bit_count[bit] == 1:
                        or_val |= (1 << bit)
            return or_val

        def nullify_or_operation(bit_count, or_val, num):
            """Helper function to remove a number's contribution from OR operation"""
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] -= 1
                    if bit_count[bit] == 0:
                        or_val &= ~(1 << bit)
            return or_val


        or_val = 0
        ans = float('inf')
        bit_count = [0] * 32
        j = 0
        
        for i in range(len(nums)):
            # Add current number to OR sum
            or_val = perform_or_operation(bit_count, or_val, nums[i])
            
            if or_val < k:
                continue
                
            # Try to minimize window by removing elements from start
            while j <= i and or_val >= k:
                ans = min(ans, i - j + 1)
                or_val = nullify_or_operation(bit_count, or_val, nums[j])
                j += 1
        
        
        return -1 if ans == float('inf') else ans





        # orVal=0
        # res=inf
        # bitCount=[0]*32

        # def performOrOperation(bitCount, orVal, n):
        #     orVal |= n
        #     for t in range(32):
        #         if (n & (1 << t)): bitCount[t]+=1


        # def nullifyOrOperation(bitCount, orVal, n):
        #     for t in range(32):
        #         if (n & (1 << t)): bitCount[t]-=1
        #         if bitCount[t]==0: orVal&=(~(1<<t))

        # j=0
        # for i in range(len(nums)):
        #     performOrOperation(bitCount, orVal, nums[i])
        #     if orVal<k: continue
        #     while(j<=i and orVal>=k):
        #         nullifyOrOperation(bitCount, orVal, nums[j])
        #         res=min(res, i-j+1)
        #         j+=1


        # return -1 if res==inf else res