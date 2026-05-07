class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def getMin(r):
            m = inf
            idx = 0

            for i in range(len(r)):
                if (r[i] < m):
                    m = r[i]
                    idx = i

            return [m, idx]
        
        arr=[0]*2

        for i in range(k):
            arr = getMin(nums)
            nums[arr[1]] = arr[0] * multiplier


        return nums