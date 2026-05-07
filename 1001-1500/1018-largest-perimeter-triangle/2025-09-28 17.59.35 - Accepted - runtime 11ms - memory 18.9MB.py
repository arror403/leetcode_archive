class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def area(a, b, c):
            s = (a+b+c)/2
            return 0 if (s<a or s<b or s<c) else (s*(s-a)*(s-b)*(s-c))**(1/2)

        nums.sort(reverse=True)

        for i in range(len(nums)-2):
            if area(nums[i], nums[i+1], nums[i+2]) > 0:
                return nums[i] + nums[i+1] + nums[i+2]
            

        return 0

# max(0.5 * abs(i[0]*j[1] + j[0]*k[1] + k[0]*i[1] - j[0]*i[1] - k[0]*j[1] - i[0]*k[1])
#                for i, j, k in combinations(points, 3))