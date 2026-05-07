class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        m,f=[],True
        for i in range(len(nums)):
            if nums[i]==1:
                m.append(i)
        # print(m)
        for i in range(1,len(m)):
            if (m[i]-m[i-1]-1)>=k:
                continue
            else:
                f=False
                break
                
        return f
            