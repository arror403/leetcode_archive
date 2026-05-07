class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        for i in range(len(nums)-2):
            # print (i,i+1,i+2)
            if self.area(nums[i],nums[i+1],nums[i+2]) > 0:
                return (nums[i]+nums[i+1]+nums[i+2])
            
        return 0
        
        # print(nums)
        # print(self.area(nums[0],nums[1],nums[2]))
        
        
    def area(self, a, b, c):
        s=(a+b+c)/2
        # calculate the area
        if (s*(s-a)*(s-b)*(s-c))<0: return 0
        return (s*(s-a)*(s-b)*(s-c))**0.5