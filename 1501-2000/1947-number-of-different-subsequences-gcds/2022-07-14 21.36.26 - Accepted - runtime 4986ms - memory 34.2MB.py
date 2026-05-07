class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:        
        nums = set(nums)
        max_num = max(nums)
        limit = max_num//2
        res = 0
        for i in range(1, max_num+1):
            if i in nums:
                res += 1
            elif i <= limit:
                curr_gcd = 0
                for j in range(i*2, max_num+1, i):
                    if j not in nums: 
                        continue
                    if curr_gcd == 0: 
                        curr_gcd = j
                    else:
                        curr_gcd = math.gcd(j, curr_gcd)
                        if curr_gcd == i:
                            res += 1
                            break
        return res