class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res=set()

        for i in nums:
            res = res | {x for x in range(i[0],i[1]+1)}

        # return len([{x for x in range(i[0],i[1]+1)} for i in nums])

        return len(res)