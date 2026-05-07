class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        n=len(nums[0])
        
        for i in range(2**n):
            tmp=bin(i)[2:]

            while len(tmp)!=n: tmp='0'+tmp
            # print(tmp)

            if tmp not in nums:
                return tmp