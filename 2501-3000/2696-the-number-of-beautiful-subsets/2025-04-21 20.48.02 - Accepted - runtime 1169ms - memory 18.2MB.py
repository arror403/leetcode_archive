class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq={}
        nums.sort()

        def f(i: int) -> int:
            if i==len(nums): return 1   # base case

            res=f(i+1)                  # nums[i] not taken

            if nums[i]-k not in freq:   # check if we can take nums[i]
                freq[nums[i]]=freq.get(nums[i], 0)+1
                res+=f(i+1)             # nums[i] taken
                freq[nums[i]]-=1
                
                if freq[nums[i]]==0: del freq[nums[i]]
                    
            return res


        return f(0)-1 # -1 for empty subset