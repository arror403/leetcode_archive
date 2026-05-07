class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            f=True
            for v in range(1001):
                if (v|(v+1))==i:
                    ans.append(v)
                    f=False
                    break

            if f: ans.append(-1)


        return ans