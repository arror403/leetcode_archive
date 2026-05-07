class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        L=len(height)
        if (not height or L==0): return 0

        maxArea=0
        lessFromLeft=[0]*L  # idx of the first bar the left that is lower than current
        lessFromRight=[0]*L # idx of the first bar the right that is lower than current
        lessFromRight[-1]=L
        lessFromLeft[0]=-1

        for i in range(1,L):
            p=i-1 
            while (p>=0 and height[p]>=height[i]):
                p=lessFromLeft[p]
            lessFromLeft[i]=p

        for i in range(L-2,-1,-1):
            p=i+1
            while (p<L and height[p]>=height[i]):
                p=lessFromRight[p]
            lessFromRight[i]=p

        for i in range(L):
            maxArea=max(maxArea, height[i]*(lessFromRight[i]-lessFromLeft[i]-1))


        return maxArea