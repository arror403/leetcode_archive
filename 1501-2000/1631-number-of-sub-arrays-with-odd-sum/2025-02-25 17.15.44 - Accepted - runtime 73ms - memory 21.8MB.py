class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1
        odd_count = res = current_sum = 0
        
        for v in arr:
            current_sum = (current_sum + v) % 2
            
            if current_sum == 0:
                res = (res + odd_count) % MOD
                even_count += 1
            else:
                res = (res + even_count) % MOD
                odd_count += 1
        

        return res