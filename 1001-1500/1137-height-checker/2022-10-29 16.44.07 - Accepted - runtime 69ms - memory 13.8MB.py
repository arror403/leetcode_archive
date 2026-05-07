class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        r=sorted(heights)
        res=0
        for i in range(len(heights)):
            if heights[i]!=r[i]:
                res+=1

        return res