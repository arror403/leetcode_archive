class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # i=0
        stack=[]
        res=[-1]*n

        for i in range(n*2):
            while stack and (nums[stack[-1]]<nums[i%n]):
                res[stack.pop()]=nums[i%n]
            stack.append(i%n)

        return res
            # if m[i+1]<m[i]:
            #     i+=1
            # else:
            #     res+=[m[i+1]]*(i-j+1)
            #     i=j