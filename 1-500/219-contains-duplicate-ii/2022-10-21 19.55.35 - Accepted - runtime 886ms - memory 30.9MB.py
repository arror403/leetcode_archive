class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        t=[]
        for i in range(len(nums)):
            # tmp=[nums[i],i]
            t.append([nums[i],i])
        t.sort(key=lambda x:x[0])
        # print(t)
        for i in range(len(t)-1):
            if t[i][0]==t[i+1][0] and abs(t[i][1]-t[i+1][1])<=k:
                return True
        return False